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
        super().__init__(health, strength)
        self.name = name
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'{self.name} has received {str(damage)} points of damage'
        else:
            return f'{self.name} has died in act of combat'

    def battleCry(self):
        return 'Odin Owns You All!'

# Saxon


class Saxon(Soldier):
    
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'A Saxon has received {str(damage)} points of damage'
        else:
            return f'A Saxon has died in combat'


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
        # Select random viking and saxon
        i_viking = random.randint(0, len(self.vikingArmy) - 1)
        i_saxon = random.randint(0, len(self.saxonArmy) - 1)

        viking = self.vikingArmy[i_viking]
        saxon = self.saxonArmy[i_saxon]

        # Calculate and apply damage
        damage = viking.strength
        result = saxon.receiveDamage(damage)

        # Remove saxon if he dies
        if saxon.health <= 0:
            self.saxonArmy.pop(i_saxon)
        
        return result
    
    def saxonAttack(self):
        # Select random viking and saxon
        i_viking = random.randint(0, len(self.vikingArmy) - 1)
        i_saxon = random.randint(0, len(self.saxonArmy) - 1)

        viking = self.vikingArmy[i_viking]
        saxon = self.saxonArmy[i_saxon]

        # Calculate and apply damage
        damage = saxon.strength
        result = viking.receiveDamage(damage)

        # Remove viking if he dies
        if viking.health <= 0:
            self.vikingArmy.pop(i_viking)
        return result
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return 'Vikings have won the war of the century!'
        elif len(self.vikingArmy) == 0:
            return 'Saxons have fought for their lives and survive another day...'
        else:
            return "Vikings and Saxons are still in the thick of battle."