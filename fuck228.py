import ClassServer
from threading import Thread
import time
def cheker():
    global threadList
    while True:
        time.sleep(10)
        print(f"threads: {threadList}")
threadList = []
a = ClassServer.Server(port=1498, ip="192.168.0.14", threadList_=threadList)
t = Thread(target=cheker)
t.start()
a.startListen()
