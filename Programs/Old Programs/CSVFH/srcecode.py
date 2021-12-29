#
# srcecode - a file for containing the initial file testing methods as well as the main menu method for interacting with the user on the homepage
#
# File Created by: Joe Griffin
# Date Created: January 20th, 2020
#
# Section: SE-211-001
# Faculty Advisor: Dr. Filippos Vokolos, Ph.D.
# Teaching Assistant: Philip Jones

import sys
from os import listdir      #Importing the srcebank file along with system and os
from srcebank import *


#Gatekeeper method which checks to see if the program was triggered with a file as the argument
def gatekpr(): 
    if len(sys.argv) >= 2:
        if test(sys.argv[1]):
            mainMenu(sys.argv[1])
        else:
            pass
    else:
        print("ERROR:noFileSent: - No file was sent into the srcecode.py program - most likely an error in the CSVFH file")

#test method for seeing if the file is in the current directory
def test(file):
    if file in listdir():
        return True
    else:
        print("ERROR:FileInvalid: - No file was found in the CSV File Handling Folder - Make sure you are typing the right name!")


#Main Menu method for interacting with the user on the homepage
def mainMenu(file):
    CSV = dataTransfer(file)
    CSV.columnwidth()
    
    print("Hello! Welcome to the CSV File Handler")
    user = ""
    
    while user != "q":  #Home Page Loop
        print(pageturn)
        print("The File You Have Selected Is: '" + file + "'")
        print("What would you like to do with this file?")
        print("1) Display File Data")
        print("2) Edit File Data")
        print("Q) Quit the Program")
        
        user = input("|==> ").lower().strip()
        print()
        
        if user == "1":         #Displaying File Data
            print(pageturn)
            print("Displaying...(You May Need to Make the Window Bigger)")
            print(str(CSV))
            menuReturn()
            
        elif user == "2":       #Editing File Data
            print(pageturn)
            print("Displaying...(You May Need to Make the Window Bigger)")
            print(str(CSV))
            
            editCSVdata(CSV)
            CSV = dataTransfer(file)
            CSV.columnwidth()
            menuReturn()
            
        elif user == "q":       #Letting the user value pass through in order to quit the program correctly
            pass
        
        else:                   #Error Handling
            print("ERROR:InputInvalid: - The option you inputted is not available - Try something else!")

#This triggers when the script is activated but only after all of the methods have been created
if __name__ == "__main__":
    gatekpr()