
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


class War:
    vikingArmy=[]
    saxonArmy=[]
    def addViking(vik):
        vikingArmy+=vik
    def addSaxon(sax):
        saxonArmy+=sax
    def vikingAttack():
        Saxon.receiveDamage(Viking.attack())
    def saxonAttack()
    def showStatus()


   
   


