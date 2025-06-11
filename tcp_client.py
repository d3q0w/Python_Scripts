import socket


target_host = "google.com"
target_port = 80


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client.connect((target_host, target_port))


http_request = (
    "GET / HTTP/1.1\r\n"
    f"Host: {target_host}\r\n"
    "Connection: close\r\n"  
    "\r\n"
)
client.sendall(http_request.encode())  


response = b""
while True:
    chunk = client.recv(4096)
    if not chunk:
        break
    response += chunk


print(response.decode(errors="replace"))  # replace to handle any invalid characters


client.close()
