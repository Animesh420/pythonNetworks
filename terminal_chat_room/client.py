# Client side chat room

import socket
import threading

# define constants to be used
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = 'utf-8'
BYTE_SIZE = 1024


# Create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))


def send_message():
    '''
    Send a message to the server to be broadcast
    '''
    while True:
      msg = input("")
      client_socket.send(msg.encode(ENCODER))


def receive_message():
    '''
    Receive a message from the server
    '''

    while True:

        try:
            # Receive an incoming message from the server
            msg = client_socket.recv(BYTE_SIZE).decode(ENCODER)

            # check for the name flag
            if msg.upper() == "NAME":
                name = input("What is your name: ")
                client_socket.send(name.encode(ENCODER))
            else:
              print(msg)
        except:
            print("An error occurred")
            client_socket.close()
            break

# Create threads to continuosly send and receive message

receive_thread = threading.Thread(target=receive_message)
send_thread = threading.Thread(target=send_message)

receive_thread.start()
send_thread.start()