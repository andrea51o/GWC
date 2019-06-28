#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing: print(aRandomNumber)

guess = input("Guess a number between 1 and 20 (inclusive):")
if not guess.isnumeric(): # checks if a string is only digits 0 to 9
	print("That's not a positive whole number, try again!")
else:
	guess = int(guess) # converts a string to an integer
	guesses = 0
while guesses < 3:
	guess = int(input("Guess a random number between 1 and 20:"))
	print('random number')
	print(aRandomNumber)
	if guesses == aRandomNumber:
		print("Success")
  	if guess > aRandomNumber:
		print("Guess lower!")
	if guess < aRandomNumber:
		print("Guess higher!")
	guesses+= 1
	print(guesses)
