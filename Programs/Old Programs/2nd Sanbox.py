#Asking the user for a valid input
def get_integer():
    valid=False
    while not valid:
        try:
            x = input(question)
            x=int(x)
            valid=True
        except ValueError as e:
            print("Could Not Understand")
    return x

#Messing with lists  
L = [x**2 for x in range (0,10)]
print(L)