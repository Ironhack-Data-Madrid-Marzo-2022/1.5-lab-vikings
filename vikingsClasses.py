
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
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)
    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)
    def vikingAttack(self):
        saxons = self.saxonArmy
        saxons = random.randint(0,len(self.saxonArmy)-1)
        if saxons.health<0:
            saxons.remove(saxons)
        else:
            return Saxon.receiveDamage
    def saxonAttack(self):
        vikings = self.vikingArmy
        vikings = random.randint(0,len(self.vikingArmy)-1)
        if vikings.health<0:
            vikings.remove(vikings)
        else:
            return Viking.receiveDamage
    def showStatus(self):
        if saxons == []:
            return "Vikings have won the war of the century!"
        elif vikings == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    pass
