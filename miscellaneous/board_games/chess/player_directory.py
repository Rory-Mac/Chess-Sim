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
                self.__remove_player(client_connection)
                return
            elif data_words[0] == "list-all":
                self.__list_players(client_connection)
            elif data_words[0] == "game-request":
                pass
            elif data_words[0] == "notify-game-address":
                pass
            response = "Message received successfully"
            client_connection.send(response.encode('utf-8'))

    def __remove_player(self, client_connection):
        player_address = client_connection.getpeername()
        player_username = self.online_player_addresses.pop(player_address)
        self.online_players.pop(player_username)

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

    def __game_request(self, username):
        pass

#   game-request/notify-game-address
#   current connection P1 makes game request to P2
#   find address mapped to P2 username
#   ask if P2 wants to accept request
#   P2 responds, if response rejected, notify P1, continue
#   if response accepted, P2 listens for opponent and notifies server of address
#   server notifies P1 of address which then connects to P2
#   game ends, P1/P2 send game over packet to server
#   server moves players from in-game status to online status