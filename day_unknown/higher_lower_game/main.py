# https://replit.com/@appbrewery/higher-lower-start?v=1#main.py

from art import logo
from art import vs
from game_data import data

import os
import random

# random.randint(a,b) = return random int between a and b (inclusive)

# ------------------------------------------------------------------------------------ # 

def clear_terminal():
    """Clears the terminal screen."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and macOS
        os.system('clear')
    print(logo)

# ------------------------------------------------------------------------------------ #

def game_v1():
	score = 0
	a_index = -1 # not yet selected
	b_index = -1 # not yet selected
	play = True

	while play:
		
		clear_terminal()

		# assign A
		if a_index == -1:
			a_index = random.randint(0,len(data)-1) 
		else:
			a_index = b_index

		# assign B
		while a_index == b_index:
			b_index = random.randint(0,len(data)-1)

		print(f"Compare A: {data[a_index]['name']}, a {data[a_index]['description']}, from {data[a_index]['country']}")
		print(vs)
		print(f"Against B: {data[b_index]['name']}, a {data[b_index]['description']}, from {data[b_index]['country']}")
		ans = input("Who has more followers? Type 'A' or 'B': ")

		# check if player is correct
		if ans == "A":
			if data[a_index]['follower_count'] > data[b_index]['follower_count']:
				score += 1
				print(f"You're right! Current score: {score}.")
			else:
				clear_terminal()
				play = False
				print(f"Sorry, you're wrong. Final score: {score}.")
		elif ans == "B":
			if data[b_index]['follower_count'] > data[a_index]['follower_count']:
				score += 1
				print(f"You're right! Current score: {score}.")
			else:
				clear_terminal()
				play = False
				print(f"Sorry, you're wrong. Final score: {score}.")

# ------------------------------------------------------------------------------------ #

def game_v2():
	score = 0
	play = True
	choice_a = {}
	choice_b = {}

	while play:
		
		clear_terminal()
		if score > 0:
			print(f"You're right! Current score: {score}")

		# assign A
		if len(choice_a) == 0:
			choice_a = random.choice(data)
		else:
			choice_a = choice_b

		# assign B
		while len(choice_b) == 0 or choice_a == choice_b:
			choice_b = random.choice(data)

		print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}")
		print(vs)
		print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}")
		ans = input("Who has more followers? Type 'A' or 'B': ")

		# check if player is correct
		if ans == "A":
			if choice_a['follower_count'] > choice_b['follower_count']:
				score += 1
			else:
				play = False
		elif ans == "B":
			if choice_b['follower_count'] > choice_a['follower_count']:
				score += 1
			else:
				play = False

	clear_terminal()
	print(f"Sorry, you're wrong. Final score: {score}")

# ------------------------------------------------------------------------------------ #

play = True

while play:
	game_v2()
	if input("\nWant to play again? (y/n) ") != 'y':
		play = False

print("Thanks for playing!\n")





