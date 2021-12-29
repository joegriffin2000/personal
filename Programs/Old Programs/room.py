class Room:
    #Constructor sets the description
    #All four doors should be set to None to start
    def __init__(self,descr):
        self.__descr = descr
        self.__north = None
        self.__south = None
        self.__east = None
        self.__west = None
        
    #Accessors
    def __str__(self):
        return self.__descr
    def getNorth(self):
        return self.__north
    def getSouth(self):
        return self.__south
    def getEast(self):
        return self.__east
    def getWest(self):
        return self.__west
    
    #Mutators
    def setDescription(self,d):
        self.__descr = d
    def setNorth(self,n):
        self.__north = n 
    def setSouth(self,s):
        self.__south = s
    def setEast(self,e):
        self.__east = e
    def setWest(self,w):
        self.__west = w