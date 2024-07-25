'''
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
- Equal to or over 18.5 but below 25 they have a normal weight
- Equal to or over 25 but below 30 they are slightly overweight
- Equal to or over 30 but below 35 they are obese
- Equal to or over 35 they are clinically obese.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
BMI = weight / (height * height)

Important: you do not need to round the result to the nearest whole number. 
It's fine to print out a floating point number for this exercise. 
The interpretation message needs to include the words from the interpretations above. 
e.g. underweight, normal weight, overweight, obese, clinically obese.
'''

# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight/(height**2)

if bmi >= 35:
  print(f"Your BMI is {bmi}, you are clinically obese.")
elif bmi >= 30:
  print(f"Your BMI is {bmi}, you are obese.")
elif bmi >= 25:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi >= 18.5:
  print(f"Your BMI is {bmi}, you have a normal weight.")
else:
  print(f"Your BMI is {bmi}, you are underweight.")
  


