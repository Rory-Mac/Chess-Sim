import random
import threading
from socket import *
from constants import *
from concurrent.futures import ThreadPoolExecutor

class ServerApp:
    def __init__(self):
        self.client_connections = []
        # player-address key-value pair in online_players is address-player key-value pair in online_player_addresses 
        self.online_players = {}
        self.online_player_addresses = {}
        # player-address key-value pair in ingame_players is address-player key-value pair in ingame_player_addresses
        self.ingame_players = {}
        self.ingame_player_addresses = {}
        # threaded listener listens for inbound connections, main thread enters administrative CLI
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind(PLAYER_DIRECTORY_ADDR)
        server_listener = threading.Thread(target=self.__start_server, args=())
        server_listener.daemon = True
        server_listener.start()
        self.__CLI()

    def __CLI(self):
        while True:
            cmd = input("Enter Command: ")
            if cmd == "exit":
                self.__close_server()
                break

    def __start_server(self):
        self.socket.listen()
        with ThreadPoolExecutor(max_workers=48) as executor:
            while True:
                conn, addr = self.socket.accept()
                # process/store client connection
                self.online_player_addresses[addr] = "unknown"
                self.client_connections[addr] = conn
                self.client_connections.append(conn)
                print(f"Connection accepted from {addr}")
                # assign handling of client connection to thread pool
                executor.submit(self.__client_handler, conn)

    # entry point for threaded processing of client requests
    def __client_handler(self, client_connection):
        while True:
            data = client_connection.recv(1024)
            if not data:
                break
            data = data.decode('utf-8')
            data_words = data.split()
            print(f"Received data from {client_connection.getpeername()}: {data}")
            if data_words[0] == "set-username":
                self.__set_username(client_connection, data_words[1])
            elif data_words[0] == "leave":
                self.__remove_player(client_connection)
                break
            elif data_words[0] == "list-all":
                self.__list_players(client_connection)
            elif data_words[0] == "game-request":
                self.__game_request(client_connection, data_words[1])
            response = "Message received successfully"
            client_connection.send(response.encode('utf-8'))
        client_connection.close()

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

    def __game_request(self, user_connection, opponent_username):
        opponent_address = self.online_players[opponent_username]
        opponent_connection = self.client_connections[opponent_address]
        message = f"incoming-request {self.online_player_addresses[user_connection]}"
        opponent_connection.send(message.encode('utf-8'))
        message = opponent_connection.recv(1024).decode('utf-8')
        if message == "accept":
            user_listening_addr = opponent_connection.recv(1024).decode('utf-8')
            user_color = random.choice(["white", "black"])
            opponent_color = "black" if user_color == "white" else "white"
            message = f"accepted {user_listening_addr} {user_color}"
            user_connection.send(message.encode('utf-8'))
            message = f"{opponent_color}"
            opponent_connection.send(message.encode('utf-8'))
        elif message == "deny":
            message = f"denied"
            user_connection.send(message.encode('utf-8'))

    def __close_server(self):
        for conn in self.client_connections:
            conn.close()
        self.socket.close()

ServerApp()

