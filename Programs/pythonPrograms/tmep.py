userNum = input("Enter integers between 1 and 100, inclusive: ")
userList = userNum.split(" ")

for i in range(0,len(userList)):
    userList[i] = int(userList[i])

userList.sort()

i=0
while len(userList)>0:
    iCount = userList.count(userList[i])
    if iCount == 1:
        print(userList[i],"occurs",iCount,"time")
        userList.pop(i)
    elif iCount > 1:
        print(userList[i],"occurs",iCount,"times")
        for j in range(0,iCount):
            userList.pop(i)
