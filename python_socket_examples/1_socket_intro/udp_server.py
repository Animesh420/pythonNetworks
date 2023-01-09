# UDP server side
import socket

# Create a server side socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the new socket to a tuple (IP Address, Port address)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

# we are not listening/ accepting connections since UDP is a conectionless protocol, directly receiving message
message, address = server_socket.recvfrom(5)
print(message.decode('utf-8'))
print(address)


# we are not listening/ accepting connections since UDP is a conectionless protocol, directly receiving message
message, address = server_socket.recvfrom(5)
print(message.decode('utf-8'))
print(address)
