from socket import *
from constants import *
from threading import Thread

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
        self.server_socket.send(message.encode('utf-8'))
        response = self.server_socket.recv(PACKET_MAX_SIZE)
        if response == "success":
            opponent_address = self.server_socket.recv(PACKET_MAX_SIZE)
            self.__connect_to_opponent(opponent_address)
            return True
        elif response == "failure":
            return False

    def __connect_to_opponent(self, opponent_addr):    
        self.opponent_socket.connect(opponent_addr)
        print(f"Connection made and game started with {self.opponent_socket.getpeername()}")

    def listen_for_opponent(self):
        print("listening for opponent...")
        self.opponent_socket.bind(('localhost', 0))
        self.opponent_socket.listen()
        # notify player directory of listening port
        message = f"notify-game-address {self.opponent_socket.getsockname()}"
        self.server_socket.send(message.encode('utf-8'))
        # accept inbound connection to start game
        connection, address = self.opponent_socket.accept()
        self.opponent_connection = connection
        print(f"Connection accepted from opponent {address}")

    def make_move(self, move):
        if self.opponent_connection:
            self.opponent_connection.send(move.encode('utf-8'))
        else:
            self.opponent_socket.send(move.encode('utf-8'))
        self.moves.append(move)

    def get_opponent_move(self):
        if self.connection:
            move = self.opponent_connection.recv(PACKET_MAX_SIZE)
        else:
            move = self.opponent_socket.recv(PACKET_MAX_SIZE)
        self.moves.append(move)

    # main player to player directory interface
    def enter_CLI(self):
        while True:
            cmd = input("Input command: ")
            cmd_words = cmd.split()
            if cmd_words[0] == "help":
                print("\thelp : list all commands")
                print("\tlist : list all available players")
                print("\trequest [player] : request game with player")
                print("\texit : exit command-line interface")
            elif cmd_words[0] == "list":
                self.list_players()
            elif cmd_words[0] == "request":
                if self.game_request(cmd_words[1]): 
                    print("Request Accepted.")
                    return True
                else:
                    print("Request Denied.")
            elif cmd == "exit":
                self.leave_player_directory()
                return False
            else:
                print("Command not found. Type 'help' for list of commands.")

    def start(self):
        self.set_user_handle(input("Enter username: "))
        self.join_player_directory()
        # listen for server interrupts
        server_thread = Thread(target=self.__server_handler, args=())
        server_thread.start()

    def __server_handler(self):
        while True:
            data = self.server_socket.recv(1024)
            data_words = data.split()
            if data_words[0] == "listen":
                self.listen_for_opponent()


# start player runtime,
# enter CLI, when game request accepted,
# enter game context, when game ends,
# enter CLI context


# player is created, user name set, joins player directory, server handler starts, CLI starts
# when in game, neither threads are necessary
# after game, threads should resume