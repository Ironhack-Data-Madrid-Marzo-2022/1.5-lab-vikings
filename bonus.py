from vikingsClasses import *
vikikings =[
    Viking("name1", 10, 10),
    Viking("name2",10, 10),
]

saxons = [
    Saxon(10,10),
    Saxon(10,10),
]

war = War()

for i in vikikings:
    war.addViking(i)

for i in saxons:
    war.addSaxon(i)

while war.showStatus()=="Vikings and Saxons are still in the thick of battle.":
    war.saxonAttack()
    war.vikingAttack()
    war.showStatus()

print(war.showStatus())

