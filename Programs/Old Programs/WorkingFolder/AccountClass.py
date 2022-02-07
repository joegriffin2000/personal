#
# This Document is for housting my account class and a couple useful functions
#
#

def validSTR(s):
    if s == int(s):
        return False
    else:
        s.lower().strip(' ')
        return True
        
    
class Acc():
    def __init__(self,ID,FirstName,LastName,Pred):
        self__ID = ID
        self__FN = FirstName
        self__LN = LastName
        self__Pred = Pred
        
    def getFirstName():
        return self__FN
    def getLastName():
        return self__LN
    def getID():
        return self__ID
    
    def setFirstName(x):
        self__FN = x
    def setLastName(x):
        self__LN = x
    
    def setPred(pred):
        self__Pred = pred
    def setSucc(succ):
        self__Succ = succ


def AdminLogin():
    userName = input("user: ")
    userPass = input("pass: ")
    
    UL=open("userlist", "r")
    
    for lines in UL.readlines():
        if ("%s/%s\n" % (userName,userPass)) == lines:
            return True
        
    return False


