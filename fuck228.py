import ClassServer
from threading import Thread
import time

def cheker():
    global threadList
    while True:
        try:
            if input() == "s":
                for (thread, user) in threadList:
                    print("user: ", user.userUID)
        except:
            pass
threadList = []
a = ClassServer.Server(port=1503, ip="192.168.0.14", threadList_=threadList)
t = Thread(target=cheker)
t.start()
a.startListen()
