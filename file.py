from vikingsClasses import *
vikingos=[Viking('Ragnar',2,2),Viking('Loki',2,2)]
sajones=[Saxon(3,3),Saxon(3,3)]
w=War()
for e in vikingos:
    w.addViking(e)
for e in sajones:
    w.addSaxon(e)
print(w.vikingArmy)
print(w.saxonArmy)

while len(w.vikingArmy)!=0 and len(w.saxonArmy)!=0:
    print('inicial')
    w.vikingAttack()
    w.saxonAttack()
    print(w.vikingArmy)
    print(w.saxonArmy)
    print('final')
    w.showStatus()
    if len(w.vikingArmy)==0 or len(w.saxonArmy)==0:
        break
    