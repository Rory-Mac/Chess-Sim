import threading
from socket import *
from constants import *

class PlayerDirectory:
    def __init__(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        # player-address key-value pair in online_players is address-player key-value pair in online_player_addresses 
        self.online_players = {}
        self.online_player_addresses = {}
        # player-address key-value pair in ingame_players is address-player key-value pair in ingame_player_addresses
        self.ingame_players = {}
        self.ingame_player_addresses = {}
        # player directory listens for connections on initialisation
        self.__listen()

    def __listen(self):
        self.socket.bind(PLAYER_DIRECTORY_ADDR)
        self.socket.listen()
        while True:
            client_connection, client_address = self.socket.accept()
            print(f"Connection accepted from {client_address}")
            self.online_player_addresses[client_address] = "unknown"
            client_handler = threading.Thread(target=self.__client_handler, args=(client_connection))
            client_handler.start()

    # entry point for threaded processing of all client requests
    def __client_handler(self, client_connection):
        while True:
            data = client_connection.recv(1024)
            if not data: break
            data = data.decode('utf-8')
            data_words = data.split()
            print(f"Received data from {client_connection.getpeername()}: {data}")
            if data_words[0] == "set-username":
                self.__set_username(client_connection, data_words[1])
            elif data_words[0] == "leave":
                pass
            elif data_words[0] == "list-all":
                self.__list_players(client_connection)
            elif data_words[0] == "game-request":
                pass
            elif data_words[0] == "notify-game-address":
                pass
            response = "Message received successfully"
            client_connection.send(response.encode('utf-8'))

    def __set_username(self, client_connection, username):
        if self.online_players.get(username, None):
            response = "Username Taken."
            client_connection.send(response.encode('utf-8'))
            return
        old_username = self.online_player_addresses[client_connection]
        self.online_player_addresses[client_connection] = username
        self.online_players.pop(old_username)
        self.online_players[username] = client_connection

    def __list_players(self, client_connection):
        response = self.online_players.values()
        client_connection.send(response.encode('utf-8'))

    def __game_request(self):
        pass

# process player requests:
#   finish set username and list players
#   leave command
#   game-request

# when a player connects
#   they have an address, they set a username
#   initially online, when they join a game, they are in-game, when the game ends, they are online