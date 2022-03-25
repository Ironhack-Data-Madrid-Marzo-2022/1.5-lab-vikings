
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


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking(self,Viking):
        self.Viking=Viking
        self.vikingArmy.append(Viking)
    def addSaxon(self,Saxon):
        self.Saxon=Saxon
        self.saxonArmy.append(Saxon)
    def vikingAttack(self):
        if Saxon.health<0:
            self.saxonArmy.remove(Saxon)
        else:
            return Saxon.receiveDamage
    def saxonAttack(self):
        if Viking.health<0:
            self.vikingArmy.remove(Viking)
        else:
            return Viking.receiveDamage
    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    pass
