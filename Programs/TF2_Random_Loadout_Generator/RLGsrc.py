# Random Loadout Generator - Allows the user to select a TF2 Class and then the program provides the user with a random TF2 Loadout
# by Joe "DynaJoe" Griffin
# 

#imports
import tkinter as tk
import os
import json
import random

#classes
class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

#globals
pathToClassData = "C:\\Users\\joegr\\Desktop\\TF2_Random_Loadout_Generator\\classdata"
pathToItemImages = "C:\\Users\\joegr\\Desktop\\TF2_Random_Loadout_Generator\\images"
classToClassFile = {
    "demoman":"demoman.json",
    "engineer":"engineer.json",
    "heavy":"heavy.json",
    "medic":"medic.json",
    "pyro":"pyro.json",
    "scout":"scout.json",
    "sniper":"sniper.json",
    "soldier":"soldier.json",
    "spy":"spy.json"
    }
    
def mainViewer(fileSet):
    myWindow = tk.Tk()
    myWindow.title("Randomized Loadout")
    windowWidth = 900
    windowHeight = 300
    
    labelstr = fileSet[0]['name'] + ", " + fileSet[1]['name'] + ", and " + fileSet[2]['name']
    
    img1 = tk.PhotoImage(file = pathToItemImages + "\\" + fileSet[0]['imagefile'])
    img2 = tk.PhotoImage(file = pathToItemImages + "\\" + fileSet[1]['imagefile'])
    img3 = tk.PhotoImage(file = pathToItemImages + "\\" + fileSet[2]['imagefile'])
    
    img1 = img1.subsample(2)
    img2 = img2.subsample(2)
    img3 = img3.subsample(2)
    
    canvas = tk.Canvas(myWindow,bg="lightgray",width=windowWidth,height=windowHeight)
    label = tk.Label(text = labelstr,relief=tk.RAISED)
    canvas.create_image(1,1, anchor=tk.NW, image=img1)
    canvas.create_image(windowWidth*.33,1, anchor=tk.NW, image=img2)
    canvas.create_image(windowWidth*.66,1, anchor=tk.NW, image=img3)
    label.pack(side=tk.BOTTOM)
    canvas.pack()
    myWindow.mainloop()

def JsonFileRead(jsonFile):
    f = open(jsonFile,'r')
    string = f.read()
    f.close
    return json.loads(string)

def getClassData():
    os.chdir(pathToClassData)
    classData = os.listdir()
    editedClassData = []
    for i in range(0,len(classData)):
        #changing the class data filename to be presentable
        temp = classData[i][:-5]
        editedClassData.append(temp)

    return editedClassData

def generateLoadout(userClass):
    classFile = classToClassFile[userClass]
    classJson = JsonFileRead(pathToClassData + "\\"+classFile)
    
    primaryRandInt = random.randint(0,len(classJson[0]['weapons'])-1)
    secondaryRandInt = random.randint(0,len(classJson[1]['weapons'])-1)
    tertiaryRandInt = random.randint(0,len(classJson[2]['weapons'])-1)
    
    primaryWeapon = classJson[0]['weapons'][primaryRandInt]
    secondaryWeapon = classJson[1]['weapons'][secondaryRandInt]
    tertiaryWeapon = classJson[2]['weapons'][tertiaryRandInt]
    
    finalLoadout = (primaryWeapon,secondaryWeapon,tertiaryWeapon)
    
    return finalLoadout

def main():
    print("Welcome to the Random Loadout Generator!")
    print("Select a class to generate for:")
    classdata = getClassData()
    classdata.sort()
    
    for i in range(0,len(classdata)):
        print("{0}. {1}".format(i+1,classdata[i].capitalize()))
        
    userInput = input(":")
    userRandomizedLoadout = ""
    for i in range(0,len(classdata)):
        if userInput == classdata[i] or userInput == str(i+1):
            userRandomizedLoadout = generateLoadout(classdata[i])
    
    mainViewer(userRandomizedLoadout)
    

if __name__ == "__main__":
    main()