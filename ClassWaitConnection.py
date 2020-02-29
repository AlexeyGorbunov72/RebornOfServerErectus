import ClassServer
import classIndetifireUser
from threading import Thread
class WaitConnection():
    server_ = None
    def __init__(self, server):
        self.server_ = server
    def waitConnection(self):
        while True:
            conn = self.server_.sock.accept()
            indentifer = classIndetifireUser.IndetifireUser()
            thread = Thread(target=indentifer.transfer, args=(conn, ))
            thread.start()