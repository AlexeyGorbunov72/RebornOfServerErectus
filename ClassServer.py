import socket
import firebase_admin
import ClassWaitConnection
from firebase_admin import credentials


class Server:
    sock = None
    cred = None
    threadList = []
    def __init__(self, port, ip, threadList_):
        self.threadList = threadList_
        self.sock = socket.socket()
        self.sock.bind((ip, port))
        self.sock.listen(10000)
        socket.setdefaulttimeout(20)
        self.cred = credentials.Certificate("messengererectus-firebase-adminsdk-n5g6n-91f4747547.json")
        firebase_admin.initialize_app(self.cred)
        print("succsesful")
    def startListen(self):
        print("Start listening...")
        server_ = self
        waitConnection = ClassWaitConnection.WaitConnection(server=server_, threadList_=self.threadList)

        waitConnection.waitConnection()
