import random
import threading
from socket import *
from constants import *
from concurrent.futures import ThreadPoolExecutor

class ServerApp:
    def __init__(self):
        self.client_connections = []
        self.players = {}   # map player tags to dictionary containing "status" and "active_connection"
        self.active_connections = {}    # map active connections to player tags
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
                self.active_connections[addr] = ""
                self.client_connections.append(conn)
                # assign handling of client connection to thread pool
                executor.submit(self.__client_handler, conn)

    # entry point for threaded processing of client requests of the form (request_type, payload)
    def __client_handler(self, client_connection):
        while True:
            data = client_connection.recv(1024)
            if not data:
                break
            request_type, payload = data.decode('utf-8')
            if request_type == RequestType.SET_NAME:
                if self.players.get(payload, None):
                    client_connection.send((RequestType.NAME_TAKEN).encode('utf-8'))
                else:
                    self.__set_username(client_connection, payload)
            elif request_type == RequestType.LEAVE_SERVER:
                self.__remove_player(client_connection)
                break
            elif request_type == RequestType.LIST_ALL:
                self.__list_players(client_connection)
            elif request_type == RequestType.GAME_REQUEST:
                self.__game_request(client_connection, payload)
        client_connection.close()

    def __remove_player(self, client_connection):
        player_address = client_connection.getpeername()
        player_tag = self.active_connections.pop(player_address)
        self.players.pop(player_tag)
        self.client_connections.remove(client_connection)
        client_connection.close()

    def __set_username(self, client_connection, username):
        old_username = self.active_connections[client_connection]
        self.active_connections[client_connection] = username
        self.players.pop(old_username)
        self.players[username] = {
            "status" : PlayerStatus.ONLINE,
            "active_connection" : client_connection   
        }

    def __list_players(self, client_connection):
        client_connection.send(self.players.values().encode('utf-8'))

    def __game_request(self, client_connection, payload):
        user_from, user_to = payload
        requested_addr = self.players[user_to]["active_connection"]
        requested_conn = self.client_connections[requested_addr]
        requested_conn.send((RequestType.GAME_REQUEST, (user_from, user_to)).encode('utf-8'))
        response, payload = requested_conn.recv(1024).decode('utf-8')
        if response == RequestType.ACCEPT_GAME:
            listening_addr = payload
            color_user_from = random.choice([PieceColor.WHITE, PieceColor.BLACK])
            color_user_to = PieceColor.BLACK if color_user_from == PieceColor.WHITE else PieceColor.BLACK
            client_connection.send((RequestType.INITIALISE_GAME, (listening_addr, color_user_from)))
            requested_conn.send((RequestType.INITIALISE_GAME, color_user_to))
        elif response == RequestType.REJECT_GAME:
            client_connection.send((RequestType.REJECT_GAME).encode('utf-8'))

    def __close_server(self):
        for conn in self.client_connections:
            conn.close()
        self.socket.close()

ServerApp()

