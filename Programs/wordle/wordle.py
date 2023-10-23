#wordle dupe
#by dynaj03

import random

file = "savefile1.txt"
f = open(file,"r")
ListOfWords = f.read().split()
f.close()
ListOfWords.sort()

file = "sgb-words.txt"
f = open(file,"r")
AllWordsStanford = f.read().split()
f.close()
AllWordsStanford.sort()

AllLetters = set(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])

def main():
    RandomWord = ListOfWords[random.randint(0,len(ListOfWords))]
    print("Enter a Word! You have 6 Tries.")
    
    user = ""
    counter = 1
    etched = set()
    
    while((user != RandomWord) and (counter <= 6)):
        user = input(" - "+str(counter)+":").strip().lower()
        if (AllWordsStanford.count(user) != 0) and (len(user) == 5):
            print()
            print("\t" + " ".join(list(user)))
            print("\t" + " ".join(getMatchString(RandomWord,user)))
            print()
            
            etched.update(user)
            #print("Tried: "," ".join(etched.difference(set(RandomWord))).upper())
            #print("Available: ", " ".join(AllLetters.difference(etched).union(set(RandomWord))).upper())
            
            counter +=1
        else:
            print("NOT A VALID WORD. TRY AGAIN")
    
    print()
    print("The Word Was:",RandomWord.capitalize())
    
    if (RandomWord == user):
        print("Victory!")
    else:
        print("Too Bad...")
        
def getMatchString(RandomWord,userWord):
    matchString=["*","*","*","*","*"]
    for i in range(0,len(RandomWord)):
        if RandomWord[i] == userWord[i]:
            matchString[i] = "!"
        elif (RandomWord.count(userWord[i]) > 0):
            matchString[i] = "?"
    
    return matchString

#method for checking for count of a given word
def copyCheck():
    attemptWord = input("word2check: ")
    if (ListOfWords.count(attemptWord) == 1):
        print(True)
    elif (ListOfWords.count(attemptWord) > 1):
        print("ERROR: WORD IS IN THE LIST MORE THAN ONCE ALREADY")   
    else:
        print(False)
        
def printingPlurals():
    for i in ListOfWords:
        if i.startswith("d") and i.endswith('s'):
            print(i)

def wordCount():
    count=0
    for i in ListOfWords:
        count +=1
    print(count)

def pieceCheck():
    c1 = 's'
    for i in ListOfWords:
        if ((i.endswith(c1))):
            print(i)
    
if __name__ == "__main__":
    main()
    #copyCheck()
    #printingPlurals()
    #wordCount()
    #pieceCheck()
    
    input()