#########################
#						            #
#    Ikan Adventures    #
# 			          			#
#########################

def welcome():
	print("***********************************************\n")
	print("Welcome to Ikan Adventure!\n")
	print("Bloop bloop. You are an Ikan. What do you want to be called?\n")
	
def player_():
	print("A group of sardine lurks and decides to attack you. Please choose Tail Swipe, Bite or Guard! \n")
	a = input ('-->')
	if(a=="Tail Swipe"):
		print("You've chosen to swipe that muthafucka!\n")
		
	elif(a=="Bite"):
		print("\nCHOMP! Jaws of steel! \n")
	elif(a=="Guard"):
		print("*clink!* You're a toughie! But we'll see if it works\n")
	else:
		print("Tail Swipe, Bite or Guard?\n")
		player_()
		
	return a

def compo():
	from random import randint
	x = randint(1,3)
	if(x==1):
		return "Tail Swipe"
	elif(x==2):
		return "Bite"
	elif(x==3):
		return "Guard"

def outcome(com,pla):
	if(com==pla):
		return "Stalemate"
	elif(com)
welcome()
z = comp_()
p = player_()
print("The group of sardines are going to {} {}!\n".format(z,p))

'''while hp!=0:
	meet_a_fish()
	fight()
	who_wins()'''
