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

    def addViking(self, warrior):

        self.vikingArmy.append(warrior)

    def addSaxon(self, warrior):

        self.saxonArmy.append(warrior)

    def vikingAttack(self):

        v = random.choice(self.vikingArmy)

        s = random.choice(self.saxonArmy)

        if(s.self.health==v.self.strength): self.saxonArmy.remove(s)

        return s.receiveDamage(v.self.strength)

    def saxonAttack(self):

        v = random.choice(self.vikingArmy)

        s = random.choice(self.saxonArmy)

        if(v.self.health==s.self.strength): self.vikingArmy.remove(v)

        return v.receiveDamage(s.self.strength)

    def showStatus(self):

        if(self.saxonArmy==[]): 



    
