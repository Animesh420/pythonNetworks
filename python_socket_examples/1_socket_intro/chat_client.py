# Chat client side

import socket

# define constants to be used
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = 'utf-8'
BYTE_SIZE = 1024

# Create a server socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))

# Accept any incoming connection and let them know they are connected
print("Client is running ...")
# Send/Receive message
while True:
    # receive the message from server
    message = client_socket.recv(BYTE_SIZE).decode(ENCODER)

    # Quit if the connected server wants to quit else keep receiving messages
    if message.upper() == "QUIT":
        client_socket.send("quit".encode(ENCODER))
        print("\nEnding the chat on client ... good bye.\n")
        break

    else:
        print(f"\n{message}")
        message = input("Message: ")
        client_socket.send(message.encode(ENCODER))

client_socket.close()
