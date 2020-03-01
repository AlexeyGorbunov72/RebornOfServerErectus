import socket
import json
from threading import Thread
def reciving(sock):
    while True:
        print(sock.recv(1024).decode())
port=1503
ip="192.168.0.14"

sock = socket.socket()
sock.connect((ip, port))
a = Thread(target=reciving, args=(sock, ))
a.start()
dictPattrn = {"type": 2, "chatID": 228, "message": "hello from dude 1", "nickname": "dude 1"}
sock.send(input("uid: ").encode())
while True:
    dictPattrn["text"] = input(":")
    sock.send(json.dumps(dictPattrn).encode())