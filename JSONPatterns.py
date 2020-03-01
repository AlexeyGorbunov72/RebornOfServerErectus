from enum import Enum
class JSONPatterns(Enum):
    initialJson = 0
    searchJson = 1
    chatingJson = 2
pattrns = [{"type": 0, "UID": ""},
           {"type": 1,"search" : ""},
           {"type": 2, "chatID": 0, "message": "", "nickname": ""}]

def getSerchJSON():
    return pattrns[JSONPatterns.searchJson.value]

def getInitialJson():
    return pattrns[JSONPatterns.initialJson.value]

def getChatingJson():
    return pattrns[JSONPatterns.chatingJson.value]

