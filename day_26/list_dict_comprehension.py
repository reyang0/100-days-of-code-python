# ------------------------------------------------------------------------------------------- #
# List Comprehension
# ------------------------------------------------------------------------------------------- #

# Old Method
numbers = [1, 2, 3]
new_list = []
for n in list:
	add_1 = n + 1
	new_list.append(add_1)

# New Method 
new_list = [new_item for item in orig_list]
new_list = [new_item for item in orig_list if test]

numbers = [1, 2, 3]						# [1, 2, 3]
new_list = [n + 1 for n in numbers]		# [2, 3, 4]

name = "Angela"							# "Angela"
new_list = [letter for letter in name]	# ['A', 'n', 'g', 'e', 'l', 'a']

orig_list = [n for n in range(1,5)]		# [1, 2, 3, 4]
new_list = [n * 2 for n in range(1,5)]	# [2, 4, 6, 8]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
long_names = [name for name in names if len(name) >= 5]

# - - - - - - - - - - - - - - - - - - - - - -  #
# Exercise 15: Squaring Numbers
# - - - - - - - - - - - - - - - - - - - - - -  #

# You are going to write a List Comprehension to create a new list called squared_numbers.
# This new list should contain every number in the list numbers but each number should be squared. 
# DO NOT modify the List numbers directly. Try to use List Comprehension instead of a Loop. 

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n * n for n in numbers]
print(squared_numbers)

# - - - - - - - - - - - - - - - - - - - - - -  #
# Exercise 16: Filtering Even Numbers
# - - - - - - - - - - - - - - - - - - - - - -  #

# In this list comprehension exercise you will practice using list comprehension to filter out 
# the even numbers from a series of numbers.   

# Use list comprehension to convert the list_of_strings to a list of integers called numbers.   
# Then use list comprehension again to create a new list called result.
# This new list should only contain the even numbers from the list numbers. 

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(n) for n in list_of_strings]
result = [n for n in numbers if n % 2 == 0]
print(result)

# - - - - - - - - - - - - - - - - - - - - - -  #
# Exercise 17: Data Overlap
# - - - - - - - - - - - - - - - - - - - - - -  #

# Take a look inside file1.txt and file2.txt.
# They each contain a bunch of numbers, each number on a new line. 

# You are going to create a list called result which contains the numbers that are common in
# both files. 

with open("file1.txt") as file1:
	file1_data = file1.readlines()
with open("file2.txt") as file2:
	file2_data = file2.readlines()
result = [int(line.strip()) for line in file1_data if line in file2_data]
print(result)

# ------------------------------------------------------------------------------------------- #
# Dictionary Comprehension
# ------------------------------------------------------------------------------------------- #

# New Method
new_dict = {new_key:new_value for item in list}
new_dict = {new_key:new_value for (key, value) in dict.items()}
new_dict = {new_key:new_value for (key, value) in dict.items() if test}

import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores = {student:random.randint(1,100) for student in names} # random score 1 - 99
passed_students = {student:score for (student, score) in students_scores.items() if score >=60}

# - - - - - - - - - - - - - - - - - - - - - -  #
# Exercise 18: Dictionary Comprehension 1
# - - - - - - - - - - - - - - - - - - - - - -  #

# You are going to use Dictionary Comprehension to create a dictionary called result that takes 
# each word in the given sentence and calculates the number of letters in each word.   

# Try Googling to find out how to convert a sentence into a list of words.
# DO NOT Create a dictionary directly.
# To keep this exercise simple, count any punctuation following a word with no whitespace as 
# part of the word. Note that "Swallow?" therefore has a length of 8.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}

# - - - - - - - - - - - - - - - - - - - - - -  #
# Exercise 19: Dictionary Comprehension 2
# - - - - - - - - - - - - - - - - - - - - - -  #

# You are going to use Dictionary Comprehension to create a dictionary called weather_f that 
# takes each temperature in degrees Celsius and converts it into degrees Fahrenheit. 

# To convert temp_c into temp_f use this formula: (temp_c * 9/5) + 32 = temp_f

# DO NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.


weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:(temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)

# ------------------------------------------------------------------------------------------- #

student_dict = {
	"student": ["Angela", "James", "Lily"],
	"score": [56, 76, 98]
}

# - - - - - - - - - - - - - - #
# Looping through dictionaries
# - - - - - - - - - - - - - - #
#for (key, value) in student_dict.items():
#	print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# - - - - - - - - - - - - - - #
# Loop through data frame
# - - - - - - - - - - - - - - #

# Loop through columns of a data frame
#for (key, value) in student_data_frame.items():
#	print(key)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
	#print(index) 			# print index
	#print(row) 			# print (key,value)
	#print(row.student) 	# print student names
	#print(row.score) 		# print scores
	if row.student == "Angela":
		print(row.score) 	# print only Angela's score



















































