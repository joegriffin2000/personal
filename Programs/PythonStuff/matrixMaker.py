#Set Minimum Numbers
xMin = 1
yMin = 1
#Set Maximum Numbers
xMax = 6
yMax = 6

#Fixing Maximums and Making Matrix
def MatrixCreate(xMin,yMin,xMax,yMax):
    xMax+=1
    yMax+=1
    listoflists = []
    for i in range(yMin,yMax):
        temp = []
        for j in range(xMin,xMax):
            temp.append((i,j))
        listoflists.append(temp)
    return listoflists

#Printing Matrix
def printMatrix(LIST):
    for i in LIST:
        print(i)

def validValues(userxmin,userymin,userxmax,userymax):
    if userxmin.isdigit() and userymin.isdigit():
        if userxmax.isdigit() and userymax.isdigit():
            return True
        else:
            return False
    else:
        return False

#Main Menu
def mainMenu():
    print("Please insert the minimum and maximum numbers (Input Q to Cancel)")
    userXMin = input("Minimum X:")
    userYMin = input("Minimum Y:")
    userXMax = input("Maximum X:")
    userYMax = input("Maximum Y:")
    
    if "q" in [userXMin.lower(),userYMin.lower(),userXMax.lower(),userYMax.lower()]:
        print("Quitting...")
    elif validValues(userXMin,userYMin,userXMax,userYMax):
        userMatrix = MatrixCreate(int(userXMin),int(userYMin),int(userXMax),int(userYMax))
        printMatrix(userMatrix)
    else:
        print("Error: One or more of the value was not a valid integer")

if __name__ == "__main__":
    mainMenu()