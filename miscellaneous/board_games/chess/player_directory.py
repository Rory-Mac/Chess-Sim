import threading
from socket import *
from constants import *

class PlayerDirectory:
    def __init__(self):
        self.connections = {}
        self.online_players = {}
        self.ingame_players = {}
        self.player_addresses = {}
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.__listen()

    def __listen(self):
        self.socket.bind(PLAYER_DIRECTORY_ADDR)
        self.socket.listen()
        while True:
            client_socket, client_address = self.socket.accept()
            print(f"Connection accepted from {client_address}")
            client_handler = threading.Thread(target=self.__client_handler, args=(client_socket))
            client_handler.start()
            
    def __client_handler(self, client_socket):
        while True:
            data = client_socket.recv(1024)
            if not data: break
            data = data.decode('utf-8')
            data_words = data.split()
            print(f"Received data from {client_socket.getpeername()}: {data}")
            if data_words[0] == "set-username":
                pass
            elif data_words[0] == "leave":
                pass
            elif data_words[0] == "list-all":
                pass
            elif data_words[0] == "game-request":
                pass
            elif data_words[0] == "notify-game-address":
                pass
            response = "Message received successfully"
            client_socket.send(response.encode('utf-8'))

    def listPlayers(self):
        pass

    def game_request(self):
        pass

    def update_status(self):
        pass

# process player requests:
#   join
#   leave
#   list-all
#   game-request