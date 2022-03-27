import random
from vikingsClasses import Viking, Saxon, War

battle = War()

def createVikingArmy():

    print("Let's create a viking army of 10 soldiers.")

    for i in range(10):

        name = input('Enter name: ')

        health = int(input('Enter health: '))

        strength = int(input('Enter strength: '))

        battle.addViking(Viking(name,health,strength))

def createSaxonArmy():

    print("Let's create a saxon army of 10 soldiers.")

    for i in range(10):

        health = int(input('Enter health: '))

        strength = int(input('Enter strength: '))

        battle.addSaxon(Saxon(health,strength))

def startWar(battle):

    x = random.randint(0,1)

    if x==1:
        
        print('Vikings attack!')

        battle.vikingAttack()

    else:

        print('Saxons attack!')

        battle.saxonAttack()

    print(battle.showStatus())

    while len(battle.vikingArmy)>=1 and len(battle.saxonArmy)>=1:

        startWar(battle)

createVikingArmy()

createSaxonArmy()

startWar(battle)

