# Designing a code to work with my newly designed Hexaternary System
#
# The Hexaternary Number System answers the same question that the hexadecimal system answers which is:
# "how can I fit shit loads of number into a very small value" and it succeeds.
#
# The Hexaternary System uses the digits 0-9 as well as all letters a-z in order to do value representation.

def decimalize(s):
    ordS = ord(s) #finding the ascii's value
    #UpperCase Situation
    if ordS >= 65 and ordS <= 90: 
        ordS += 10 #adjusting for 0-9 digits
        ordS -= 65 #subtracting for true value
        return ordS #sending back value
    #LowerCase Situation
    elif ordS >= 97 and ordS <= 122:
        ordS += 10 #adjusting for 0-9 digits
        ordS -= 97 #subtracting for true value
        return ordS #sending back value

def main():
    print("Please insert the septaternary number to be converted to decimal")
    userInput = str(input("/:").strip())
    numList = list(userInput)
    numList.reverse()
    
    accumulate = 0
    digitMultiplier = 1
    for i in range(0,len(numList)):                                       #start iterating through the provided number 
        digitMultiplier = 36 ** i                                         #setting the digit multiplier for every digit
        if numList[i].isdigit():                                          #if its already a number
            #print("{0}. {1}*{2}".format(i+1,numList[i],digitMultiplier)) #premade print statements for showing number processing in realtime
            accumulate += int(numList[i]) * digitMultiplier               #adding the found value to the accumulate
        elif numList[i].isalpha():                                        #if it is a letter that needs to be converted to a number
            #print("{0}. {1}*{2}".format(i+1,numList[i],digitMultiplier)) #premade print statements for showing number processing in realtime
            accumulate += int(decimalize(numList[i])) * digitMultiplier   #adding the found value to the accumulate
        else:
            print("Error: Invalid Character Caught in Parsing")
    
    print("")
    print("Hexaternary:",userInput)
    print("Decimal:",accumulate)
    print("")

if __name__ == "__main__":
    main()