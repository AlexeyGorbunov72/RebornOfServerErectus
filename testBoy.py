import socket

port=1498
ip="192.168.0.14"

sock = socket.socket()

sock.connect((ip, port))

while True:
    sock.send(input(":").encode())