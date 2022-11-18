# working on an inventory system using json files
#
#

#imports
import json
import sys

#globals
jsonFile = 'playerInventory.json'
validArgs = ["-f"]

def CheckArgs():
    args = sys.argv
    for i in range(0,len(args)):
        if validArgs.count(args[i]) > 0:
            if args[i] == "-f":
                SetFile(args[i+1])
                
def SetFile(filename):
    global jsonFile
    jsonFile = filename

#direct json file reading
def JsonFileRead():
    f = open('inventory//'+jsonFile,'r')
    string = f.read()
    f.close
    return json.loads(string)

#direct json file saving
def JsonFileSave(editedjson):
    f = open('inventory//'+jsonFile,'w')
    temp = json.dumps(editedjson,indent=4)
    f.write(str(temp))
    f.close()

#specialized design for the inventory
def JsonPrettyPrint(json):
    for i in json:
        print("========================================================")
        print("Name:",i['name'])
        print("Stats:",i['stats'])
        
def CreateNewItem():
    itemName = input("Name:").strip().lower()

def Main():
    print("Welcome to your Inventory!")
    print("Displaying Items:")
    
    inventory = JsonFileRead()
    JsonPrettyPrint(inventory)
    JsonFileSave(inventory)
    

if __name__ == '__main__':
    CheckArgs()
    Main()