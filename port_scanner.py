import socket
import sys

host = "google.com"
port = 80
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
code = client.connect_ex((host, port))
if code == 0:
    print("[+] {} open".format(port))