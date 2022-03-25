import random
# Soldier


class Soldier:

    def __init__(self, health, strength):
    	self.health = health
    	self.strength = strength
    	
    def attack(self):
    	return self.strength
    	
    def receiveDamage(self, damage):
    	self.health -= damage
    

# Viking


class Viking(Soldier):
    
    def __init__(self, name, health, strength):
    
    	self.name = name
    	Soldier.__init__(self, health, strength)
    	
    def attack(self):
    	return self.strength
    	
    def receiveDamage(self, damage):
    
    	self.health -= damage
    	
    	if self.health <= 0:
    		a = self.name + ' has died in act of combat'
    		return a
    		
    	else:
    		danio = str(damage)
    		a = self.name + ' has received ' + danio + ' points of damage'
    		return a
    		
    def battleCry(self):
    	return 'Odin Owns You All!'
	

# Saxon


class Saxon(Soldier):

    def __init__(self, health, strength):

    	Soldier.__init__(self, health, strength)
    	
    def attack(self):
    	return self.strength
    	
    def receiveDamage(self, damage):
    
    	self.health -= damage
    	
    	if self.health <= 0:
    		return 'A Saxon has died in combat'
    		
    	else:
    		danio = str(damage)
    		return 'A Saxon has received ' + danio + ' points of damage'

# War


class War:

    def __init__(self):
    
    	self.vikingArmy = []
    	self.saxonArmy = []
    	
    	
    	
    def addViking(self, Viking):
    	self.vikingArmy.append(Viking)
    	
    	
    	
    def addSaxon(self, Saxon):
    	self.saxonArmy.append(Saxon)
    	
    	
    	
    def vikingAttack(self):
    
    	i = random.randint(0, len(self.vikingArmy)-1)
    	
    	vik = self.vikingArmy[i]
    	
    	damage = vik.strength
    	
    	j = random.randint(0, len(self.vikingArmy)-1)
    	
    	sax = self.saxonArmy[j]
    	
    	if sax.receiveDamage(damage) == 'A Saxon has died in combat':
    			self.saxonArmy.pop(j)
    			
    	if sax.health <= 0:
    		return 'A Saxon has died in combat'
    		
    	else:
    		return 'A Saxon has received ' + str(damage) + ' points of damage'
    				
    	
    	
    	
    
    def saxonAttack(self):
    
    	i = random.randint(0, len(self.saxonArmy)-1)
    	
    	sax = self.saxonArmy[i]
    	
    	damage = sax.strength
    	
    	j = random.randint(0, len(self.vikingArmy)-1)
    	
    	vik = self.vikingArmy[j]
    
    	if vik.receiveDamage(damage) == vik.name + ' has died in act of combat':
    			self.vikingArmy.pop(j)
    			
    	if vik.health <= 0:
    		a = vik.name + ' has died in act of combat'
    		return a
    		
    	else:
    		danio = str(damage)
    		a = vik.name + ' has received ' + danio + ' points of damage'
    		return a
    	
    def showStatus(self):
    	
    	if not self.vikingArmy:
    		
    		return 'Saxons have fought for their lives and survive another day...'
    		
    	elif not self.saxonArmy:
    	
    		return 'Vikings have won the war of the century!'
    	
    	else:
    		return 'Vikings and Saxons are still in the thick of battle.'
    	
    	
    	
    	
    	
    	
    	
    	
