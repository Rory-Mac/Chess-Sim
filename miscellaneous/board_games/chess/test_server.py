from socket import *
import pickle

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('localhost', 18000))
server_socket.listen()
connection, _ = server_socket.accept()
message = connection.recv(1024)
message = pickle.loads(message)
print(message[2][1])
