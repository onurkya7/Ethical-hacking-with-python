import socket

server_ip = input("Enter the Server IP Address:")
server_port = int(input("Enter Server port:"))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))
print("Server Connected!")

message = input("Enter the message here...")
client_socket.sendall(message.encode())
client_socket.close()
