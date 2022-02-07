#
# srcebank - a file for storing classes for use in the srcecode module
# 
# File Created by: Joe Griffin
# Date Created: January 20th, 2020
#
# Section: SE-211-001
# Faculty Advisor: Dr. Filippos Vokolos, Ph.D.
# Teaching Assistant: Philip Jones
#

#Importing the srcecode file
import srcecode

#Display Helper String
pageturn = "=================\n-----------------"

#Save CSV method for saving the data back into the desired CSV File
def saveCSV(file,data):
    print("Would you like to save this data to the file? (y/n)")
    uSave = input("|==> ").lower().strip()
    temp = list(data)
    if uSave == "y":
        f = open(file,"w")
        for i in temp:
            if temp.index(i) != len(temp)-1: 
                i[-1] = str(i[-1]) + "\n"
            
        for i in temp:
            for j in i:
                if i.index(j) == len(i)-1:
                    f.writelines(j)
                else:
                    f.writelines(j+",")
            
    elif uSave == "n":
        print("Sending you back to the Home Page!")
    else:
        print("ERROR:notValidInput: Sending user back to Home Page")      #Error Handling

#Data Transfer method which pulls data from the CSV File and makes it into an object
def dataTransfer(file):
    f = open(file,"r")
    CSV = f.readlines()
    data = []
    
    for line in CSV:
        data.append(line.split(","))
   
    for line in data:
        if line != data[-1]:
            line[-1] = line[-1][slice(-1)]
    
    f.close()
    csv = CSVData(data,file)
    return csv

#menuReturn method which asks the user if they want to quit or return to the program
def menuReturn():
    print(pageturn)
    print("Do you wish to return to menu? (y/n)")
    ureturn = input("|==> ").lower().strip()
    
    if ureturn == "y":
        return
    elif ureturn == "n":
        quit()
    else:
        print("ERROR:notValidInput: Sending user back to Home Page")      #Error Handling
        return

#EditCSVdata method that allows the user to select a row and column and then input a value to put in that position)
def editCSVdata(CSV):
    data = CSV.getData()
    print("Enter the Row Number (1,2,3,etc...)")
    uRow=input("|==> ").lower().strip()
    
    if uRow.isalpha():
        print("ERROR:notValidInput: Sending user back to Home Page")      #Error Handling
        return
    
    current = data[int(uRow)-1]
    
    print("Enter the Column Number (1,2,3,etc...)")
    uCol=input("|==> ").lower().strip()
    
    if uCol.isalpha():
        print("ERROR:notValidInput: Sending user back to Home Page")      #Error Handling
        return
    
    value = current[int(uCol)-1]
    
    print("The current value in the postion ("+uCol+","+uRow+") is " + value )
    print("What do you wish to change it to? (Enter Q to not edit the value)")
    uValue = input("|==> ").strip()
    
    if uValue.lower() == "q":
        return
    elif uValue == "":
        print("ERROR:noValueSent: - No value was sent into the program")      #Error Handling
        print("Returning to Menu...(Press Enter to Continue)")
        input("")
    else:
        data[int(uRow)-1][int(uCol)-1] = uValue
        CSV.setData(data)
        saveCSV(CSV.getFile(),CSV.getData())
        
#CSVData Class which is used to carry information gathered from the desired CSVData file
class CSVData():        
    def __init__(self,List,f):
        self.__data = List
        self.__file = f
        
    #Accessors
    def getData(self):
        return self.__data
    def getFile(self):
        return self.__file
    #Mutators
    def setData(self,x):
        self.__data = x
    def setFile(self,x):
        self.__file = x
    
    #ColumnWidth Method for determining how much space should be in each column to account for lenght of the values
    def columnwidth(self):
        self.__cWidth = []
        for i in self.__data[0]:
            self.__cWidth.append(0)    #Creating the cWidth list with the correct amount of elements to match the columns of the CSV Data
        
        for i in self.__data:
            for j in range(0,len(i)):  #Setting the values of the cWidth list to match the length of the longest element of each column
                if len(i[j]) > self.__cWidth[j]:
                    self.__cWidth[j] = int(len(i[j])) 
    
    #String representation method which allows for easily displaying the information storied in the self.__data attribute            
    def __str__(self):
        for i in self.__data:
            string = ""
            for j in range(0,len(i)): #using the cWidth variable and string from each element to perfectly space the lines of the CSV data
                if len(i[j]) < self.__cWidth[j]:
                    space = (self.__cWidth[j]-len(i[j])) * " "
                    string += space + str(i[j]) + "|"
                else:
                    string += str(i[j]) + "|"
                    
            print(string)
        
        return ""

