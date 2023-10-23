# ______________________________________________________
# ImageViewing
# By DynaJ03
# 

import os
import sys
from tkinter import *
from PIL import ImageTk,Image

def inputMenu():
    print("Please Provide a Path to a Directory! (enter q to quit or r to return)")
    print("This path starts right here at '{}'".format(os.getcwd()))
    directory = input(": ").strip()
    
    if directory.lower() == "q" or directory.lower() == "quit":
        print("Quitting...")
        return "exit"
    elif directory.lower() == "r" or directory.lower() == "return":
        print("Returning...")
        return "retry"
    elif directory[len(directory)-1] != '\\': #Adds a slash to the end to make sure we are working in a directory no matter what the user puts in
        directory += '\\'
        
    try:
        setDir(directory)
    except:
        return "retry"
    
    displayDir()
    print("Which File Would You Like To View? (enter q to quit or r to return)")
    file = input(": ")
    
    if file.lower().strip() == "q" or file.lower().strip() == "quit":
        print("Quitting...")
        return "exit"
    elif file.lower().strip() == "r" or file.lower().strip() == "return":
        print("Returning...")
        return "retry"
    
    try:
        setFile(file)
    except:
        return "retry"
    
    return file

def displayDir(List = os.listdir()): #Function for Displaying Image Files in a Directory
    print()
    print("Displaying Image Files (ending in .png or .jpg)")
    print(List)
    counter = 0
    for i in List:
        if i.endswith(".png") or i.endswith(".jpg"):
            ++counter
            print(counter,i)

def setDir(filePath):
    try:
        os.chdir(filePath)
    except FileNotFoundError:
        print("The directory path given could not be found")
        raise FileNotFoundError
    except NotADirectoryError:
        print("The directory path given could not be found")
        print("Make sure you are passing in a directory and not a file.")
        raise NotADirectoryError

def setFile(fileName):
    try:
        f = open(fileName,"r")
        f.close()
    except FileNotFoundError:
        print("The directory path given could not be found")
        print("Make sure you are passing in a directory and not a file.")

def mainViewer(file):
    myWindow = Tk()
    myWindow.title("Viewing " + file)
    img = ImageTk.PhotoImage(Image.open(file))
    
    canvas = Canvas(myWindow, width = img.width(), height = img.height())
    canvas.pack()
    canvas.create_image(1,1, anchor=NW, image=img)
    myWindow.mainloop()


if __name__ == "__main__":
    while True:
        fileString = inputMenu()
        
        if fileString == "exit": #After interacting with the user, determines whether or not the user still wants to view a file or would rather quit out of the program
            break
        elif fileString == "retry":
            continue
        else:
            mainViewer(fileString)
        
