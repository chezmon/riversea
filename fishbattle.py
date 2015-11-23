
import random

class Enemy:
	
	kind = 'fish'
	names = ['Salmon', 'Bass', 'Dory','Flathead', 'Angler', 'Hammerhead Shark']
	attacks = ['Tail Swipe', 'Bite', 'Guard']
	
	def __init__(self, health):
		self.health = health
		self.health_max = 10
		
	def displayAttacks(self):
		return("{}".format(self.attacks))

	def displayName(self):
		ey = random.choice(Enemy.names)
		return("{}".format(ey))

	def displayState(self):
		return("{0.health}/{0.health_max}\n".format(self))

	def attack(self):
		random_attack = random.choice(self.attacks)
		return(random_attack)


class Player:
	def __init__(self, name, health):
		
		self.name = name
		self.health = health
		self.health_max = 10

	def displayState(self):
		return("{0.health}/{0.health_max}\n".format(self))

def battle(player, enemy):
	if player == enemy:
		return('draw')
	elif (player=='Tail Swipe' and enemy=='Guard') or (player=='Bite' and enemy=='Tail Swipe') or (player=='Guard' and enemy=='Bite'):
		return('player')
	else:
		return('enemy')

def modify_phealth(health, who_won):
	new_health = health
	if who_won == 'player':
		new_health += 1
		return new_health
	elif who_won == 'enemy':
		new_health -= 1
		return new_health
	else:
		return new_health

def modify_ehealth(health, who_won):
	e_health = health
	if who_won=='player':
		e_health -= 1
		return e_health
	else: 
		return e_health

def play(name):
	health_ = 10
	health_e = 10
	b = Enemy(health_)


	while health_>0 and health_e>0:
		#get player attack
		a = input("-->")
		playa = Player(a,health_e)
		if a in Enemy.attacks:

			# get random attack from enemy
			e = b.attack()

			# determines who wins: returns tie, player, enemy 
			who_wins = battle(a, e)

			# change player health
			health_a=modify_phealth(health_, who_wins)

			# update health to changed player health
			health_=health_a

			# change enemy health
			if modify_ehealth:
				health_ee = modify_ehealth(health_e, who_wins)
				health_e = health_ee

			print("\nYou {}! \n The other fish is a {} and they {}! \n ************* \n".format(a, b.displayName(), e))
			print("\nHealth now: {}/{}\n".format(health_, playa.health_max))
			print("\nEnemy's health: {}/{}\n".format(health_e,b.health_max))

		else:
			print("\nSorry what?\n")
			

nama = input("What name?\n")
print("\nsup {}?\n Please choose only 'Tail Swipe', 'Bite', Guard'.\n".format(nama))
play(nama)
print("\nGame over!\n\n")
