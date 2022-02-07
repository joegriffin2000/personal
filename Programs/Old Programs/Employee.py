#Name: Joe Griffin
#Drexel ID: jeg358
#Purpose: Employee Class Script

from Node import *
from LinkedList import *

class Employee():
    def __init__(self,id,hours=0,payrate=0,gross=0):
        self.__ID = id
        self.__workHours = float(hours)
        self.__payRate = float(payrate)
        self.__grossWages = float(gross)
        self.setgrossWages()
        
    def getID(self): #id accessor 
        return self.__ID
    
    def getworkHours(self): #work hours accessor 
        return self.__workHours
    
    def getpayRate(self): #pay rate accessor 
        return self.__payRate
    
    def getgrossWages(self): #gross wages accessor 
        return self.__grossWages
    
    def setworkHours(self,workHours): #work hours getter
        self.__workHours = round(float(workHours),2)
        
    def setpayRate(self,payRate): #pay rate getter
        self.__payRate = round(float(payRate),2)
        
    def setgrossWages(self): #gross wages getter
        self.__grossWages = round(self.__workHours * self.__payRate,2)
        
    def __str__(self):
        print("ID:",self.__ID)
        print("Work Hours:",self.__workHours)
        print("Pay Rate:",self.__payRate)
        string = "Gross Wages: " + str(self.__grossWages)
        return string
    
    def __eq__(self,a,b):
        if a.getID == b.getID:
            return True
        else:
            return False
    
if __name__ == "__main__":
    print(Employee("221"))