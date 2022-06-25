import Get_Cards
import Card_Modules
menu = Card_Modules.menu
generateCard = Get_Cards.generateCard
doWork = Card_Modules.doWork
goodbye = Card_Modules.goodbye
showAll = Card_Modules.showAll

while True:
	inpt = int(menu())
	if (inpt == 1):
		doWork()
	elif (inpt == 2):
		showAll()
	elif (inpt == 3):
		goodbye()
		exit()
	else: 
		print("That wasn't an option, try again...")