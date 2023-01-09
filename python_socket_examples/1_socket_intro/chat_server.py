# Chat server side

import socket

# define constants to be used
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = 'utf-8'
BYTE_SIZE = 1024

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()


# Accept any incoming connection and let them know they are connected
print("Server is running ...")
client_socket, client_address = server_socket.accept()
client_socket.send("You are connected to the server ...\n".encode(ENCODER))

# send/receive message
while True:
    # Receive information from the client
    message = client_socket.recv(BYTE_SIZE).decode(ENCODER)
    # Quit if the client socket wants to quit

    if message.upper() == "QUIT":
        client_socket.send("quit".encode(ENCODER))
        print("\nEnding the chat on server.... good bye.\n")
        break
    else:
        print(f"\n{message}")
        message = input("Message: ")
        client_socket.send(message.encode(ENCODER))

server_socket.close()
