
# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -=damage


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

'''
War
Now we get to the good stuff: WAR!
Our War constructor function will allow us to have a Viking army and a Saxon army that battle each other.

Modify the War constructor and add 5 methods to its prototype:

x addViking()
x addSaxon()
x vikingAttack()
x saxonAttack()
x showStatus()


constructor function
x When we first create a War, the armies should be empty. We will add soldiers to the armies later.

x should receive 0 arguments
x should assign an empty array to the vikingArmy property
x should assign an empty array to the saxonArmy property
x addViking() method
x Adds 1 Viking to the vikingArmy. If you want a 10 Viking army, you need to call this 10 times.

x should be a function
x should receive 1 argument (a Viking object)
x should add the received Viking to the army
x shouldn't return anything
addSaxon() method
The Saxon version of addViking().

should be a function
should receive 1 argument (a Saxon object)
should add the received Saxon to the army
shouldn't return anything
vikingAttack() method
A Saxon (chosen at random) has their receiveDamage() method called with the damage equal to the strength of a Viking (also chosen at random). This should only perform a single attack and the Saxon doesn't get to attack back.

should be a function
should receive 0 arguments
should make a Saxon receiveDamage() equal to the strength of a Viking
should remove dead saxons from the army
should return result of calling receiveDamage() of a Saxon with the strength of a Viking
saxonAttack() method
The Saxon version of vikingAttack(). A Viking receives the damage equal to the strength of a Saxon.

should be a function
should receive 0 arguments
should make a Viking receiveDamage() equal to the strength of a Saxon
should remove dead vikings from the army
should return result of calling receiveDamage() of a Viking with the strength of a Saxon
showStatus() method
Returns the current status of the War based on the size of the armies.

should be a function
should receive 0 arguments
if the Saxon array is empty, should return "Vikings have won the war of the century!"
if the Viking array is empty, should return "Saxons have fought for their lives and survive another day..."
if there are at least 1 Viking and 1 Saxon, should return "Vikings and Saxons are still in the thick of battle."
'''

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self):
        pass

    def vikingAttack(self):
        pass

    def saxonAttack(self):
        pass

    def showStatus(self):
        pass
