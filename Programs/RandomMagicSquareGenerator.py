import random

def printList(xList):
    for i in range(0,len(xList)):
        print(xList[i])


multiDimensionalArray = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

num = 0

range1 = list(range(0,5))
range2 = list(range(0,5))

random.shuffle(range1)
random.shuffle(range2)

for i in range1:
    for j in range2:
        num += 1
        multiDimensionalArray[i][j] = num

printList(multiDimensionalArray)