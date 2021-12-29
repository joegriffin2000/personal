#Mark Boady and Matthew Burlick
#Drexel University 2018
#CS 172

from monster import *
import random

#This function has two monsters fight and returns the winner
def monster_battle(m1, m2):

    m1.resetHealth()
    m2.resetHealth()

    #next print out who is battling
    print("Starting Battle Between")
    print(m1.getName()+": "+m1.getDescription())
    print(m2.getName()+": "+m2.getDescription())
    
    
    #Whose turn is it?
    attacker = None
    defender = None
    
    #Select Randomly whether m1 or m2 is the initial attacker
    #to other is the initial defender
    roll = random.randint(0,1)
    if roll == 0:
        attacker = m1
        defender = m2
    else:
        attacker = m2
        defender = m1
    
    print(attacker.getName()+" goes first.")
    
    #Loop until either 1 is unconscious or timeout
    while( m1.getHealth() > 0 and m2.getHealth() > 0):
        #Determine what move the monster makes
        #Probabilities:
        #   60% chance of standard attack
        #   20% chance of defense move
        #   20% chance of special attack move

        #Pick a number between 1 and 100
        move = random.randint(1,100)
        #It will be nice for output to record the damage done
        before_health=defender.getHealth()
        
        #for each of these options, apply the appropriate attack and 
        #print out who did what attack on whom
        if( move >=1 and move <= 60):
            #Attacker uses basic attack on defender
            attacker.basicAttack(defender)
            print(attacker.getName() + " used " + attacker.basicName() + " on " + defender.getName())
        elif move>=61 and move <= 80:
            #Defend!
            attacker.defenseAttack(defender)
            print(attacker.getName() + " used " + attacker.defenseName() + " on " + defender.getName())
        else:
            #Special Attack!
            attacker.specialAttack(defender)
            print(attacker.getName() + " used " + attacker.specialName() + " on " + defender.getName())
        
        temp = attacker
        attacker = defender
        defender = temp
        print(defender.getName() +" at "+ str(defender.getHealth()))
        print(attacker.getName() +" at "+ str(attacker.getHealth()))
        print("")
    
    win = attacker
    
    if attacker.getHealth() == 0:
        win = defender
    if defender.getHealth() == 0:
        win = attacker
    
    return win

#----------------------------------------------------
if __name__=="__main__":
    #Every battle should be different, so we need to
    #start the random number generator somewhere "random".
    #With no input Python will set the seed
    
    first = LittleBunnny()
    second = mikeTyson()
    
    winner1 = monster_battle(first,second)
    print(winner1.getName()+" is victorious in the first match!")
    print("")
    
    first = goblin("Jess the Goblin")
    second = werewolf("Benjamin the Werewolf")
    
    winner2 = monster_battle(first,second)
    print(winner2.getName()+" is victorious in the second match!")
    print("")
    
    
    first = winner1
    second = winner2
    
    winner3 = monster_battle(first,second)
    print(winner3.getName()+" is victorious in the final match!")
    print("")