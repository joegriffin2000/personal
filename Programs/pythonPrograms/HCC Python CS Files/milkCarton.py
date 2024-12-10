print("Welcome To the Milk Carton Calculator")
print("Please Enter the Amount of Milk Produced This Morning Below")
milkAmount = float(input("In Liters:"))

print("")
print("The amount of milk produced was "+str(milkAmount)+" Liters")

#The number of cans would be the total amount of liters of milk divided by 3.78 (for how many liters can fit in a can)
numCans = milkAmount / 3.78
print("This would make "+str(round(numCans))+" cans")

#The cost of a single can would be $1.44 so multiplying it by the number of cans would get us the total cost of making the cans of milk.
costMilk = numCans * 1.44
print("This would cost $"+str(round(costMilk,2))+" dollars") #printing with a cost value formated for actual currency

#The profit of the cans would be the profit of any specific can times the number of cans that are sold (being all of the cans for simplicity's sake)
profitMilk = numCans *.27
print("This would produce $"+str(round(profitMilk,2))+" dollars in profit") #printing with a profit value formated for actual currency