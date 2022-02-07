class Media():
    def __init__(self,typ='',name='',rating=0):
        self.__type = typ
        self.__name = name
        self.__rating = rating
        
    def getType(self):
        return self.__type
    
    def getName(self):
        return self.__name
    
    def getRating(self):
        return self.__rating
    
    def setType(self,typ):
        self.__type = typ
        
    def setName(self,name):
        self.__name = name
        
    def setRating(self,rating):
        self.__rating = rating
        
    def __str__(self):
        print("Type: "+self.__type)
        print("Name: "+self.__name)
        print("Rating: "+str(self.__rating)+"/10")
        return ("")
    
class Movie(Media):
    def __init__(self,typ="",name="",rating=0,director='',runtime=0):
        super().__init__(typ,name,rating)
        self.__director = director
        self.__runtime = runtime
        
    def getDirector(self):
        return self.__director
    
    def getRuntime(self):
        return self.__runtime
    
    def setDirector(self,director=''):
        self.__director = director
        
    def setRuntime(self,runtime=0):
        self.__runtime  = runtime
        
    def play(self):
        print (super().getName()+", directed by "+self.__director+" is playing now.")
        
    def __str__(self):
        print (super().__str__())
        print ("Director: "+self.__director)
        print ("Runtime: "+ str(self.__runtime))
        return("")

class Song(Media):
    def __init__(self,typ="",name="",rating=0,artist="",album=""):
        super().__init__(typ,name,rating)
        self.__artist = artist
        self.__album = album
        
    def getArtist(self):
        return self.__artist
    
    def getAlbum(self):
        return self.__album
    
    def setArtist(self,artist):
        self.__artist = artist
        
    def setAlbum(self,album):
        self.__album = album
        
    def play(self):
        print (super().getName()+", by "+self.__artist+" is playing now.\n")
        
    def __str__(self):
        print (super().__str__())
        print ("Artist: " + self.__artist)
        print ("Album: " + self.__album)
        return("")

class Picture(Media):
    def __init__(self,typ="",name="",rating=0,resolution=0):
        super().__init__(typ,name,rating)
        if resolution <= 200:
            self.__resolution = 200
        else:
            self.__resolution = resolution
            
    def getResolution(self):
        return self.__resolution
    
    def setResolution(self,resolution):
        if resolution <= 200:
            self.__resolution = 200
        else:
            self.__resolution = resolution
            
    def show(self):
        print("Showing "+ super().getName())
        
    def __str__(self):
        print (super().__str__())
        print ("Resolution: " + str(self.__resolution))
        return("")
    
if __name__ == "__main__":
    p1 = Picture("Picture","dogimage.jpg",4,500)
    p1.show()
    print(p1)