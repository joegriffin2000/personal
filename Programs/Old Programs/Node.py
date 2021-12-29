#Name: Joe Griffin
#Drexel ID: jeg358
#Purpose: Node Class Script

#TAKEN FROM LECTURE NOTES
#Title: LinkedListDemo.py
#Author:   Adelaida A. Medlock
#Date:     Febraury 18, 2019
#Code Version: 1
#Availability: https://learn.dcollege.net/webapps/blackboard/content/listContent.jsp?course_id=_235963_1&content_id=_7557822_1

from LinkedList import *
from Employee import *

# The Node class - to be used to create linked lists
# a Node is the basic unit in a linked list

class Node():
    def __init__(self, data, next = None):
        self.__data = data
        self.__next = next
    
    # getters
    def getData(self):
        return self.__data
    
    def getNext(self):
        return self.__next
    
    #setters
    def setData(self,d):
        self.__data = d

    def setNext(self,n):
        self.__next = n

    #overloaded operators
    def __str__(self):
        return self.__data