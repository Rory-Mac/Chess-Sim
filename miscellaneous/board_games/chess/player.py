from socket import *
from constants import *
from threading import Thread

class Player:
    def __init__(self, application):
        self.application = application
        self.game_trigger = None
        self.user_handle = input("Enter username: ")
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.opponent_socket = socket(AF_INET, SOCK_STREAM)
        self.opponent_connection = None
        self.move_history = []
        self.__join_player_directory()
        self.__start_server_listener()

    def get_game_trigger(self):
        return self.game_trigger
    
    def reset_game_trigger(self):
        self.game_trigger = None

    def __join_player_directory(self):
        self.server_socket.connect(PLAYER_DIRECTORY_ADDR)
        print(f"Connection made with {self.server_socket.getpeername()}")
        message = f"set-username {self.user_handle}"
        self.server_socket.send(message.encode('utf-8'))

    def leave_player_directory(self):
        message = "leave"
        self.server_socket.send(message.encode('utf-8'))
        self.server_socket.close()

    def list_players(self):
        message = "list-all"
        self.server_socket.send(message.encode('utf-8'))
        response = self.server_socket.recv(PACKET_MAX_SIZE)
        print(response)

    def game_request(self, opponent_address):
        message = f"game-request {opponent_address}"
        self.server_socket.send(message.encode('utf-8'))
        response = self.server_socket.recv(PACKET_MAX_SIZE)
        response_words = response.split()
        if response_words[0] == "accepted":
            print("Request Accepted.")
            self.__connect_to_opponent(response_words[1])
            # start thread listening for opponent moves
            opponent_thread = Thread(target=self.__opponent_handler, args=())
            opponent_thread.start()
            return response_words[2] # game orientation
        if response_words[0] == "denied":
            print("Request Denied.")
        return False

    def __connect_to_opponent(self, opponent_addr):    
        self.opponent_socket.connect(opponent_addr)
        print(f"Connection made and game started with {self.opponent_socket.getpeername()}")

    def __listen_for_opponent(self):
        print("listening for opponent...")
        self.opponent_socket.bind(('localhost', 0))
        # notify player directory of listening address
        message = f"{self.opponent_socket.getsockname()}"
        self.server_socket.send(message.encode('utf-8')) 
        # start listening for opponent connection
        self.opponent_socket.listen()
        # accept inbound connection to start game
        connection, address = self.opponent_socket.accept()
        self.opponent_connection = connection
        print(f"Connection accepted from opponent {address}")

    # listen for server interrupts
    def __start_server_listener(self):
        server_thread = Thread(target=self.__server_handler, args=())
        server_thread.start()

    def __server_handler(self):
        while True:
            data = self.server_socket.recv(PACKET_MAX_SIZE)
            data_words = data.split()
            if data_words[0] == "incoming-request":
                response = input(f"Incoming-request from {data_words[1]}. Type \"Accept\" or \"Deny\": ")
                self.server_socket.send(response.encode('utf-8'))
                if response == "deny": continue
                elif response == "accept":
                    self.__listen_for_opponent()
                    game_orientation = self.server_socket.recv(PACKET_MAX_SIZE).decode('utf-8')
                    self.in_game = game_orientation
                    self.__opponent_handler()
            else:
                print(data)

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