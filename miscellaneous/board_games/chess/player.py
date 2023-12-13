import pickle
from socket import *
from constants import *
from threading import Thread

class Player:
    def __init__(self):
        self.game_trigger = None
        self.player_tag = input("Enter username: ")
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.opponent_socket = socket(AF_INET, SOCK_STREAM)
        self.opponent_connection = None
        self.move_history = []
        self.__join_server()
        self.__start_server_listener()

    def __join_server(self):
        self.server_socket.connect(PLAYER_DIRECTORY_ADDR)
        message = (RequestType.SET_NAME, self.player_tag)
        self.server_socket.send(pickle.dumps(message))
        response = self.server_socket.recv(PACKET_MAX_SIZE)
        request_type, _ = pickle.loads(response)
        while request_type != RequestType.SUCCESS:
            self.player_tag = input("Username Taken. Please try again: ")
            message = (RequestType.SET_NAME, self.player_tag)
            self.server_socket.send(pickle.dumps(message))
            response = self.server_socket.recv(PACKET_MAX_SIZE)
            request_type, _ = pickle.loads(response)

    def leave_server(self):
        message = (RequestType.LEAVE_SERVER, None)
        self.server_socket.send(pickle.dumps(message))
        self.server_socket.close()

    def list_players(self):
        message = (RequestType.LIST_ALL, None)
        self.server_socket.send(pickle.dumps(message))

    def game_request(self, opponent_tag):
        message = (RequestType.GAME_REQUEST, (self.player_tag, opponent_tag))
        self.server_socket.send(pickle.dumps(message))

    # listen for server interrupts
    def __start_server_listener(self):
        server_thread = Thread(target=self.__server_handler, args=())
        server_thread.daemon = True
        server_thread.start()

    # handle server-originated interrupts
    def __server_handler(self):
        while True:
            message = self.server_socket.recv(PACKET_MAX_SIZE)
            request_type, payload = pickle.loads(message)
            if request_type == RequestType.GAME_REQUEST:
                user_from, _ = payload
                response = input(f"Incoming-request from {user_from}. Type \"Accept\" or \"Reject\": ")
                if response.lower() == "reject":
                    self.server_socket.send(pickle.dumps((RequestType.REJECT_GAME, None)))
                elif response.lower() == "accept":
                    # start listening
                    self.opponent_socket.bind(('localhost', 0)) 
                    self.opponent_socket.listen()
                    # notify server of listening address
                    message = (RequestType.ACCEPT_GAME, (user_from, self.opponent_socket.getsockname()))
                    self.server_socket.send(pickle.dumps(message))
            elif request_type == RequestType.INITIALISE_REQUESTED:
                # trigger start of game, server handler moves into opponent handler context
                self.game_trigger = payload
                self.__opponent_handler()
            elif request_type == RequestType.INITIALISE_REQUESTING:
                print("Request Accepted. Game initialising...")
                listening_addr, game_orientation = payload
                self.opponent_socket.connect(listening_addr)
                # trigger start of game, server handler moves into opponent handler context
                self.game_trigger = game_orientation
                self.__opponent_handler()
            elif request_type == RequestType.LIST_ALL:
                print(payload)
            elif request_type == RequestType.REJECT_GAME:
                print("Request Denied.")
            return False

    def __opponent_handler(self):
        connection, _ = self.opponent_socket.accept()
        self.opponent_connection = connection
        while True:
            if self.opponent_connection:
                message = self.opponent_connection.recv(PACKET_MAX_SIZE)
                move = pickle.loads(message)
            else:
                message = self.opponent_socket.recv(PACKET_MAX_SIZE)
                move = pickle.loads(message)
            if move == "termination": break
            self.move_history.append(move)

    def send_move(self, move):
        if self.opponent_connection:
            self.opponent_connection.send(pickle.dumps(move))
        else:
            self.opponent_socket.send(pickle.dumps(move))
        self.move_history.append(move)