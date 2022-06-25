import Get_Cards
import os
import webbrowser
import itertools

generateCard = Get_Cards.generateCard
getAllCards = Get_Cards.getAllCards


# prints the main menu
def menu():
	ftrlength = showHeader("Menu")
	print("1: Practice with Cards")
	print("2: Get All Cards")
	print("3: Exit\n")
	showFooter(ftrlength)
	result = input(f"\n{C.B}What would you like to do?{C.E} ")
	return(result)


# closes the program
def goodbye():
	os.system('cls')
	print("See You Later!")
	


# calls the generate random card function from "Get_Cards" and passes the single choice
# back with both the question and answer and prints it to the screen
def doWork():
	while True:
		qt, ans = generateCard()
		ftrlength = showHeader("Flash Cards")
		print(f"{C.BOLD}{qt}{C.E}\n")
		print(f"{C.Y}press 's' to skip.{C.E}\n")
		showFooter(ftrlength)
		inpt = input(f"\n{C.B}Press any key to see the answer. (press e to exit){C.E}")
		#if 'e', exit
		if (inpt == 'e'):
			return
		#if not 's', show answer
		elif (inpt != 's'):
			showHeader("Flash Cards")
			print(qt + "\n")
			webbrowser.open(ans)
			showFooter(ftrlength)
			inpt = input(f"\n{C.B}Press any key to see the next card. (press e to exit){C.E}")
			if (str(inpt) == "e"):
				return
		

# Gets all the cards in a list, passes them in and prints them. For choosing specific
# cards to study
def showAll():
	while True:
		ftrlength = showHeader("Showing All Entries")
		# for counting entries
		x = 1
		qt, ans = getAllCards()
		ttl_cards = len(qt)
		for row in qt:
			print(str(x) + ": " + row)
			x = x + 1
		print("\n")	
		showFooter(ftrlength)
		inpt1 = input(f"{C.B}\nWhat function would you like to study?: (press e to exit) {C.E}")
		
		#try,except statement to catch if users put a charactor other then 'e' in
		try:
			if inpt1 == "e":
				return
			#elif to catch if user puts a number outside options in
			elif int(inpt1) < 1 or int(inpt1) > ttl_cards:
				input("That wasn't an option, try again....")
			else:
				inpt1 = int(inpt1) - 1
				webbrowser.open(ans[inpt1])
		except:
			input("That wasn't an option, try again....")


# passes in a string var with the header text, 
# counts it's characters so that it can compute the header length and then prints it.
def showHeader(header):
	lgth = len(header)
	lgth = int(lgth) + 22
	os.system('cls')
	print(f"{C.B}-" * lgth)
	print("---------- " + header + " ----------")
	print(f"{C.B}-{C.E}" * lgth + "\n")
	return lgth

#takes the lgth of the header and adds a footer to the bottom of the card.
def showFooter(lgth):
	print(f"{C.B}-{C.E}" * lgth)
	print(f"{C.B}-{C.E}" * lgth)
	print(f"{C.B}-{C.E}" * lgth)
	return

# Class used to format the prints in color
class C:
    H = '\033[95m'
    B = '\033[94m'
    C = '\033[96m'
    G = '\033[92m'
    Y = '\033[93m'
    R = '\033[91m'
    E = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

