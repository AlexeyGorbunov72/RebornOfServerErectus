import sqlite3
import ClassUser
from threading import Thread
import requests
import ClassHandleUserData
class IndetifireUser:
    db = sqlite3.connect("ErectusDB.db")
    cur = db.cursor()
    threadList = []
    def __init__(self, threadList_):
        self.threadList = threadList_
    def transfer(self, connection):


        UID = connection.recv(100).decode()
        print(UID)
        if UID:
            user = ClassUser.UserErectus(connection, UID, None)
            self.kostul(user)

        else:
            exit(228)
        exit("STOP! ITS DONT END")
        # # # # # # # # # # COMMING SOON # # # # # # #
        data = []
        with sqlite3.connect("ErectusDB.db") as cur:
            cur.execute(f"SELECT token FROM Users WHERE userUID = '{UID}'")
            data = cur.fetchall()

        if data:
            user.tokenFireBase = data[0][0]
            self.pushToHandler(self, user)
        else:
            self.exceptionNonToken(user)

    def pushToHandler(self, user):

        self.threadList.append([Thread(target=ClassHandleUserData.HandleUserData(threadList_=self.threadList), args=(user, )), user])
        self.threadList[-1][0].start()

    def exceptionNonToken(self, user):

        r = requests.get(r'https://erectus-63adc.firebaseio.com/Users.json?print=pretty')
        responseFromFirebase = r.json()
        try:
            token = responseFromFirebase[user.userUID]['token']
            print("TOKEN: ", token)
        except:
            print(f"Fucken retard try to fuck me!")
            exit(f"<sys>This UID None: {user.userUID} ")


        self.cur.execute(f"INSERT INTO Users VALUES ('{user.userUID}' , '{token}')")
        self.db.commit()

        self.threadList.append([Thread(target=ClassHandleUserData.HandleUserData(threadList_=self.threadList), args=(user,)), user])
        self.threadList[-1][0].start()

    def kostul(self, user):
        print("in kostul: ", self.threadList)
        classJopa_Penis228 = ClassHandleUserData.HandleUserData(threadList_=self.threadList)
        self.threadList.append([Thread(target=classJopa_Penis228.handleData, args=(user,)), user])
        self.threadList[-1][0].start()
        print("END OF TRANSFER")
