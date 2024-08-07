#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")

bill = float(input("How much was the bill? $"))
tip_percent = int(input("How much was the tip in percent? "))
people = int(input("How many people will split the bill? "))
per_person = (bill / people) * (1+tip_percent/100)

print(f"Each person should pay : ${per_person:.2f}")
