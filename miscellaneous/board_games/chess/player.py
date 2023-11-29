from socket import *
from enum import Enum

class PlayerState(Enum):
    ONLINE = 0
    INGAME = 1

class Player:
    def __init__(self, user_handle):
        self.user_handle = user_handle
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.connection = None
        self.moves = []
        self.player_state = PlayerState.ONLINE

    def listen(self):
        print("listening...")
        self.socket.bind(('localhost', 18000))
        self.socket.listen()
        connection, address = self.socket.accept()
        self.connection = connection
        print(f"Connection accepted from {address}")

    def connect(self):
        self.socket.connect(('localhost', 18000))
        print(f"Connection made with {self.socket.getpeername()}")

    def make_move(self, move):
        if self.connection:
            self.connection.send(move.encode())
        else:
            self.socket.send(move.encode())
        self.moves.append(move)

    def get_opponent_move(self):
        if self.connection:
            move = self.connection.recv(4096)
        else:
            move = self.socket.recv(4096)
        self.moves.append(move)
