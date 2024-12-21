rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

str_choice = ["Rock","Paper","Scissors"]
vis = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
user_str_choice = str_choice[user_choice]
print(vis[user_choice])

computer_choice = random.randint(0,2)
computer_str_choice = str_choice[computer_choice]
print("Computer chose: ")
print(vis[computer_choice])

if user_choice == computer_choice:
    print("It's a draw.")
elif user_str_choice == "Rock":
    if computer_str_choice == "Paper":
        print("Computer wins!")
    else:
        print("You win!")
elif user_str_choice == "Paper":
    if computer_str_choice == "Scissors":
        print("Computer wins!")
    else:
        print("You win!")
elif user_str_choice == "Scissors":
    if computer_str_choice == "Rock":
        print("Computer wins!")
    else:
        print("You win!")
