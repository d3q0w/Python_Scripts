import socket

target_host = "127.0.0.1"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(2.0)  

client.sendto(b"AAAABBB", (target_host, target_port))

try:
    data, addr = client.recvfrom(4096)
    print("Received:", data.decode())
except socket.timeout:
    print("No response (timeout)")

client.close()
