def contains(self,other):
    return self.count(other) >= 1

def ListToDict(LIST1 = None,LIST2 = None):
    DICT = {}
    if (LIST1 == None) and (LIST2 == None):
        pass
    elif (LIST1 != None) and (LIST2 == None):
        for i in range(0,len(LIST1)):
            DICT[i] = LIST1[i]
    elif (LIST1 != None) and (LIST2 != None):
        if len(LIST1) == len(LIST2):
            for i in range(0,len(LIST1)):
        else:
            raise IndexError('Union not allowed with list of differing lengths')
            return None
    else:
        pass
    return DICT
    
def makeAutoMenu(LIST,STEP=1,START=0,STOP=None,CAP=']'):
    if STOP == None:
        STOP = len(LIST)

    for i in range(START,len(LIST),STEP):
        print("{0}{1} {2}".format(i+1,CAP,LIST[i]))

if __name__ == "__main__":
    #makeAutoMenu(['man','sheep','pony','dog'])
    #print(contains([1,2,3],3))
    listOne = [10,12,13,14,15]
    listTwo = ["A","B","C","D","E"]
    dictOneTwo = ListToDict(listOne,listTwo)

    print(dictOneTwo)