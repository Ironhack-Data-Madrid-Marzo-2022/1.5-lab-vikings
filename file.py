from vikingsClasses import *

vikings = [
    Viking('Erik', 100, 100),
    Viking('Thor', 100, 100),
    Viking('Harald', 100, 100),
    Viking('Helge', 100, 100),
    Viking('Loki', 100, 100)
]

saxons = [
    Saxon(100, 100),
    Saxon(100, 100),
    Saxon(100, 100),
    Saxon(100, 100),
    Saxon(100, 100)
]

war = War()

for e in vikings:
    war.addViking(e)

for e in saxons:
    war.addSaxon(e)

while war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    war.saxonAttack()
    war.vikingAttack()
    war.showStatus()

print(war.showStatus())





