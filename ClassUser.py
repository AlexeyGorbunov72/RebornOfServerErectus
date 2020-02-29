class UserErectus:
    connection = None
    userUID = None
    tokenFireBase = None
    def __init__(self, connection_, userUID_, token_):
        self.connection = connection_
        self.userUID = userUID_
        self.tokenFireBase = token_
    def sendUserToUser(self):
        pass

    def reciveByUser(self):

        return self.connection.recv(1024).decode()
