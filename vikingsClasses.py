from audioop import add
from os import lseek
from pickle import FALSE, TRUE
import random
from tkinter import N


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

    def addViking (self, v) :
        
        self.vikingArmy.append(v)


    def addSaxon(self, s):
        
        self.saxonArmy.append(s)

    
    def vikingAttack(self):
        # random object in list of saxon
        id_s= random.randint (0, len(self.saxonArmy)-1)
        # have to call an object in viking list to attack also
        id_v= random.randint(0, len(self.vikingArmy)-1)  
        r_saxon= self.saxonArmy[id_s]
        r_viking= self.vikingArmy[id_v]
        #calculate the damage and ouyt put the result
        dmg= r_viking.strength
        r= r_saxon.receiveDamage(dmg)
        if r_saxon.health <= 0:
            self.saxonArmy.pop(id_s)
        return r


    def saxonAttack(self):

        id_s= random.randint(0, len(self.vikingArmy)-1)
        id_v= random.randint (0, len(self.saxonArmy)-1)
        r_saxon= self.saxonArmy[id_s]
        r_viking= self.vikingArmy[id_v]

        dmg= r_saxon.strength
        r= r_viking.receiveDamage(dmg)
        if r_viking.health <= 0:
            self.vikingArmy.pop(id_v)

        return r




    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) >= 1 and len(self.vikingArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."
