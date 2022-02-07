#
# WorkingWithClasses.py is a sandbox python script where I am currently experimenting with different concepts relating to classes and inheritance
#
#  Made by Joe "Dynam0_" Griffin
#

#__GLOBALS______________________________________________________
EveryThing = []


#__CLASSES______________________________________________________
class objct():
    def __init__(self,x = int(),y = int(),z = int()):
        if x.isdigit():  #Initializing X
            self.__x = int(x)
        else:
            self.__x = int()
        if y.isdigit(): #Initializing Y
            self.__y = int(y)
        else:
            self.__y = int()
        if z.isdigit(): #Initializing Z
            self.__z = int(z)
        else:
            self.__z = int()
    
    #Setters
    def setx(self,x):
        self.__x = x
    def sety(self,y):
        self.__y = y
    def setz(self,z):
        self.__z = z
    #Getters
    def getx(self):
        return self.__x
    def gety(self):
        return self.__y
    def getz(self):
        return self.__z
    #Checkers
    def checkx(self):
        return str(self.__x).isdigit()
    def checky(self):
        return str(self.__y).isdigit()
    def checkz(self):
        return str(self.__z).isdigit()
    
    def __repr__(self):
        return "obj(" + str(self.__x) + "," + str(self.__y) + "," + str(self.__z) + ")"

class entity(objct):
    def __init__(self,x,y,z,mass = int(),volume = int()):
        super().__init__(x,y,z)
        
        if mass.isdigit():  #Initializing Mass
            self.__mass = mass
        else:
            self.__mass = int()
        
        if volume.isdigit():  #Initializing Volume
            self.__volume = volume
        else:
            self.__volume = int()
    #Setters
    def setMass(self,mass):
        self.__mass = mass
    def setVolume(self,volume):
        self.__volume = volume
    #Getters
    def getMass(self):
        return self.__mass
    def getVolume(self):
        return self.__volume
    
    def checkMass(self):
        return str(self.__mass).isdigit()
    def checkVolume(self):
        return str(self.__volume).isdigit()
    
    
#__EXTRA FUNCTIONS______________________________________________
def ValidLocal(Local):
    temp = Local.split(",")
    if len(temp) == 3:
        pass
    elif len(temp) > 3:
        print("ERROR: Too Many Values Provided")
        return False
    else:
        print("ERROR: Too Few Values Provided")
        return False
    
    for h in temp:
        if h.isdigit():
            h = int(h)
            pass
        else:
            print("ERROR: Invalid Values")
            return False   
    return True

def EntityMenu():
    print("Where is your entity? Please provide three numbers seperated by commas")
    UserLocation = input(":=: ").strip().lower()
    if UserLocation == "q" or UserLocation == "quit":
        return False
    elif ValidLocal(UserLocation):
        temp = UserLocation.split(",")
        x,y,z = temp[0], temp[1], temp[2]
    else:
        return
        
    print("How much does your object weigh? (in kilograms)")
    UserMass = input(":=: ").strip().lower()
    if UserMass.isdigit() and UserMass > 0:
        mass= UserMass
    else:
        print("ERROR: Invalid Mass Value")
        return
    
    print("What is the volume of this object? (in m^3)")
    UserVolume = input(":=: ").strip().lower()
    if UserVolume.isdigit():
        volume = UserVolume
    else:
        print("ERROR: Invalid Volume")
        return
    
    UserEntity = entity(x,y,z,mass,volume)
    EveryThing.append(UserEntity)
    return UserEntity
    
def ObjectMenu():
    print("Where is your object? Please provide three numbers seperated by commas")
    UserLocation = input(":=: ").strip().lower()
    if UserLocation == "q" or UserLocation == "quit":
        return False
    elif ValidLocal(UserLocation):
        temp = UserLocation.split(",")
        x,y,z = temp[0], temp[1], temp[2]
    else:
        return
    
    UserObject = objct(x,y,z):
    EveryThing.append(UserObject)
    return UserObject

    
def DisplayMenu():
    print("Displaying all items")
    for item in EveryThing:
        print(Everything[])
        
def Menu():
    print("_______________________")
    print("[1] Display")
    print("[2] Create")
    print("[3] Remove")

if __name__ == "__main__":
    print("Hello and Welcome to CRE8R")
    while True:
        Menu()
    
    