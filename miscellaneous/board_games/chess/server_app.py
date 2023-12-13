import random
import pickle
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
            if cmd == "help":
                print("\thelp : list valid commands")
                print("\texit : close and exit server")
            elif cmd == "exit":
                self.__close_server()
                break
            else:
                print("Unknown Command, type 'help' for list of commands.")

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
            request_type, payload = pickle.loads(data)
            if request_type == RequestType.SET_NAME:
                if self.players.get(payload, None):
                    client_connection.send(pickle.dumps((RequestType.FAILURE, None)))
                else:
                    self.__set_username(client_connection, payload)
            elif request_type == RequestType.LEAVE_SERVER:
                self.__remove_player(client_connection)
                break
            elif request_type == RequestType.LIST_ALL:
                client_connection.send(pickle.dumps(self.players.values()))
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

    def __game_request(self, client_connection, payload):
        user_from, user_to = payload
        requested_addr = self.players[user_to]["active_connection"]
        requested_conn = self.client_connections[requested_addr]
        requested_conn.send(pickle.dumps((RequestType.GAME_REQUEST, (user_from, user_to))))
        response = requested_conn.recv(1024)
        request_type, payload = pickle.loads(response)
        if request_type == RequestType.ACCEPT_GAME:
            listening_addr = payload
            color_user_from = random.choice([PieceColor.WHITE, PieceColor.BLACK])
            color_user_to = PieceColor.BLACK if color_user_from == PieceColor.WHITE else PieceColor.BLACK
            client_connection.send(pickle.dumps((RequestType.INITIALISE_GAME, (listening_addr, color_user_from))))
            requested_conn.send(pickle.dumps((RequestType.INITIALISE_GAME, (listening_addr, color_user_to))))
        elif request_type == RequestType.REJECT_GAME:
            client_connection.send(pickle.dumps((RequestType.REJECT_GAME, None)))

    def __close_server(self):
        for conn in self.client_connections:
            conn.close()
        self.socket.close()

ServerApp()

