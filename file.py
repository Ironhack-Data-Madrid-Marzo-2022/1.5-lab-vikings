from unicodedata import name
from vikingsClasses import Viking, Saxon, War
from random import randint

def war():
    n_vikings = int(input('Enter the number of vikings: ') )
    n_saxons = int(input('Enter the number of saxons: ') )

    war = War()

    # Add vikings and saxons
    for _ in range(n_vikings):
        war.addViking(Viking(name = 'Pepe', health = 20, strength= 200))
    for _ in range(n_saxons):
        war.addSaxon(Saxon(health = 10, strength= 100))
    

    # Define random battle
    def battle(war):
        """Fights a random battle."""
        
        who_attacks = 'Viking' if randint(0, 1) == 1 else 'Saxon'
        if who_attacks == 'Viking':
            print(f'A {who_attacks} is attacking!')
            war.vikingAttack()
        else:
            print(f'A {who_attacks} is attacking!')
            war.saxonAttack()
        print(war.showStatus())
                     
    while len(war.vikingArmy) > 0 and len(war.saxonArmy) > 0:
        battle(war)

if __name__ == "__main__":
    war()