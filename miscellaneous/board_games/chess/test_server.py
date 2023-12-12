from socket import *
import threading
from concurrent.futures import ThreadPoolExecutor

class TestServer:
    def __init__(self):
        self.connections = []
        self.numbers = []
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind(('localhost', 18000))
        server_thread = threading.Thread(target=self.__start_server, args=())
        server_thread.daemon = True
        server_thread.start()
        self.CLI()

    def __client_handler(self, client_socket):
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            self.numbers.append(data)
        client_socket.close()

    def __start_server(self):
        self.socket.listen()
        with ThreadPoolExecutor(max_workers=48) as executor:
            while True:
                client_socket, _ = self.socket.accept()
                self.connections.append(client_socket)
                executor.submit(self.__client_handler, client_socket)

    def CLI(self):
        while True:
            cmd = input("Enter Command: ")
            if cmd == "print":
                print(self.numbers)
            elif cmd == "exit":
                self.close_server()
                break

    def close_server(self):
        for socket in self.connections:
            socket.close()
        self.socket.close()

TestServer()

# test with multiple listeners