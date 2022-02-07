from AccountClass import *
#from FrameWork import *

def ApprovedMenu():
    print("Welcome")
    print("What would you like to do?")
    Input = input(": ")

if __name__ == "__main__":
    print("Hello! Welcome to the Account Storage UI")
    print("Please insert an admin username and password")
    if AdminLogin() == True:
        print("\n"*30)
        ApprovedMenu()
        