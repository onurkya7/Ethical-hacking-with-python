import socket

server_ip = input("Enter the Server IP Address: ")
server_port = int(input("Enter Server port:"))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)

print("Server Started Listening!!!!")
connection, address = server_socket.accept()
print("Address of the Client:", address)

while True:
    output = connection.recv(1024)
    if not output:
        break
    connection.sendall(b'Message Received...\n')

print(output.decode('utf-8'))
connection.close()
