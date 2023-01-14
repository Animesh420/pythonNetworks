# Pickle Server
import socket
import pickle

# Create a server socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))

# Receive the pickled list from the server
pickled_list = client_socket.recv(1024)
print(pickled_list)
print(type(pickled_list))
print(pickle.loads(pickled_list))
