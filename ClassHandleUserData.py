from ClassUser import UserErectus
import ClassWorkerWithUserData
class HandleUserData():
    threadList = []
    def __init__(self, threadList_):
        self.threadList = threadList_


    def handleData(self, userErectus_):
        distributer = ClassWorkerWithUserData.Distributor(threadList_=self.threadList)
        print(userErectus_.userUID)
        print("in handleData: ", self.threadList)
        while True:
            message = userErectus_.reciveByUser()
            if not message:
                exit(f"Fucken shit ({userErectus_.userUID} disconnected) ")
            print(message)
            distributer.ditribute(message=message)

