
# Soldier


class Soldier:

    def __init__(self, health, strength):

        self.health=health
        self.strength=strength
        

    def attack(self):
        
        return self.strength

    def receiveDamage(self,damage):

        self.health-=damage




# Viking


class Viking(Soldier):

    def __init__(self,name, health, strength):

        self.name=name

        Soldier.__init__(self,health,strength)
        
    def receiveDamage(self,damage):

        self.health -=damage

        if self.health>0:

            return str(self.name) + " has received " + str(damage) + " points of damage"

        if self.health<=0:

            return str(self.name) + " has died in combat"

    def battleCry(self):
        
        return ("Odin Owns You All!")

      

# Saxon


class Saxon(Soldier):

    def __init__(self,health, strength):

        Soldier.__init__(self,health,strength)

    def receiveDamage(self,damage):

        self.health -=damage

        if self.health>0:

            return "A Saxon has received " + str(damage) + " points of damage"

        if self.health<=0:

            return "A Saxon has died in combat"



# War

import random
class War:

    def __init__(self):

        self.vikingArmy=[]
        self.saxonArmy=[]

    def addViking(self,Viking):

        self.vikingArmy.append(Viking)

    def addSaxon(self,Saxon):

        self.saxonArmy.append(Saxon)

    def vikingAttack(self):

       indv=random.randint(0,len(self.vikingArmy)-1)
       inds=random.randint(0,len(self.saxonArmy)-1)

       vik=self.vikingArmy[indv]
       saj=self.saxonArmy[inds]

       saj.receiveDamage(vik.strength)

       if saj.health <=0:

           self.saxonArmy.pop(saj)

    
       return (saj.receiveDamage(vik.strength))

         

       

    def saxonAttack(self):

       indv=random.randint(0,len(self.vikingArmy)-1)
       inds=random.randint(0,len(self.saxonArmy)-1)

       vik=self.vikingArmy[indv]
       saj=self.saxonArmy[inds]

       vik.receiveDamage(saj.strength)

       if vik.health <=0:

           self.vikingArmy.pop(vik)

       return vik.receiveDamage(saj.strength)











        

        

        



