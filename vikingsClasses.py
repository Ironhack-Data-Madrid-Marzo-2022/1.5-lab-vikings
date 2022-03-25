class Soldier:

    def __init__(self, health, strength):

        self.health = health
        
        self.strength = strength

    def attack(self):
        
        return self.strength

    def receiveDamage(self, damage = 0):

        self.health -= damage

class Viking(Soldier):

    def __init__(self, name = '', health = '', strength = ''):

        self.name = name
        
        self.health = health

        self.strength = strength

    def receiveDamage(self, damage = 0):

        self.health -= damage

        if(self.health<=0): return f'{self.name} has died in act of combat'






class Saxon:
    pass



class War:
    pass
