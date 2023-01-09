# Server side program

import socket
import threading
# define constants to be used
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = 'utf-8'
BYTE_SIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

# Create two blank lists to store connected client sockets adn their names
client_socket_list = []
client_name_list = []


def broadcast_message(message):
    '''
    Send a message to ALL clients connected to the server
    '''
    for client_socket in client_socket_list:
      client_socket.send(message)


def receive_message(client_socket):
    '''
    Receive an incoming message from a specific client and forward the messsage to be broadcasted 
    '''
    while True:
        try:
            # Get the name of the given client
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]

            # Receive message
            msg = client_socket.recv(BYTE_SIZE).decode(ENCODER)
            msg = f"{name}: {msg}".encode(ENCODER)
            broadcast_message(msg)
        except:
          # find the index of the client socket in our list
          index = client_socket_list.index(client_socket)
          name = client_name_list[index]

          # Remove the client and name from the list 
          client_socket_list.remove(client_socket)
          client_name_list.remove(name)

          client_socket.close()

          # broadcast to all clients
          broadcast_message(f"{name} has left the chat".encode(ENCODER))
          break 


def connect_client():
    '''
    Connect an incoming client to the server
    '''
    while True:
        # Accept any incoming client connect
        client_socket, client_address = server_socket.accept()
        print(f"Connected with {client_address} ...")

        # send a NAME flag to prompt the client for their name
        client_socket.send("NAME".encode(ENCODER))
        client_name = client_socket.recv(BYTE_SIZE).decode(ENCODER)

        # Add new client sockt and client name to appropriate lists
        client_socket_list.append(client_socket)
        client_name_list.append(client_name)

        # Update the server individual client and ALL clients
        print(f"Name of new client is {client_name}\n")  # server
        client_socket.send(f"{client_name}, you have connected to the server!\n".encode(
            ENCODER))  # Individual client

        broadcast_message(
            f"{client_name} has joined the chat!\n".encode(ENCODER))

        # Now that a new client has connected, start a thread
        receive_thread = threading.Thread(
            target=receive_message, args=(client_socket,))
        receive_thread.start()


# Start the server
print("Server is listening for incoming connections")
connect_client()
