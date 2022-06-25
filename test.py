
def menu():
	while (True):
		print("1. Option 1")
		print("2. Option 2")
		print("3. exit")

		ans = input("choose an option")
		if ans == '1':
			print("in option 1")
		elif ans == '2':
			print("in option 2")
		elif ans == '3':
			break
		else:
			print("Unknown option")

menu()