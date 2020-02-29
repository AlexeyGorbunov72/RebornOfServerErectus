import sqlite3
import ClassUser
from threading import Thread
import requests
import ClassHandleUserData
class IndetifireUser:
    db = sqlite3.connect("ErectusDB.db")
    cur = db.cursor()
    def transfer(self, connection):
        global threadsList

        UID = connection[0].recv(100).decode()
        print(UID)
        if UID:
            user = ClassUser.UserErectus(connection, UID, None)
            self.kostul(user)

        else:
            exit(228)
        # # # # # # # # # # COMMING SOON # # # # # # #
        self.cur.execute(f"SELECT token FROM Users WHERE userUID = '{UID}'")
        data = self.cur.fetchall()

        if data:
            user.tokenFireBase = data[0][0]
            self.pushToHandler(self, user)
        else:
            self.exceptionNonToken(user)

    def pushToHandler(self, user):
        global threadList
        threadList.append([Thread(target=ClassHandleUserData.HandleUserData(), args=(user, )), user])
        threadList[-1][0].start()

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

        threadsList.append([Thread(target=ClassHandleUserData.HandleUserData(), args=(user,)), user])
        threadsList[-1][0].start()

    def kostul(self, user):
        threadsList.append([Thread(target=ClassHandleUserData.HandleUserData(), args=(user,)), user])
        threadsList[-1][0].start()
