
# Soldier


class Soldier:
    def __init__(self,health,strength):
        self.health=health
        self.strength=strength
    def receiveDamage(self,damage):
        self.health=self.health-damage
    def attack(self):
        return self.strength
            


# Viking


class Viking(Soldier):
    def __init__(self,name,strength,health):
        Soldier.__init__(self,strength,health)
        self.name=name
    def receiveDamage(self,damage):
        self.health=self.health-damage
        if self.health>0:
            return str(self.name)+' has received '+ str(damage) +' points of damage'
        else:
            return str(self.name)+' has died in act of combat'

    def battleCry(self):
            return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self,strength,health):
        Soldier.__init__(self,strength,health)
    def receiveDamage(self,damage):

            self.health=self.health-damage
            if self.health>0:
                return 'A Saxon has received '+ str(damage) +' points of damage'
            else:
                return 'A Saxon has died in combat'

    


    pass

# War
import random
class War:
    
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        saxon=random.choice(self.saxonArmy)
        viking=random.choice(self.vikingArmy)
        v_dam=saxon.receiveDamage(viking.strength)
        if saxon.health <=0:
            self.saxonArmy.pop(self.saxonArmy.index(saxon))
        return v_dam


    
    def saxonAttack(self):
        saxon=random.choice(self.saxonArmy)
        viking=random.choice(self.vikingArmy)
        s_dam=viking.receiveDamage(saxon.strength)
        if viking.health <=0:
            self.vikingArmy.pop(self.vikingArmy.index(viking))
        return s_dam
        

    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return print('Vikings have won the war of the century!')
        elif len(self.vikingArmy) == 0:
            return print('Saxons have fought for their lives and survive another day...')
        else:
            return print("Vikings and Saxons are still in the thick of battle.")


   
   


