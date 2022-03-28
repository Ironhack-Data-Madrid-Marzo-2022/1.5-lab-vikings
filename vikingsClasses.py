
# Soldier


class Soldier():
    def __init__(self, health, strength):

            self.health = health

            self.strength = strength

    def attack(self):

            return self.strength

    def receiveDamage(self, damage):

        self.health -= damage


# Viking

class Viking(Soldier): # de soldier
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

    def battleCry(self):

        return "Odin Owns You All!"



# Saxon


class Saxon(Soldier): # de soldier

        def __init__(self, health, strength):

            self.health = health

            self.strength = strength

        def receiveDamage(self, damage):

            self.health -= damage

            if self.health <= 0:

                return " A saxon has died in combat"

            else:

                return f"A Saxon has received {damage} points of damage"

# War


class War:
    pass
