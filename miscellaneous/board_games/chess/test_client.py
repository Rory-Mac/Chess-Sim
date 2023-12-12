import random
from socket import *

class TestClient:
    def __init__(self):
        self.socket_to_server = socket(AF_INET, SOCK_STREAM)
        self.socket_to_server.connect(('localhost', 18000))
        self.start_rng()
        self.socket_to_server.close()

    def start_rng(self):
        while True:
            message = input("Enter any key to trigger: ")
            if message == "exit": 
                break
            message = str(random.randint(0,100))
            self.socket_to_server.send(message.encode('utf-8'))

TestClient()