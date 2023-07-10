# jsonInventoryClassFormat
# by Joe "Dynaj03" Griffin
# 
# this is an example of an inventory system that uses a specified json file and is able to work with it.
# has a variety of uses just needs to be modified for them

import json

Classes_kword = 'classes'
Loadouts_kword = 'loadouts'
class_kword = 'class'
loadout_kword = 'loadout'

class inventory():
    def __init__(self,invFile):
        self.invFile = invFile
        self.invJson = self.JsonFileRead()
        
        #setting important lists for inventory
        self.invLoadoutList = self.invJson[Loadouts_kword]
        self.invClassList = self.invJson[Classes_kword]
        self.invClassList = list(set(self.invClassList))   #getting rid of duplicates
        self.invClassList.sort()
        
        if not self.validLoadoutCheck():
            raise KeyError("Classes in the file \'" + self.invFile + "\' do not correlate with Loadouts")
    
    def setInvFile(self,xFile):
        self.invFile = xFile
        self.invJson = self.JsonFileRead()
        
        self.invLoadoutList = self.invJson[Loadouts_kword]
        self.invClassList = self.invJson[Classes_kword]
        self.invClassList = list(set(self.invClassList))
        self.invClassList.sort()
        
        if not self.validLoadoutCheck():
            raise KeyError("Classes in the file \'" + self.invFile + "\' do not correlate with Loadouts")
        
    def getInvClassList(self):
        return self.invClassList
    def getInvLoadoutList(self):
        return self.invLoadoutList
    
    #DO_NOT_TOUCH_THIS_FUNCTION
    def JsonFileRead(self):
        f = open(self.invFile,'r')
        string = f.read()
        f.close()
        return json.loads(string)
    
    #DO_NOT_TOUCH_THIS_FUNCTION
    def JsonFileWrite(self,jsonWrite,jsonIndent=4):
        f = open(self.invFile,'w')
        f.write(json.dumps(jsonWrite, indent=jsonIndent))
        f.close()
    
    #validLoadoutCheck
    #checks the class lists and the loadout to see if every class listed in the loadout is also in the class list.
    def validLoadoutCheck(self):
        result = True
        for i in self.invLoadoutList:
            if self.invClassList.count(i[class_kword]) == 0:
                result = False
        return result
    
    def __str__(self,indent=4):
        result = "Printing from \'" + self.invFile + "\'\n\n"
        
        #This needs to be changed if change the format of the loadouts
        item_kword = 'item'
        name_kword = 'name'
        for Class in self.invLoadoutList:
            result += Class[class_kword].capitalize() + ":\n"
            count=0
            for ClassSlot in Class[loadout_kword]:
                count+=1
                result += (indent*" ") + str(count) + "." + ClassSlot[item_kword][name_kword].capitalize() + "\n"
            
        return result
        
if __name__ == "__main__":
    jfile = "dynaj03.json"
    dyna = inventory(jfile)
    print(dyna)
