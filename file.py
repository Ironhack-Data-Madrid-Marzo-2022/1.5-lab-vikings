from vikingsClasses import Saxon, Viking, War

battle = War()



vdic = [Viking('George',5,5),Viking('Steve',6,6),Viking('Michael',7,7)]

battle.addViking(vdic[0])
battle.addViking(vdic[1])
battle.addViking(vdic[2])











sdic = [Saxon(20,20),Saxon(40,40),Saxon(60,60)]

battle.addSaxon(sdic[0])
battle.addSaxon(sdic[1])
battle.addSaxon(sdic[2])

battle.vikingAttack()
battle.saxonAttack()

print(battle.showStatus())


