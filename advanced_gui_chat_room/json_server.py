# Server side json
import socket
import json

# Constant
ENCODER = "utf-8"
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345

# Create a message dict to represent a message
message_packet = {
    "flag": "MESSAGE",
    "name": "MIKE",
    "message": "This is my message coming through",
    "color": "#00ff3f"
}


# Turn the dict into string by json
message_json = json.dumps(message_packet)
print(message_json)
print(type(message_json.encode(ENCODER)))


# Create a server Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

# Listen for all incoming connections

while True:
  client_socket, client_address = server_socket.accept()
  print(f"Connected to {client_address} \n")

  # Send the json object -> which converts data into string and then encodes it
  client_socket.send(message_json.encode(ENCODER))
  server_socket.close()
  break 