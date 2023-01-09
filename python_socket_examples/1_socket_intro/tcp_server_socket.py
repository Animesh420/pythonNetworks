# TCP Server side
import socket

# Create a server side socket using IPV4 (AF_INET) and TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# See how to get IP address dynamically
# print(socket.gethostname())  # hostname
# ip of the given host by name
# print(socket.gethostbyname(socket.gethostname()))

# Bind our new socket to a tuple (IP address, PORT address)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

# Put the socket in listening mode to look for any possible connection
server_socket.listen()

# Listen forever to accept any incoming connection
while True:
    # accept every single connection and store two pieces of information
    client_socket, (client_address, client_port) = server_socket.accept()
    # print(type(client_socket), type(client_address))
    # print(client_socket, client_address)
    print(f"Connected to {client_address} !\n")

    # send a message to the client that just connected
    client_socket.send("You are connected !!".encode("utf-8"))
    server_socket.close()
    break 
