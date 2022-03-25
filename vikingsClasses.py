import random

class Soldier:

    def __init__(self, health, strength):

        self.health = health
        
        self.strength = strength

    def attack(self):
        
        return self.strength

    def receiveDamage(self, damage = 0):

        self.health -= damage

class Viking(Soldier):

    def __init__(self, name = '', health = '', strength = ''):

        self.name = name
        
        Soldier.__init__(self, health, strength)

    def receiveDamage(self, damage = 0):

        self.health -= damage

        if(self.health<=0): return self.name + ' has died in act of combat'

        else: return self.name + ' has received ' + str(damage) + ' points of damage'
    
    def battleCry(self):

        return 'Odin Owns You All!'

class Saxon(Soldier):

    def __init__(self, health = '', strength = ''):

        Soldier.__init__(self, health, strength)

    def receiveDamage(self, damage=0):

        self.health -= damage

        if(self.health<=0): return 'A Saxon has died in combat'

        else: return 'A Saxon has received ' + str(damage) + ' points of damage'
    
class War:

    def __init__(self):

        self.vikingArmy = []

        self.saxonArmy = []

    def addViking(self, viking):

        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):

        self.saxonArmy.append(saxon)

    def vikingAttack(self):

        v1 = self.vikingArmy[random.randint(0, len(self.vikingArmy)-1)]

        s1 = self.saxonArmy[random.randint(0, len(self.saxonArmy)-1)]

        dam1 = s1.receiveDamage(v1.strength)

        if(s1.health==v1.strength): self.saxonArmy.remove(s1)

        return dam1

    def saxonAttack(self):

        v2 = self.vikingArmy[random.randint(0, len(self.vikingArmy)-1)]

        s2 = self.saxonArmy[random.randint(0, len(self.saxonArmy)-1)]

        dam2 = v2.receiveDamage(s2.strength)

        if(v2.health==s2.strength): self.vikingArmy.remove(v2)

        return dam2

    def showStatus(self):

        if not self.saxonArmy: return 'Vikings have won the war of the century!'

        elif not self.vikingArmy: return 'Saxons have fought for their lives and survive another day...'

        elif(len(self.saxonArmy)==1 or len(self.vikingArmy)==1): return 'Vikings and Saxons are still in the thick of battle.'



    
