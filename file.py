from vikingsClasses import Saxon, Viking, War

battle = War()

print('Create your viking army: ')

vlist = []

for i in range(3):

    name = input('Enter name: ')

    health = int(input('Enter health: '))

    strength = int(input('Enter strength: '))

    vlist.append(Viking(name,health,strength))

    battle.addViking(vlist[i])

print('Create your saxon army: ')

slist = []

for i in range(3):

    health = int(input('Enter health: '))

    strength = int(input('Enter strength: '))

    slist.append(Saxon(health,strength))

    battle.addSaxon(slist[i])

battle.vikingAttack
battle.saxonAttack
battle.vikingAttack
battle.saxonAttack
battle.vikingAttack
battle.saxonAttack

print('The result of 3 rounds. A soldier attack on another one for round:')
print(battle.showStatus())