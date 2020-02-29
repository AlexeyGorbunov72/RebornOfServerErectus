from ClassUser import UserErectus
class HandleUserData():
    def handleData(self, userErectus_):
        print(userErectus_.userUID)
        while True:
            message = userErectus_.reciveByUser()
            if message: print(message)

