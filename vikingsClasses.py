import random


# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage


# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return self.name + " has received " + str(damage) + " points of damage"
        else:
            return self.name + " has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"


# Saxon
class Saxon(Soldier):
    def __init(self, health, strength):
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return "A Saxon has received " + str(damage) + " points of damage"
        else:
            return "A Saxon has died in combat"


# War
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        if len(self.vikingArmy) > 0 and len(self.saxonArmy) > 0:
            idxSaxon = random.randint(0, len(self.saxonArmy) - 1)
            idxViking = random.randint(0, len(self.vikingArmy) - 1)
            viking = self.vikingArmy[idxViking]
            saxon = self.saxonArmy[idxSaxon]
            result = saxon.receiveDamage(viking.attack())
            self.saxonArmy.pop(idxSaxon)
            return result

    def saxonAttack(self):
        if len(self.vikingArmy) > 0 and len(self.saxonArmy) > 0:
            idxSaxon = random.randint(0, len(self.saxonArmy) - 1)
            idxViking = random.randint(0, len(self.vikingArmy) - 1)
            viking = self.vikingArmy[idxViking]
            saxon = self.saxonArmy[idxSaxon]
            result = viking.receiveDamage(saxon.attack())
            self.vikingArmy.pop(idxViking)
            return result

    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
