#
# untitled 0 - working on creating different data structures for cs260
#
#

class pNode():
    def __init__(self,v,n):
        self.__value = v
        self.__next = n
        
    def getNext(self):
        return self.__next
    def getValue(self):
        return self.__value
    
    def setNext(self,x):
        self.__next = x
    def setValue(self,x):
        self.__value = x
        
    def __repr__(self):
        return self.__value
    
class List():
    def __init__(self,first):
        self.__first = first
        self.__current = first
        
    def getFirst(self):
        return self.__first
    def getCurrent(self):
        return self.__current
    
    def setFirst(self,x):
        self.__first = x
    def setCurrent(self,x):
        self.__current = x
        
    def __repr__(self):
        string = "["
        while self.__current.getNext() != None:
            string += self.__current + ", "
            self.__current = self.__current.getNext()
            
        return string + self.__current + "]"
        