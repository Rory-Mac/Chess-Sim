import random
import pickle
import threading
import datetime
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
        # no admin-interaction required, server spun-down with "exit" signal 
        while True:
            if input() == "exit":
                self.__close_server()
                break

    def __start_server(self):
        self.socket.listen()
        with ThreadPoolExecutor(max_workers=48) as executor:
            while True:
                conn, addr = self.socket.accept()
                self.active_connections[addr] = ""
                self.client_connections.append(conn)
                self.__log_server_event(RequestType.JOIN_SERVER, addr)
                # assign handling of client connection to thread pool
                executor.submit(self.__client_handler, conn)

    def __log_server_event(self, request_type : RequestType, event_from=None, event_to=None):
        col1 = f"[{datetime.datetime.now()}] [{request_type.name}]"
        col2 = None
        col3 = None
        if event_from:
            sending_player_tag = self.active_connections[event_from] if self.active_connections[event_from] != "" else "?"
            col2 = f" {sending_player_tag}@{event_from}"
        if event_to:
            col3 = f"{self.active_connections[event_to]}@{event_to}"
        if col1:
            output = col1
        if col2:
            output = "{:<50} {:<20}".format(col1, col2)
        if col3:
            output = "{:<50} {:<20} {:^6} {:<20}".format(col1, col2, "->", col3)
        print(output)

    # entry point for threaded processing of client requests of the form (request_type, payload)
    def __client_handler(self, client_connection):
        while True:
            data = client_connection.recv(1024)
            if not data:
                break
            request_type, payload = pickle.loads(data)
            if request_type == RequestType.SET_NAME:
                self.__log_server_event(request_type, client_connection.getpeername())
                if self.players.get(payload, None):
                    client_connection.send(pickle.dumps((RequestType.FAILURE, None)))
                    self.__log_server_event(RequestType.FAILURE, client_connection.getpeername())
                else:
                    self.__set_username(client_connection, payload)
                    client_connection.send(pickle.dumps((RequestType.SUCCESS, None)))
                    self.__log_server_event(RequestType.SUCCESS, client_connection.getpeername())
            elif request_type == RequestType.LEAVE_SERVER:
                self.__remove_player(client_connection)
                self.__log_server_event(request_type, client_connection.getpeername())
                break
            elif request_type == RequestType.LIST_ALL:
                message = (RequestType.LIST_ALL, list(self.players.keys()))
                client_connection.send(pickle.dumps(message))
                self.__log_server_event(request_type, client_connection.getpeername())
            elif request_type == RequestType.GAME_REQUEST:
                self.__game_request(client_connection, payload)
            elif request_type == RequestType.ACCEPT_GAME:
                user_from, listening_addr = payload
                color_user_from = random.choice([PieceColor.LIGHT, PieceColor.DARK])
                color_user_to = PieceColor.DARK if color_user_from == PieceColor.LIGHT else PieceColor.LIGHT
                requesting_connection = self.players[user_from]["active_connection"]
                requesting_connection.send(pickle.dumps((RequestType.INITIALISE_REQUESTING, (listening_addr, color_user_from))))
                client_connection.send(pickle.dumps((RequestType.INITIALISE_REQUESTED, color_user_to)))
                self.__log_server_event(request_type, client_connection.getpeername(), requesting_connection.getpeername())
            elif request_type == RequestType.REJECT_GAME:
                user_from, _ = payload
                requesting_connection = self.players[user_from]["active_connection"]
                requesting_connection.send(pickle.dumps((RequestType.REJECT_GAME, payload)))
                self.__log_server_event(request_type, client_connection.getpeername(), requesting_connection.getpeername())
        client_connection.close()

    def __remove_player(self, client_connection):
        player_address = client_connection.getpeername()
        player_tag = self.active_connections.pop(player_address)
        self.players.pop(player_tag)
        self.client_connections.remove(client_connection)
        client_connection.close()

    def __set_username(self, client_connection, username):
        client_addr = client_connection.getpeername()
        old_username = self.active_connections[client_addr]
        self.active_connections[client_addr] = username
        if self.players.get(old_username, None):
            self.players.pop(old_username)
        self.players[username] = {
            "status" : PlayerStatus.ONLINE,
            "active_address" : client_addr,
            "active_connection" : client_connection
        }

    def __game_request(self, client_connection, payload):
        user_from, user_to = payload
        requested_conn = self.players[user_to]["active_connection"]
        requested_conn.send(pickle.dumps((RequestType.GAME_REQUEST, (user_from, user_to))))
        self.__log_server_event(RequestType.GAME_REQUEST, client_connection.getpeername(), requested_conn.getpeername())

    def __close_server(self):
        for conn in self.client_connections:
            conn.close()
        self.socket.close()

ServerApp()
