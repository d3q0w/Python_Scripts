import socket
from IPy import IP
def check_ip(ip):
    try:
        IP(ip)
        return (ip)
    except ValueError:
        return socket.gethostbyname(ip)

def scan_port(ipaddress,port):
    try:
        sock = socket.socket()
        sock.settimeout(0.6)
        sock.connect(ipaddress, port)
        print("Port" +str(port)+ " is open!")
    except:
        print("[-] Port" + str(port)+ " is closed! ")


ipaddress = input("[+] Enter target to scan: ")
converted_ip=check_ip(ipaddress)
for port in range(1,20):
    scan_port(converted_ip, port)

