'''
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:
1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
2. Then check for the number of times the letters in the word LOVE occurs.
3. Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:
"Your score is *x*, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:
"Your score is *y*, you are alright together."

Otherwise, the message will just be their score. e.g.:
"Your score is *z*."

e.g.

name1 = "Angela Yu"
name2 = "Jack Bauer"

T occurs 0 times
R occurs 1 time
U occurs 2 times
E occurs 2 times
Total = 5

L occurs 1 time
O occurs 0 times
V occurs 0 times
E occurs 2 times
Total = 3

Love Score = 53

Print: "Your score is 53."
'''

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

name = name1 + name2
score = 0
score += name.lower().count("t")
score += name.lower().count("r")
score += name.lower().count("u")
score += name.lower().count("e")
score1 = str(score)
score = 0
score += name.lower().count("l")
score += name.lower().count("o")
score += name.lower().count("v")
score += name.lower().count("e")
score2 = str(score)

score = int(score1+score2)
if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
