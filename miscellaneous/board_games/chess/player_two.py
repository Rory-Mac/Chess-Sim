from multiprocessing.connection import Client
from multiprocessing.connection import Listener

channel_one_client = Client(('localhost', 6000), authkey=b'our super secret shared key')
while True:
    message = input()
    channel_one_client.send(message)
    if message == "exit": break
channel_one_client.close()

listener = Listener(('localhost', 6001), authkey=b'another super secret shared key')
channel_two_listener = listener.accept()
while True:
    message = channel_two_listener.recv()
    if message == "exit": break
    print("RECEIVED MESSAGE: ", message)
channel_two_listener.close()
listener.close()
