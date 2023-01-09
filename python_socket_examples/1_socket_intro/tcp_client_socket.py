# TCP Client side
import socket

# Create a client side socket using IPV4 (AF_INET) and TCP (SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to a server located at a given IP and PORT
client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))

# Receive a message from the server ..., You must specify the max number of bytes to receive
message = client_socket.recv(10)
print(message.decode('utf-8'))


# # Receive a message from the server ..., You must specify the max number of bytes to receive
message = client_socket.recv(10)
print(message.decode('utf-8'))


# Close the client socket
client_socket.close()
