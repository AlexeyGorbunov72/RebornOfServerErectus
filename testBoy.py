import socket

port=1502
ip="172.32.5.100"

sock = socket.socket()

sock.connect((ip, port))

while True:
    sock.send(input(":").encode())