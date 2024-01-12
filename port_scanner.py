import socket
import threading

target_host = "example.com"
start_port = 1
end_port = 1024

# Create a dictionary to store open ports and their names
open_ports = {}

# Port scanning function
def scan_port(port):
    try:
        # Create a socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout of 1 second for the connection attempt
        socket.setdefaulttimeout(1)
        # Attempt to connect to the port
        result = sock.connect_ex((target_host, port))
        # If the port is open, get the service name and add it to the dictionary
        if result == 0:
            service_name = socket.getservbyport(port)
            open_ports[port] = service_name
        # Close the socket
        sock.close()
    except Exception as e:
        pass

# Use multiple threads to initiate scanning processes
threads = []
for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Print the open ports and their names
for port, service_name in open_ports.items():
    print(f"Port {port} ({service_name}) is open.")
