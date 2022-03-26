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

        Soldier.__init__(self, health, strength)

    def receiveDamage(self, damage):
        self.health -= damage

        if self.health > 0:
            info = self.name + " has received " + str(damage) + " points of damage"
            return info
        else:
            info = self.name + " has died in act of combat"
            return info

    def battleCry(self):
        return "Odin Owns You All!"


# Saxon


class Saxon(Soldier):

    def __init__(self, health, strength):

        Soldier.__init__(self, health, strength)

    def receiveDamage(self, damage):
        self.health -= damage

        if self.health > 0:
            info = "A Saxon has received " + str(damage) + " points of damage"
            return info
        else:
            info = "A Saxon has died in combat"
            return info

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

        index_saxon = random.randint(0, len(self.saxonArmy) - 1)
        id_saxon = self.saxonArmy[index_saxon]

        index_viking = random.randint(0, len(self.vikingArmy) - 1)
        id_viking = self.vikingArmy[index_viking]

        damage = id_viking.strength
        life_saxon = id_saxon.receiveDamage(damage)


        if id_saxon.health <= 0:
            self.saxonArmy.pop(index_saxon)
            return life_saxon
        else:
            return life_saxon


    def saxonAttack(self):

        index_saxon = random.randint(0, len(self.saxonArmy) - 1)
        id_saxon = self.saxonArmy[index_saxon]

        index_viking = random.randint(0, len(self.vikingArmy) - 1)
        id_viking = self.vikingArmy[index_viking]

        damage = id_saxon.strength
        life_viking = id_viking.receiveDamage(damage)


        if id_viking.health <= 0:
            self.vikingArmy.pop(index_viking)
            return life_viking
        else:
            return life_viking

    def showStatus(self):

        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"

        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."

        else:
            return "Vikings and Saxons are still in the thick of battle."


