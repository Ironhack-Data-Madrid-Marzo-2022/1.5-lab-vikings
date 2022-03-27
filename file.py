from vikingsClasses import *
vikingos=[Viking('Ragnar',3,3),Viking('Loki',3,3)]
sajones=[Saxon(2,2),Saxon(2,2)]
for e in vikingos:
    War.addViking(e)
for e in sajones:
    War.addSaxon(e)

while len(vikingos)!=0 or len(sajones)!=0:
    War.vikingAttack()
    War.saxonAttack()
War.showStatus()