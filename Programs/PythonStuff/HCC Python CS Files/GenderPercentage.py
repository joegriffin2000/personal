print("Welcome to the Gender Percentage Calculator") #Prompting the User
print("Please Insert the Number of Men and Women in Your Class")
numMen = int(input("Men:"))
numWomen = int(input("Women:"))

#Calculating
numTotal = numMen + numWomen 
percentMen = numMen / numTotal
percentWomen = numWomen / numTotal

#Formating the numbers correctly
percentMen = percentMen * 100
percentWomen = percentWomen * 100

#Printing out the numbers to the screen (and doing a formatting trick)
print("")
print("Men: "+ str(round(percentMen)) +"%")
print("Women: "+ str(round(percentWomen)) +"%")