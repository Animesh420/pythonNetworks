# Pickle Server
import socket, pickle 

# Lets create a regular old list

unpickled_list = ['roti', 'kapda', 'makan']
print(type(unpickled_list))

pickled_list = pickle.dumps(unpickled_list)
print(pickled_list)
print(type(pickled_list))

# Create a server socket 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))
server_socket.listen()


while True:
  client_socket, client_address = server_socket.accept()
  print(f"Connected to {client_address}!\n")

  # Send the encoded pickled list 
  client_socket.send(pickled_list)

  # Close the socket

  server_socket.close()
  break 