# Test program just to get something on this computer
# by Joe Griffin
# March 3, 2021
# 

import itemSrc
import sys
import os

#Globals
itemFile = 'itemfile.json'
stdPrompt = 'Select: '

def postScreen():
    print("\n")
    print("Do you wish to go back to the main menu? (y/n)")
    u = input(stdPrompt).lower().strip()
    return u

def displayItems():
    print("Locating Item File...")
    file = open(itemFile,'r')
    print(file.read())
    file.close()
    
def convJSON():
    
    
if __name__ == "__main__":
    user = ""
    while (user.lower().strip() != "q"):
        print("\n~ Item Hub ~")
        print("[A] Display All Current Items")
        print("[B] Create Items")
        print("[C] Delete Items")
        
        print("[Q] Quit Program\n")
        user = input(stdPrompt).lower().strip()
        
        if (user == "a") or (user == "1"):
            displayItems()
        elif (user == "b") or (user == "2"):
            print(user)
        elif (user == "c") or (user == "3"):
            print(user)
        elif (user == "q") or (user == "4"):
            pass
        else:
            print("Invalid Entry: Sending Back to Main Menu")
            continue
        
        user = postScreen()
    
        if user == "n":
            print("Exiting Program...")
            sys.exit()
        elif user == "y":
            print("Sending Back to Main Menu")
            continue
        else:
            print("Invalid Entry: Sending Back to Main Menu")
            
            