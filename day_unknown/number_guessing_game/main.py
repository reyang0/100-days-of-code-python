
import os
import random

# ------------------------------------------------------------------------------------ # 

def clear_terminal():
    """Clears the terminal screen."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and macOS
        os.system('clear')

# ------------------------------------------------------------------------------------ #

def game():
	clear_terminal()
	print("Welcome to the Number Guessing Game!")	
	print("I'm thinking of a number between 1 and 100.")
	solution = random.randint(1,100) # a random integer between 1 and 10 (inclusive)

	# assign how many attempts user receives based on difficulty
	difficulty=''
	while difficulty != 'easy' and difficulty != 'hard':
		difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
		if difficulty == 'easy':
			attempts_left = 10
			print(f"(HINT: The number is {solution}.)")
		elif difficulty == 'hard':
			attempts_left = 5
		else:
			print("ERROR: That difficulty is not available. Please try again.")

	solved = False
	while attempts_left > 0:
		print(f"\nYou have {attempts_left} attempts remaining to guess the number.")
		guess = int(input("Make a guess: "))
		if guess == solution:
			solved = True
			attempts_left = 0 # end the game
		elif guess < solution:
			print("Too low.\nGuess again.")
		elif guess > solution:
			print("Too high.\nGuess again.")
		attempts_left -= 1 # decrement by one

	if solved == True:
		print(f"\nYou got it! The number is {solution}.")
	else:
		print("You've run out of guesses, you lose.")

# ------------------------------------------------------------------------------------ #

play = True

while play:
	game()
	if input("\nWant to play again? (y/n) ") != 'y':
		play = False

print("Thanks for playing!")





