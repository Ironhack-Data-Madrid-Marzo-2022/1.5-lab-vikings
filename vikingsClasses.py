from audioop import add
from os import lseek
import random


lseek#MODIFY 
# Soldier


from email.base64mime import header_length
from re import X
from tokenize import Name
from unicodedata import name


class Soldier:
    def __init__(self, health, strength):
        self.health= health
        self.strength= strength 

    def attack(self):
        return self.strength

        
    def receiveDamage(self, n):
            self.health=self.health - n

        

    

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):

        self.health= health
        self.strength= strength
        self.name= name

    def attack(self):

        return super().attack()

    def receiveDamage(self, n):
        self.health=self.health - n
        if self.health > 0:
            return self.name+' has received '+str(n)+' points of damage'
            
        else: 
            return self.name+' has died in act of combat'
            

    def battleCry(self):
        return 'Odin Owns You All!'
    
   
    

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health= health
        self.strength= strength

    def attack(self):
        return super().attack()


    def receiveDamage(self, n):
        self.health=self.health - n
        if self.health > 0:
            return 'A Saxon has received '+str(n)+' points of damage'
        else:
            return 'A Saxon has died in combat'

        

    

# War


class War:
    def __init__(self):

        self.vikingArmy=[]
        self.saxonArmy=[]

    def addViking(self, n=Viking):

        self.vikingArmy.append(n)


    def addSaxon(self, n=Saxon):

        self.saxonArmy.append(n)

    
    def vikingAttack(self):
        # random object in list
        id= random.randint (0, len(self.saxonArmy))  
        x= self.saxonArmy[id]
        
        Saxon.receiveDamage(self, n)
        
        

    def saxonAttack():

    def showStatus():

pass