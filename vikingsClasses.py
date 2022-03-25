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

        Soldier.__init__(self,health,strength)

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

    def __init__(self, health, strength):

        Soldier.__init__(self, health, strength)

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

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        idex_saxon = random.randint(0, len(self.saxonArmy) - 1)
        id_saxon = self.saxonArmy[idex_saxon]

        idex_viking = random.randint(0, len(self.vikingArmy) - 1)
        id_viking = self.vikingArmy[idex_viking]

        id_saxon.receiveDamage(id_viking.strength)












        pass
