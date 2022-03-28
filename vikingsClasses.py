
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
        
    def receiveDamage(self, damage):
        self.health = self.health - damage
        
# Viking


class Viking (Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        
        Soldier.__init__(self, health, strength)
        
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health -damage
        
        if self.health > 0:
            return self.name + ' has received ' + str(damage) + ' points of damage'
        else:
            return self.name + ' has died in act of combat'
    
    def battleCry(self):
    	return 'Odin Owns You All!'
        

# Saxon


class Saxon (Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
        Soldier.__init__(self, health, strength)
        
    def attack(self):
      return self.strength
  
    def receiveDamage(self, damage):
        self.health -= damage
        
        if self.health > 0:
            return 'A Saxon has received ' + str(damage) + ' points of damage'
        else:
            return 'A Saxon has died in combat'
    

# War

import random

class War:
    def __init__(self, vikingArmy, saxonArmy):
        self.vikingArmy = []
        self.saxonArmy = []
        
    def addViking(self, viking):
        self.vikingArmy.append(viking)
        
    def addSaxon(self, viking):
        self.saxonArmy.append(viking)
         
        viking = self.vikingArmy[random.radint(0, len(self.vikingArmy) -1)]
      
        damageSaxon = saxon.receiveDamage(viking.strength)

        if saxon.health <1 : self.saxonArmy.pop(saxon)

        return damageSaxon
        
        
        if viking.health < 1: self.vikingArmy.remove(viking)
    def vikingAttack(self):                 

        saxon = self.saxonArmy[random.randint(0, len(self.saxonArmy) -1)]
        viking = self.vikingArmy[random.randint(0, len(self.vikingArmy) -1)]

        damageSaxon = saxon.receiveDamage(viking.strength)
        if saxon.health <1 : self.saxonArmy.pop(damageSaxon)
        return damageSaxon

    def saxonAttack(self):

        saxon = self.saxonArmy[random.randint(0, len(self.saxonArmy) -1)]
        viking = self.vikingArmy[random.randint(0, len(self.vikingArmy) -1)]

        damageViking = viking.receiveDamage(saxon.strength)
        if viking.health <1: self.vikingArmy.pop(damageViking)
        return damageViking
    
    def showStatus(self):

        if len(self.saxonArmy) < 1: 
            return 'Vikings have won the war of the century!'

        elif len(self.vikingArmy) < 1:
            return 'Saxons have fought for their lives and survive another day...'

        else: return 'Vikings and Saxons are still in the thick of battle.'
