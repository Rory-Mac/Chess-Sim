from socket import *
from constants import *

class Player:
    def __init__(self, user_handle=None):
        self.user_handle = user_handle
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.opponent_socket = socket(AF_INET, SOCK_STREAM)
        self.opponent_connection = None
        self.moves = []

    def set_user_handle(self, user_handle):
        self.user_handle = user_handle

    def join_player_directory(self):
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
        self.socket.send(message.encode('utf-8'))
        response = self.socket.recv(PACKET_MAX_SIZE)
        if response == "success":
            opponent_address = self.socket.recv(PACKET_MAX_SIZE)
            self.connect_to_opponent(opponent_address)
        elif response == "failure":
            return

    def listen_for_opponent(self):
        print("listening for opponent...")
        self.opponent_socket.bind(('localhost', 0))
        self.opponent_socket.listen()
        # notify player directory with listening port
        message = f"notify-game-address {self.opponent_socket.getsockname()}"
        self.server_socket.send(message.encode('utf-8'))
        # accept inbound connection to start game
        connection, address = self.opponent_socket.accept()
        self.opponent_connection = connection
        print(f"Connection accepted from opponent {address}")

    def connect_to_opponent(self, opponent_addr):    
        self.socket.connect(opponent_addr)
        print(f"Connection made and game started with {self.socket.getpeername()}")

    def make_move(self, move):
        if self.opponent_connection:
            self.opponent_connection.send(move.encode())
        else:
            self.opponent_socket.send(move.encode())
        self.moves.append(move)

    def get_opponent_move(self):
        if self.connection:
            move = self.opponent_connection.recv(PACKET_MAX_SIZE)
        else:
            move = self.opponent_socket.recv(PACKET_MAX_SIZE)
        self.moves.append(move)