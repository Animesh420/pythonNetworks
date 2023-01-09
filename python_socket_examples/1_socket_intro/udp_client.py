# UDP client side
import socket

# Create a UDP IPV4 socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send some information via a connection less protocol
client_socket.sendto("Hello UDP server, how are you?".encode(
    'utf-8'), (socket.gethostbyname(socket.gethostname()), 12345))
