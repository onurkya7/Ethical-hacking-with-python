import socket

def create_covert_channel(target_host, target_port):
    try:
        covert_channel_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        covert_channel_socket.connect((target_host, target_port))
        covert_channel_socket.send(b"Covert Channel Test")
        response = covert_channel_socket.recv(1024)
        print(f"Response from the server: {response.decode()}")
    except Exception as e:
        print(f"Error: {e}")

target_host = "example.com"
target_port = 12345
create_covert_channel(target_host, target_port)
