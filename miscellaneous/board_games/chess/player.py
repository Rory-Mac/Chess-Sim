from socket import *

class Player:
    def __init__(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.connection = None
        self.moves = []

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

    def send_data(self, move):
        if self.connection:
            self.connection.send(move.encode())
        else:
            self.socket.send(move.encode())
        self.moves.append(move)

    def receive_data(self):
        if self.connection:
            move = self.connection.recv(4096)
        else:
            move = self.socket.recv(4096)
        self.moves.append(move)
    
    def print_moves(self):
        for move in self.moves:
            print(f"{move} ", end="")
        print()

if __name__ == "__main__":
    player = Player()
    mode = input("Input mode [connect|listen]: ")
    if mode == "connect":
        player.connect()
    elif mode == "listen":
        player.listen()
    while True:
        cmd = input("Input: ")
        if cmd  == "list":
            player.print_moves()
        elif cmd == "move":
            move = input("Move: ")
            player.send_data(move)
        elif cmd == "get":
            player.receive_data()
