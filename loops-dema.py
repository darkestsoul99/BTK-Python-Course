from random import randint

while input() is not "e": 
	hak = 5 
	number = randint(1,100) 
	guess = input("Guess the number between 1-100")
	if guess > 1 and guess < 100:
		if guess < number:
			print("yukarı")
			hak -= 1 

		elif guess > number:
			print("aşağı")
			hak -= 1  

		elif guess == number:
			print("You knew the number!! Congrats!!")

		if hak == 0:
			print("You've lost! Try again.")
			hak = 5 

	else:
		print("Please enter a valid number!")