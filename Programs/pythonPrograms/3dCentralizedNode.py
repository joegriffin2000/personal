#
#
#

class rotation(tuple):
    def __init__(self):
        pass

class distance(tuple):
    def __init__(self,length):
        self.__length = length
        
    def __len__(self):
        return self.__length
    
class position(tuple):
    def __init__(self,x,y,z):
        self.__x = x
        self.__y = y
        self.__z = z
        
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def getZ(self):
        return self.__z
    
    def setX(self,x):
        self.__x = x
    def setY(self):
        self.__y = y
    def setZ(self):
        self.__z = z
        
    def resetX(self):
        pass
    
    def __len__(self):
        return 3
    
def isPosition(x):
    if type(x) == position:
        return True
    else:
        return False
    

class Node():
    def __init__(self,pos=(0,0,0)):
        self.__pos = pos
        self.branches = []
    def getBranches(self):
        return self.branches
    def getNumBranches(self):
        return len(self.branches)
    def getPos(self,x = position(0,0,0)):
        if type(x) == tuple():
            return x
            #return self.__pos
        #elif type(x) == str():
            #return str(self.__pos)
        #elif type(x) == list():
            #return list().append(self.__pos)
    #def addBranch(self,name=str(),rot=rotation(),dst=distance()):
        #pickup here
        #pass
    
    # using repr for a report from each node
    def __repr__(self):
        report = "My Position is {0}.\nI have {1} Branches".format(self.__pos,len(self.branches))
        return report


if __name__ == "__main__":
    nd1 = Node((0,1,0))
    nd2 = Node((0,1,0))

    print(nd1.getPos((2,0,0)))
    