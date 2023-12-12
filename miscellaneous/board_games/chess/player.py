from socket import *
from constants import *
from threading import Thread

class Player:
    def __init__(self, application):
        self.application = application
        self.game_trigger = None
        self.player_tag = input("Enter username: ")
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.opponent_socket = socket(AF_INET, SOCK_STREAM)
        self.opponent_connection = None
        self.move_history = []
        self.__join_server()
        self.__start_server_listener()

    def get_game_trigger(self):
        return self.game_trigger
    
    def reset_game_trigger(self):
        self.game_trigger = None

    def __join_server(self):
        self.server_socket.connect(PLAYER_DIRECTORY_ADDR)
        self.server_socket.send((RequestType.SET_NAME, self.player_tag).encode('utf-8'))
        request_type, _ = self.server_socket.recv(PACKET_MAX_SIZE)
        while request_type != RequestType.SUCCESS:
            self.player_tag = input("Username Taken. Please try again: ")
            self.server_socket.send((RequestType.SET_NAME, self.player_tag).encode('utf-8'))
            request_type, _ = self.server_socket.recv(PACKET_MAX_SIZE)

    def leave_server(self):
        self.server_socket.send((RequestType.LEAVE_SERVER).encode('utf-8'))
        self.server_socket.close()

    def list_players(self):
        self.server_socket.send((RequestType.LIST_ALL).encode('utf-8'))
        response = self.server_socket.recv(PACKET_MAX_SIZE)
        print(response)

    # returns player's game orientation if request accepted, else returns none
    def game_request(self, opponent_tag):
        self.server_socket.send((RequestType.GAME_REQUEST, (self.player_tag, opponent_tag)).encode('utf-8'))
        response_type, payload = self.server_socket.recv(PACKET_MAX_SIZE)
        if response_type == RequestType.INITIALISE_GAME:
            print("Request Accepted. Game initialising...")
            listening_addr, player_orientation = payload[0], payload[1]
            self.opponent_socket.connect(listening_addr)
            # start thread listening for opponent moves
            opponent_thread = Thread(target=self.__opponent_handler, args=())
            opponent_thread.start()
            return player_orientation
        if response_type == RequestType.REJECT_GAME:
            print("Request Denied.")
        return False

    def __listen_for_opponent(self):
        print("listening for opponent...")
        self.opponent_socket.bind(('localhost', 0))
        # notify server of listening address, start listening 
        self.server_socket.send((RequestType.ACCEPT_GAME, self.opponent_socket.getpeername()).encode('utf-8')) 
        self.opponent_socket.listen()
        # accept inbound opponent connection to start game
        connection, address = self.opponent_socket.accept()
        self.opponent_connection = connection
        print(f"Connection accepted from opponent {address}")

    # listen for server interrupts
    def __start_server_listener(self):
        server_thread = Thread(target=self.__server_handler, args=())
        server_thread.start()

    # handle server-originated interrupts
    def __server_handler(self):
        while True:
            request_type, payload = self.server_socket.recv(PACKET_MAX_SIZE)
            user_from, _ = payload
            if request_type == RequestType.GAME_REQUEST:
                response = input(f"Incoming-request from {user_from}. Type \"Accept\" or \"Reject\": ")
                if response.lower() == "reject":
                    self.server_socket.send((RequestType.REJECT_GAME).encode('utf-8'))
                elif response.lower() == "accept":
                    self.__listen_for_opponent()
                    game_orientation = self.server_socket.recv(PACKET_MAX_SIZE).decode('utf-8')
                    self.in_game = game_orientation
                    self.__opponent_handler()

    def __opponent_handler(self):
        while True:
            if self.opponent_connection:
                move = self.opponent_connection.recv(PACKET_MAX_SIZE)
            else:
                move = self.opponent_socket.recv(PACKET_MAX_SIZE)
            if move == "termination": break
            self.move_history.append(move)

    def send_move(self, move):
        if self.opponent_connection:
            self.opponent_connection.send(move.encode('utf-8'))
        else:
            self.opponent_socket.send(move.encode('utf-8'))
        self.move_history.append(move)