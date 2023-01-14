# Client Side Json
import socket
import json

# Constant
ENCODER = "utf-8"
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
BYTE_SIZE = 1024


# Create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST_IP, HOST_PORT))

# Receive the json object from the server

message_json = client_socket.recv(BYTE_SIZE) # Dont need to decode the bytes received, json loads can do that automatically
message_dict = json.loads(message_json)
print(type(message_json), message_json, type(message_dict), message_dict)
