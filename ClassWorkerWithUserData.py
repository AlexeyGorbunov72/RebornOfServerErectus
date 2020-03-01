import json
import sqlite3
import time


class SupporterForCompliter:
    threadList = []

    def __init__(self, threadList_):
        self.threadList = threadList_

    def findUserConnectionByUID(self, userUID):
        print(self.threadList)
        for (thread, user) in self.threadList:
            if thread.isAlive():
                print(user.userUID, userUID)
                if int(user.userUID) == int(userUID):
                    return user

    def prepareForCreateChat(self, message):
        jsonMessage = json.loads(message)
        print(jsonMessage)
        reciverUID = jsonMessage["reciverUID"]
        senderUID = jsonMessage["senderUID"]
        with sqlite3.connect("ErectusDB.db") as db:
            cur = db.cursor()
            cur.execute(f"""SELECT chatID FROM Chats WHERE userUID = '{reciverUID}'""")
            chatsReciver = cur.fetchall()
            cur.execute(f"""SELECT chatID FROM Chats WHERE userUID = '{senderUID}'""")
            chatsSender = cur.fetchall()
            print(chatsSender, '\n', chatsReciver)
            chatsUnion = [chatId[0] for chatId in list(set(chatsReciver) & set(chatsSender))]
            unionChat = self.findUserToUserChat(chatsUnion)
            if unionChat is None:
                newRegisteredChatId = self.createChat()
                cur.execute(f"""INSERT INTO Chats VALUES ('{senderUID}', {newRegisteredChatId}), 
                                                        ('{reciverUID}', {newRegisteredChatId})""")
                db.commit()
            else:
                print(unionChat)
                return unionChat

    def createChat(self):
        with sqlite3.connect("ErectusDB.db") as db:
            cur = db.cursor()
            timeOfCreation = time.time()
            cur.execute(f"""INSERT INTO ChatInfo VALUES (NULL, {timeOfCreation})""")
            db.commit()
            cur.execute(f"""SELECT chatID FROM ChatInfo WHERE timeOfCreation = {timeOfCreation}""")
            return cur.fetchall()[0][0]

    def createConversation(self, message):
        jsonMessage = json.loads(message)

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
                    if userUID != jsonMessage["senderUID"]:
                        user = self.findUserConnectionByUID(userUID=userUID)
                        if user:
                            print("i got user: ", user.userUID)
                            user.sendMessage(message)

    def findUserToUserChat(self, arrayOfChats):
        print(arrayOfChats)
        with sqlite3.connect("ErectusDB.db") as db:
            cur = db.cursor()
            for chatId in arrayOfChats:
                cur.execute(f"""SELECT userUID FROM Chats WHERE chatID =' {chatId}'""")
                data = cur.fetchall()
                if len(data) == 2:
                    return chatId
        return None


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
            self.supporter.prepareForCreateChat(message)

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

