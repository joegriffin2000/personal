#Name: Joe Griffin
#Drexel ID: jeg358
#Purpose: Main Employee Database

from Node import *
from LinkedList import *
from Employee import *

#Function for handling option A
def optionA(): 
    userID = str(input("Enter the Employee ID(Less than 6 numbers): "))
    userpayRate = float(input("Enter the hourly rate: "))
    
    for i in range(0,len(my_Database)):
        current  = my_Database[i]
        if current.getID() == userID:
            print("Invalid Response: Already in Database")
            return
        
    if userpayRate < 6.00:
        print("Invalid Response: Pay Rate Less Than Six")
        return
    
    try:
        userpayRate = float(userpayRate)
    except:
        print('Invalid Response: Pay Rate is not a Number')
        return
        
    
    newGuy = Employee(userID)
    newGuy.setpayRate(userpayRate)
    
    my_Database.append(newGuy)

#Function for handling option B 
def optionB():
    for i in range(0,len(my_Database)):
        current = my_Database[i] 
        print(current) #displaying the data about current
        print("Enter the hours worked for Employee",current.getID(),":",end=" ")
        currentHours = input()
        print()
        
        try:
            currentHours = float(currentHours)
        except:
            print('Invalid Response: Response is not a Number')
            return
        
        if currentHours < 0: #checking to make sure it is positive
            print("Invalid Response: Work Hours Less Than Zero")
            return
        
        current.setworkHours(currentHours) #setting new work hours
        current.setgrossWages() #updating gross wages
        

#Function for handling option C
def optionC():
    print(" *** Payroll *** ")
    print(my_Database)

#Function for handling option D
def optionD():
    for i in range(0,len(my_Database)):
        current = my_Database[i]
        print(current)
        print("Enter the New Hourly Rate for Employee",current.getID(),":",end=" ")
        currentpayRate = input()
        print()
        
        try:
            currentpayRate = float(currentpayRate)
        except:
            print('Invalid Response: Response is not a Number')
            return
        
        if currentpayRate < 6.00:
            print("Invalid Response: Pay Rate Less Than Six")
            return
        
        current.setpayRate(currentpayRate)
        current.setgrossWages()

#Function for handling option E
def optionE():
    userSearch = input("Enter the ID of the Employee you wish to remove: ")
    try:
        my_Database.remove(Employee(userSearch))
        print("Done")
    except:
        print("Invalid Removal: Employee ID Not Found")
 
#Initializing User Response and LinkedList as user and my_Database
my_Database = LinkedList()
user = ""

#Main Script
while user.lower().strip(' ') != "exit":
    #Repeating Menu
    print("*** CS 172 Payroll Simulator ***")
    print("a. Add New Employee")
    print("b. Enter Hours Worked")
    print("c. Display Payroll")
    print("d. Update Employee Hourly Rate")
    print("e. Remove Employee From Payroll")
    print("f. Exit the Program")
    user = input("Enter your choice: ")
    print()
    
    #Testing for different responses
    if user.lower().strip(' ') == 'a':
        optionA()
    elif user.lower().strip(' ') == 'b':
        optionB()
    elif user.lower().strip(' ') == 'c':
        optionC()
    elif user.lower().strip(' ') == 'd':
        optionD()
    elif user.lower().strip(' ') == 'e':
        optionE()
    elif user.lower().strip(' ') == 'f':
        print("Good-Bye!")
        user = 'exit'
    else:
        print("Invalid Response: Response not in Option Range")
    
    print()    