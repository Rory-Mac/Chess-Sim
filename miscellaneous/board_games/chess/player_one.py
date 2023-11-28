from multiprocessing.connection import Listener
from multiprocessing.connection import Client

listener = Listener(('localhost', 6000), authkey=b'our super secret shared key')
channel_one_listener = listener.accept()
while True:
    message = channel_one_listener.recv()
    if message == "exit": break
    print("RECEIVED MESSAGE: ", message)
channel_one_listener.close()
listener.close()

channel_two_client = Client(('localhost', 6001), authkey=b'another super secret shared key')
while True:
    message = input()
    channel_two_client.send(message)
    if message == "exit": break
channel_two_client.close()