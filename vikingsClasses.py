
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
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):

        self.health -= damage

        if self.health <=0:

            return f"{name} has died in act of combat"

        else:
            return f"{name}has received {damage} points of damage"

    def battleCry():


# Saxon


class Saxon:
    pass

# War


class War:
    pass
