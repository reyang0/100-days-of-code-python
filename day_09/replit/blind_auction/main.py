from replit import clear
#HINT: You can call clear() to clear the output in the console.

import art

print(art.logo)

more_bids = "yes"
bids_dict = {}
while more_bids == "yes":
  name = input("What is your name? ")
  bid = int(float(input("What is your bid? $")))
  bids_dict[name] = bid
  more_bids = input("Are there any other bidders? Type 'yes or 'no'.\n\t").lower()
  if more_bids == "yes":
    clear()

highest_bid = 0
highest_person = ""
for name in bids_dict:
  if bids_dict[name] > highest_bid:
    highest_bid = bids_dict[name]
    highest_person = name

print(f"The winner is {highest_person} with a bid of ${highest_bid}")
