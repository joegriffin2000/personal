# notepad document - used for testing ideas
#

#Selected File Drive
drive = "C:"
#Imports
import os

def test():
    print(os.listdir())
    
def isDir():
    pass

def menu():
    print("Welcome to the File Management System")
    print("Currently Displaying ")
    print(os.getcwd())
    user = input("> ").lower().strip()
    
def help():
    pass

if __name__ == "__main__":
    os.chdir("/")
    #menu()
    test()