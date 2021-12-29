class Maze:
    #Inputs: Pointer to start room and exit room
    def __init__(self,st=None,ex=None):
        self.__start_room = st
        self.__exit_room = ex
        self.__current = st
        
    def getCurrent(self):
        return self.__current
    
    def moveNorth(self):
        current = self.__current
        north = current.getNorth()
        if north != None:
            self.__current = current.getNorth()
        else:
            return False
        
    def moveSouth(self):
        current = self.__current
        south = current.getSouth()
        if south != None:
            self.__current = current.getSouth()
        else:
            return False
        
    def moveEast(self):
        current = self.__current
        east = current.getEast()
        if east != None:
            self.__current = current.getEast()
        else:
            return False
        
    def moveWest(self):
        current = self.__current
        west = current.getWest()
        if west != None:
            self.__current = current.getWest()
        else:
            return False
        
    def atExit(self):
        if self.__current == self.__exit_room:
            return True
        else:
            return False
        
    def reset(self):
        self.__current = self.__start_room