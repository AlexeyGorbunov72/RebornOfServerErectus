import json
import sqlite3

class SupporterForCompliter:
    threadList = []

    def __init__(self, threadList_):
        self.threadList = threadList_

    def findUserConnectionByUID(self, userUID):
        print(self.threadList)
        for (thread, user) in self.threadList:
            if not thread.isAlive():
                continue
            print(user.userUID, userUID)
            if int(user.userUID) == int(userUID):
                return user

    def createChat(self, message):
        jsonMessage = json.loads(message)
        pass

    def sendMessageChating(self, message):
        jsonMessage = json.loads(message)
        print("I want to send some messenge: ", message)
        with sqlite3.connect("ErectusDB.db") as db:
            cur = db.cursor()
            cur.execute(f"""SELECT userUID FROM Chats WHERE chatID = {jsonMessage["chatID"]}""")
            data = cur.fetchall()
            if data:
                print("i got data: ", data)
                for userUID in data:
                    userUID = userUID[0]
                    user = self.findUserConnectionByUID(userUID=userUID)
                    if user:
                        print("i got user: ", user.userUID)
                        user.sendMessage(message)


class CompliterRequests:

    threadList = []
    supporter = 0
    def __init__(self, threadList_):
        self.threadList = threadList_
        self.supporter = SupporterForCompliter(threadList_=threadList_)

    def initialJson(self, message):
        jsonMessage = json.loads(message)
        return jsonMessage["UID"]

    def searchJson(self, message):
        jsonMessage = json.loads(message)

    def chatingMessage(self, message):
        print("in compliter: ", self.threadList)
        jsonMessage = json.loads(message)
        print("chatMessage i got some: ", message)
        if not jsonMessage["chatID"]:
            self.supporter.createChat()

        else:
            self.supporter.sendMessageChating(message)

class Distributor:
    threadList = []
    compliter = 0
    def __init__(self, threadList_):
        self.threadList = threadList_
        self.compliter = CompliterRequests(threadList_)

    def ditribute(self, message):
        print("in distribute: ", self.threadList)
        jsonMessage = json.loads(message)
        if jsonMessage["type"] == 0:  # init json
            pass

        if jsonMessage["type"] == 1:  # search json
            pass

        if jsonMessage["type"] == 2:  # chating json, create chat json
            self.compliter.chatingMessage(message)


