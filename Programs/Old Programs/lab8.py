from BST import *
import random
import time
import matplotlib.pyplot as plt

def populate(n):
    list = []
    bst = BST()
    
    for i in range(0,n):
        temp = random.randint(0,n)
        list.append(temp)
        
    for i in range(0,len(list)):
        bst.append(list[i])
        
    return (list,bst)

def check(list,x):
    for i in range(0,len(list)):
        if list[i] == x:
            return True
    
    return False

#plt.plot(10000,30,label='Linear vs Binary')
plt.ylabel("Seconds")
plt.xlabel("Number of Elements per Search")

TotalLine = []
TotalBST = []
TotalN = []
counter=0
counter2=0

n=1000
while n <= 10000:
    TotalN.append(n)
    both = populate(n)

    newList = both[0]
    newBST = both[1]

    print()

    #Checking and timing in Lineart Search
    beforeLine = time.time()
    print("Searching in Linear Search....")
    for i in range(0,len(newList)):
        #print(i, end=" ")
        if check(newList,i) == True:
            #print("True")
            counter+=1
        '''else:
            #print("False")
            pass'''
    afterLine = time.time()
    TotalLine.append(afterLine-beforeLine)
    
    print("Linear Time Elapsed for",n,"Values:",afterLine-beforeLine)

    #Checking and timing in Binary Search Tree
    beforeBST = time.time()
    print("Searching in BST....")
    for i in range(0,len(newList)):
        #print(i,end = ' ')
        
        if newBST.isin(i) == True:
            counter2 += 1
        '''if counter > 0:
            #print(True)
            pass
        else:
            #print(False)
            pass'''
            
    afterBST = time.time()
    
    TotalBST.append(afterBST-beforeBST)

    print("BST Time Elapsed for",n,"Values:",afterBST-beforeBST)
    
    n+=1000

plt.plot(TotalN,TotalLine, 'b-')
plt.plot(TotalN,TotalBST, 'r-')
plt.legend()
plt.show()