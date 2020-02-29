import ClassServer
import classIndetifireUser
from threading import Thread
class WaitConnection():
    server_ = None
    threadList = []
    def __init__(self, server, threadList_):
        self.server_ = server
        self.threadList = threadList_
    def waitConnection(self):
        while True:
            conn, ipAdres = self.server_.sock.accept()
            conn.settimeout(1000)
            indentifer = classIndetifireUser.IndetifireUser(self.threadList)
            thread = Thread(target=indentifer.transfer, args=(conn, ))
            thread.start()