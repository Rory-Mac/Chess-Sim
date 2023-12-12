from socket import *
import pickle

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('localhost', 18000))
message = ("first_field", 5318008, ("inception", "inception"))
client_socket.send(pickle.dumps(message))