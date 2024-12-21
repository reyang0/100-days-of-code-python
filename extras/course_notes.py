'''
---------------------------------------------------------------------------------

-------------
Tools
-------------

	Replit
		https://replit.com/@reyang0/day-1-printing-start
	Auditorium
		https://app.auditorium.ai/

-------------
Data Type
-------------

	Strings = characters ("") ('')
	Integer = whole number (1, 2, 3, ...)
	Float   = decimal number (1.0, 2.0, 3.0, ...)
	Boolean = True or False

-------------
Functions
-------------

	Console:
		print(str)           = print out in console
		input()              = prompting user for an input (output=string)

	Data Type:
		type(var)            = <class 'type'> for variable
		str(var)             = converts var to a string
		int(var)             = converts var to an integer
		float(var)           = converts var to a float

	String:
		len(str)             = int length of string
		str[i]               = substring at index i (starting at 0)
		str1+str2            = concatenation
		"\n"                 = new line
		"\""                 = double quote (")
		'"'                  = double quote (") (can tell between single & double quotes)
		"\t"                 = tab
		
	Integer/Float:
		a +  b               = addition
		a -  b               = subtraction
		a *  b               = multiplication
		a /  b               = division (output=float)
		a // b               = floor division (output=integer)
		a ** b               = power (a^b)
		a %  b               = modulo (=remainder)
		PEMDAS               = power, exponential, multiply/divide, addition/substration
		var += n             = increment var by n
		var -= n             = decrement var by n 

		f"str {var}"         = f-string = convert var to string
		f"{var:.2f}"         = f-string = format var to 2 decimals (output=string)

		format(var,".2f")    = format var to 2 decimals (output=string)
		"{:.2f}".format(var) = format var to 2 decimals (output=string)

	Logical Operators:
		a ==  b              = a is equal to b (a=b is assignment, not the same as ==)
		a !=  b              = a is not equal to b
		a >   b              = a is greater than b
		a >=  b              = a is greater than or equal to b
		a <   b              = a is less than b
		a <=  b              = a is less than order equal to b
		a and b              = a=true and b=true
		a or  b              = a=true or b=true
		not   a              = a=false

	Float:
		round(var,decimal)   = round var to the decimal places

-------------
Statements
-------------

	if condition1:
		do this
	elif condition2:
		do this
	else:
		do this

-------------
Data Structures
-------------

	list = [item1, item2]       = list with brackets where first index begins at 0
	list.append("new_item")     = add new_item to the end of the list
	list.extend([item3, item4]) = add new list to the end of the list
	list = [list1, list2]       = nested list

---------------------------------------------------------------------------------
'''

# ----------------------------------------------- #
# Print/Input
# ----------------------------------------------- #

print("Hello world!")
# Hello world!

print('She said: "Hello" and then left')
# She said: "Hello" and then left

print("She said: \"Hello\" and then left")
# She said: "Hello" and then left

print("Hello world!\nHello world!") # new line
# Hello world!
# Hello world!

print("Hello" + " " + "world!") # concatenate strings
# Hello world!

input("What is your name?") # prompt user for input
# What is your name?____

print("Hello " + input("What is your name?") + "!")
#1. What is your name?____
#2. Hello ____!

user_name = input("What is your name?")

numOfLetters=len("string")
print(numOfLetters) # output: 6

# ----------------------------------------------- #
# Data Types & String Manipulation
# ----------------------------------------------- #

print("string"[4]) # output: "n"
print(123+345)     # output: 468
print("123"+"345") # output: "123345"

print(123)         # output: error

# Note: 734_529.678 = 734529.678 
#       Underscores are a new addition to Python 3.6+ to help visualize larger numbers.

print(type(123)) # output: <class 'int'>

# ----------------------------------------------- #
# Control Flow & Logical Operators
# ----------------------------------------------- #

if condition1:
	#do action1
elif condition2:
	#do action2
else:
	#do this

# ----------------------------------------------- #
# Randomisation & Python Lists
# ----------------------------------------------- #

# ------------------------ #
# What is a module?
# ------------------------ #
# main.py is the file that is run
# main.py can have "import my_module" to access any functions from my_module.py file.
#
# Create a new file = my_module.py
# Any code within my_module.py is a module
# ------------------------ #

# https://pynative.com/python/random/
import random # import random module

random_integer = random.randint(1,10)                  # a random integer between 1 and 10 (inclusive)
random_float = random.random()                         # returns a float between 0.0 and 1.0 (excluding 1.0)
random_float2 = random.randint(1,10) * random.random() # returns a float between 1.0 and 10.0

fruits = [item1, item2] # list

fruits = []
vegetables = []
dirty_dozen = [fruits, vegetables] # nested list

# ----------------------------------------------- #
# Loops
# ----------------------------------------------- #

for item in list_of_items:
	#Do something to each item

for number in range(a,b): # range(a,b) = creating a range between a and b (including a, excluding b)
	print(number)


range(a,b)
range(a,b,c) # range from a (included) to b (excluded) at steps c


numbers_list = []
random.choice(numbers) # select a random choice in the numbers_list
password_list.append(random.choice(numbers)) # append to the password_list

# ----------------------------------------------- #
# Functions, Code Blocks, and While Loops
# ----------------------------------------------- #

# define function
def my_function():
	print("Hello")
	print("Bye")

# execute function
my_function()

# while statement, continue to do what is inside the block
while do_something:

# ------------------------ #
# Dictionary
# ------------------------ #

empty_dict = {}        # empty dictionary (wipe an existing dictionary)

ex_dict = {
	Key1: Value1, 
	Key2: Value2,
}

ex_list = []              # empty list
ex_list = [index]         # accessing a list with index
ex_dict[Key1]             # accessing a dictionary with a key
ex_dict[Key3] = Value3    # add a new key/value pair
print(ex_dict)
#	Key1: Value1, 
#	Key2: Value2,
#	Key3: Value3,

ex_dict[Key2] = New_Value2 # edit an item in a dictionary

for key in ex_dict:
	print(key)          # print key
	print(ex_dict[key]) # print value

# ------------------------ #
# Nesting
# ------------------------ #

nested = {
	Key1: [List], 
	Key2: {Dict},	
}

# ----------------------------------------------- #
# Functions with Outputs
# ----------------------------------------------- #

def function_name():
	'''This is a docstring and appears when this function is called'''
	return True

# ----------------------------------------------- #
# Scopes
# ----------------------------------------------- #

# ------------ #
# Local Scope
# ------------ #

# Example 1
def drink_potion():
	potion_stength = 2 # only accessible within the function
	print(potion_stength)

drink_potion()
print(potion_stength) # NameError: potion_stength not defined

# ------------ #
# Global Scope
# ------------ #
# Based on where variable was created/defined

# Example 2
player_health = 10 # global variable: accessible anywhere within the file

def drink_potion():
	potion_stength = 2 # local variable: only accessible within the function
	print(player_health)

drink_potion()

# ------------------------------------ #
# There is no block scope in Python
# ------------------------------------ #

# Example 3
if 3 > 2:
	a_var = 10 # this variable is treated with global scope

# Example 4
def example_function():
	if 3 > 2:
		b_var = 10 # this variable is treated with local scope to the function

# ------------------------------------ #
# How to access Global variables
# ------------------------------------ #

# Example 5
player_health = 10 # global variable: accessible anywhere within the file

def drink_potion():
	global player_health # now global variable is accessible within the function (not ideal to modify global var in local scope)
	potion_stength = 2   # local variable: only accessible within the function
	print(player_health)

drink_potion()

# best practice: input as param and return value

































