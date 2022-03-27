
from vikingsClasses import *

#Guerra de ser fitness vs ser gordito

#donde la vida es cuanto toma tu cuerpo para llegar a ser gordo o flaco
#str es las ganas que tienes para entrenar o comer

#definimos los guerrors donde los saxones son los guerrero fitness y los vikingos son las cosas que comemos y engordamos y comida para adelgazar
war= War()



s_list=[Saxon(250, 99),
Saxon(98, 37), 
Saxon(173, 87), 
Saxon(150, 48)]

#Creating saxon army
for i in s_list:
    war.addSaxon(i)




fitness_list= [Viking('classes_de_spinning', 100, 100),
Viking('classes_de_cross_fit', 60,150),
Viking('ensalada', 70, 80),
Viking('maraton', 50, 200)]

#Create viking army
for i in fitness_list:
    war.addViking(i)

def battle():
    while war.vikingArmy or war.saxonArmy:
        war.vikingAttack
        war.saxonAttack
    else: return war.showStatus()

print(war)








