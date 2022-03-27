
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

        self.vikingArmy= []
        self.saxonArmy= []

    def addViking(self,viking):

        self.vikingArmy.append(viking)

    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):

       indv=random.randint(0,len(self.vikingArmy)-1)
       inds=random.randint(0,len(self.saxonArmy)-1)

       vik=self.vikingArmy[indv]
       saj=self.saxonArmy[inds]

       attack_size=vik.strength
       result=saj.receiveDamage(attack_size)

       if saj.health <=0:


           self.saxonArmy.pop(inds)

       return result


        
    def saxonAttack(self):

       indv=random.randint(0,len(self.vikingArmy)-1)
       inds=random.randint(0,len(self.saxonArmy)-1)

       vik=self.vikingArmy[indv]
       saj=self.saxonArmy[inds]

       attack_size=saj.strength


       vik.receiveDamage(saj.strength)
       result=vik.receiveDamage(attack_size)

       if vik.health <=0:

           self.vikingArmy.pop(indv)


       return result


    def showStatus(self):

        if len(self.saxonArmy)== 0:
            return "Vikings have won the war of the century!"

        elif len== 0:
            return "Saxons have fought for their lives and survive another day..."
 

        elif len(self.saxonArmy)>=1 and len(self.vikingArmy)>=1:

            return "Vikings and Saxons are still in the thick of battle."












        

        

        


















