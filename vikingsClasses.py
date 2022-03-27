
# Soldier


class Soldier:
    
    def __init__(self, health, strength):

        self.health = health
        self.strength = strength
        

    def attack(self):

        return self.strength

    def receiveDamage(self,damage):

        self.health = self.health - damage 





    
    

# Viking


import random 

class Viking(Soldier):

    def __init__(self, name, health, strength):

        self.name = name
        self.health = health
        self.strength = strength

    def receiveDamage(self,damage):

        self.health = self.health - damage

        if self.health > 0:

            return str(self.name) + ' has received ' +  str(damage) +   ' points of damage'

        else:

            return str(self.name) + ' has died in act of combat'

    def battleCry(self):

        return ('Odin Owns You All!')



    

# Saxon


class Saxon(Soldier):

    def __init__(self, health, strength):

        self.health = health
        self.strength = strength

    def receiveDamage(self,damage):

        self.health = self.health - damage

        if self.health > 0:

            return 'A Saxon has received ' +  str(damage) +  ' points of damage'

        else:

            return 'A Saxon has died in combat'

    



# War


class War():

    def __init__(self):

        self.vikingArmy = []

        self.saxonArmy = []

    def addViking(self, viking):

        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):

        self.saxonArmy.append(saxon)

    def vikingAttack(self):                 

        saxon = self.saxonArmy[random.randint(0,len(self.saxonArmy)-1)]

        viking = self.vikingArmy[random.randint(0,len(self.vikingArmy)-1)]

        x = saxon.receiveDamage(viking.strength)

        if saxon.health<1: self.saxonArmy.remove(saxon)

        return x

    def saxonAttack(self):

        saxon = self.saxonArmy[random.randint(0,len(self.saxonArmy)-1)]

        viking = self.vikingArmy[random.randint(0,len(self.vikingArmy)-1)]

        x = viking.receiveDamage(saxon.strength)

        if viking.health<1: self.vikingArmy.remove(viking)

        return x

    def showStatus(self):

        if len(self.saxonArmy)<1: return 'Vikings have won the war of the century!'

        elif len(self.vikingArmy)<1: return 'Saxons have fought for their lives and survive another day...'

        else: return 'Vikings and Saxons are still in the thick of battle.'

    pass
