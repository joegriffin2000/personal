#
# This script is to allow users to provide a number and simulate the path for that number on the Collatz Conjecture
# In order to understand more about the Collatz Conjecture I recommend looking it up online to understand how it works.
# 
# Essentially, the program is supposed to find the thread of numbers associated with a given number such that even numbers are to be halfed and 
# odd numbers are to be multiplied by three and incremented by one (in that order). This provides a string of numbers where every result 
# eventually ends with the thread: 4-2-1 due to what is known as the Collatz Conjecture
#
# Created by Joseph Griffin
# 

lineBreak = "~"*20

def main():
    grablist = []
    spaceVal = 1
    while True:
        print("\nProvide a Number. Enter 'y' when finished.")
        print("Current Numbers Selected:",grablist)
        userNum = input(":").lower().strip()
        
        if userNum.isdigit():
            grablist.append(userNum)
            userNum=""
        elif userNum == "y":
            print(lineBreak)
            for i in grablist:
                final = inputProcessing(i)
                print(f"[{i:^3}]: {str(final)}")
            break
        else:
            print("Invalid Input: Not a Number")
    

def inputProcessing(userInput):
    listOutput = list()
    userInput = float(userInput)
    
    while (userInput > 1):
        if userInput % 2 == 0:
            userInput /= 2
        else:
            userInput = userInput * 3 + 1
        
        listOutput.append(userInput)
    
    return listOutput
    

if __name__ == "__main__":
    main()