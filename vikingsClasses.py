
# Soldier


from unicodedata import name


class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.health -= damage
        pass

# Viking


class Viking(Soldier):
    def __init__(self,name,health,strength):
        Soldier.__init__(self,health,strength)
        self.name=name
    def attack(self):
        return self.strength
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health >0:
            return self.name + " has received " + str(damage) + " points of damage"
        else:
            return self.name + " has died in act of combat"
    def battleCry(self):
            return "Odin Owns You All!"
    pass

# Saxon


class Saxon(Soldier):
    def __init__(self,health,strength):
        Soldier.__init__(self,health,strength)
    def attack(self):
        return self.strength
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health >0:
            return "A Saxon has received " + str(damage) + " points of damage"
        else:
            return "A Saxon has died in combat"
    pass

# War

import random
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking(self,viking):
        self.vikingArmy.append(viking)
    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)
    def vikingAttack(self):
        saxon = random.randint(0,len(self.saxonArmy)-1)
        saxons = self.saxonArmy[saxon]
        viking = random.randint(0,len(self.vikingArmy)-1)
        vikings = self.vikingArmy[viking]
        damage=vikings.strength
        result_calling = saxons.receiveDamage(damage)
        if saxons.health<=0:
            self.saxonArmy.pop(saxon)
        return result_calling
    def saxonAttack(self): #mismo que antes reemplazando donde corresponde
        saxon = random.randint(0,len(self.saxonArmy)-1)
        saxons = self.saxonArmy[saxon]
        viking = random.randint(0,len(self.vikingArmy)-1)
        vikings = self.vikingArmy[viking]
        damage=saxons.strength
        result_calling = vikings.receiveDamage(damage)
        if vikings.health<=0:
            self.vikingArmy.pop(viking)
        return result_calling
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    pass
