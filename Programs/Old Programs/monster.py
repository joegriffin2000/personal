#Mark Boady and Matthew Burlick
#Drexel University 2018
#CS 172

#This class defines a generic monster
#It doesn't actually DO anything.
#It just gives you a template for how a monster works.

#We can make any number of monsters and have them fight
#they just all need to INHERIT from this one so that work the same way

#Since this class is not intended to be used
#none of the methods do anything
#This class is cannot be used by itself.
import abc

class monster(metaclass=abc.ABCMeta):
    def __init__(self):
        return
    def __str__(self):
        return "Generic Monster Class"
    #Methods that need to be implemented
    #The description is printed at the start to give
    #additional details
    
    #Name the monster we are fighting
    #The description is printed at the start to give
    #additional details
    @abc.abstractmethod
    def getName(self):
        pass
        
    @abc.abstractmethod
    def getDescription(self):
        pass
        
    #Basic Attack Move
    #This will be the most common attack the monster makes
    #You are passed the monster you are fighting
    @abc.abstractmethod
    def basicAttack(self,enemy):
        pass
        
    #Print the name of the attack used
    @abc.abstractmethod
    def basicName(self):
        pass
        
    #Defense Move
    #This move is used less frequently to
    #let the monster defend itself
    @abc.abstractmethod
    def defenseAttack(self,enemy):
        pass
        
    #Print out the name of the attack used
    @abc.abstractmethod
    def defenseName(self):
        pass
        
    #Special Attack
    #This move is used less frequently
    #but is the most powerful move the monster has
    @abc.abstractmethod
    def specialAttack(self,enemy):
        pass
        
    @abc.abstractmethod
    def specialName(self):
        pass
        
    #Health Management
    #A monster at health <= 0 is unconscious
    #This returns the current health level
    @abc.abstractmethod
    def getHealth(self):
        pass
        
    #This function is used by the other monster to
    #either do damage (positive int) or heal (negative int)
    @abc.abstractmethod
    def doDamage(self,damage):
        pass
        
    #Reset Health for next match
    @abc.abstractmethod
    def resetHealth(self):
        pass

class goblin(monster):
    def __init__(self,name = "Goblin"):
        self.__name = name
        self.__description = "A Small Green Skinned Creature with Large Horns"
        self.__health = 23
        self.__maxhealth = 23
        
    def __str__(self):
        return "Goblin Subclass"
    
    def getName(self):
        return self.__name
        
    def getDescription(self):
        return self.__description
       
    def basicAttack(self,enemy):
        enemy.doDamage(3)
    
    def basicName(self):
        return ("Slash")
    
    def defenseAttack(self,enemy):
        self.__health += 1
    
    def defenseName(self):
        return ("Heal")
        
    def specialAttack(self,enemy):
        enemy.doDamage(6)
        
    def specialName(self):
        return("Slam")
        
    def getHealth(self):
        if self.__health < 0:
            self.__health = 0
        return self.__health

    def doDamage(self,damage):
        self.__health -= damage
        
    def resetHealth(self):
        self.__health = self.__maxhealth
        
class werewolf(monster):
    def __init__(self,name = "Wolfman"):
        self.__name = name
        self.__description = "A half man, half fur, all evil"
        self.__health = 25
        self.__maxhealth = 25
        
    def __str__(self):
        return "Werewolf Subclass"
    
    def getName(self):
        return self.__name
        
    def getDescription(self):
        return self.__description
       
    def basicAttack(self,enemy):
        enemy.doDamage(4)
    
    def basicName(self):
        return ("Bite")
    
    def defenseAttack(self,enemy):
        self.__health += 1
    
    def defenseName(self):
        return ("Heal")
        
    def specialAttack(self,enemy):
        enemy.doDamage(5)
        
    def specialName(self):
        return("Pounce")
        
    def getHealth(self):
        if self.__health < 0:
            self.__health = 0
        return self.__health

    def doDamage(self,damage):
        self.__health -= damage
        
    def resetHealth(self):
        self.__health = self.__maxhealth
        
class mikeTyson(monster):
    def __init__(self):
        self.name = 'Mike Tyson'
        self.description = 'Former boxer. Owns a tiger. Has dangerous teeth.'
        self.health = 30
        self.maxHealth = 30
    def __str__(self):
        return "Human Subclass"
    def getName(self):
        return self.name
    def getDescription(self):
        return self.description
    def basicAttack(self, enemy):
        enemy.doDamage(4)
    def basicName(self):
        return 'Bite Ear'
    def defenseAttack(self,enemy):
        pass
    def defenseName(self):
        return 'Block'
    def specialAttack(self, enemy):
        enemy.doDamage(15)
    def specialName(self):
        return 'Pet Tiger'
    def getHealth(self):
        if self.health < 0:
            self.health = 0
        return self.health
    def doDamage(self, damage):
        self.health -= damage
    def resetHealth(self):
        self.health = self.maxHealth

class LittleBunnny(monster):
    def __init__(self):
        self.name = 'Little Bunny'
        self.description = 'A harmless, cute, and innocent bunny.'
        self.health = 10
        self.maxHealth = 10
    def __str__(self):
        return "Bunny Subclass"
    def getName(self):
        return self.name
    def getDescription(self):
        return self.description
    def basicAttack(self, enemy):
        enemy.doDamage(1)
    def basicName(self):
        return 'Nibble'
    def defenseAttack(self,enemy):
        pass
    def defenseName(self):
        return 'cuteness'
    def specialAttack(self, enemy):
        enemy.doDamage(2)
    def specialName(self):
        return 'Super Ultra Mega Nibble'
    def getHealth(self):
        if self.health < 0:
            self.health = 0
        return self.health
    def doDamage(self, damage):
        self.health -= damage
    def resetHealth(self):
        self.health = self.maxHealth
