# Storage Space for methods
#
#

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import 

defaultMaxStorageSize=3

class Item(str):
    def __init__(self,itemID=0):
        super().__init__()
        self.__id = itemID
    
    def getID(self):
        return
    
    def __str__(self):
        return itemDict[self.__id]
    
    def __repr__(self):
        return self.__id

class Storage(dict):
    def __init__(self,maxSize=defaultMaxStorageSize):
        super().__init__()
        self.__max = maxSize
        
    def getMaxSize(self,x):
        return self.__max
        
class Inventory(Storage):
    def __init__(self):
        super().__init__()
    

class Player(FirstPersonController):
    def __init__(self):
        super().__init__()
        self.cursor = Entity(parent=camera.ui, model='circle', color=color.white, scale=.02)
        self.__inventory=Inventory()
        self.__inventoryUI = WindowPanel(title='Inventory', content= (Text('Name:'), InputField(name='name_field')), popup=True, enabled=False)
        
    def resetInventory(self):
        self.__inventory.clear()
        for i in range(0,20):
            self.__inventory[i] = itemDict[0]
    
    def addtoInventory(self,item=None):
        for i in range(0,len(self.__inventory)-1):
            if self.__inventory[i] == None:
                self.__inventory[i] = item
    
    def displayInventory(self,boolean):
        self.__inventoryUI.enabled = boolean
            
    def update(self):
        if held_keys['tab']:
            self.displayInventory(True)
        else:
            self.displayInventory(False)
        super().update()
            