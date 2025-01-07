# --------------------------------------------------------------------------- #
# Error Handling
# --------------------------------------------------------------------------- #

try: 
	#attempt to execute this piece of code
	#example: try to open this file
	file = open("example.txt") #FileNotFoundError
	ex_dict = {"key": "value"}
	print(ex_dict["qwerty"]) #KeyError

except FileNotFoundError:
	#run this block if there was an error
	#example: in write mode, this will create the file
	file = open("example.txt", "w")

except KeyError as error_message:
	print(f"That key {error_message} does not exist.")

else: 
	#do this piece of code if there were no errors
	content = file.read()

finally: 
	#do this no matter what happens
	#file.close()
	raise TypeError("This is an error that I made up.") #raise an exception


# --------------------------------------------------------------------------- #
# Coding Exericse 20: IndexError Handling
# --------------------------------------------------------------------------- #

# Description:
# We've got some buggy code. Try running the code. The code will crash and give you an IndexError.
# This is because we're looking through the list of fruits for an index that is out of range. 

# Objective:
# Use what you've learnt about exception handling to prevent the program from crashing. 
# If the user enters something that is out of range just print a default output of "Fruit pie". 

# IMPORTANT: 
# The exception handling should NOT allow each fruit to be printed when there is an exception. 
# e.g. it should not print out Apple pie, Pear pie and Orange pie, when there is an exception 
# it should only print "Fruit pie". 

fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        fruit = fruits[index]
        print(fruit + " pie")

make_pie(4)

# --------------------------------------------------------------------------- #
# Coding Exericse 21: KeyError Handling
# --------------------------------------------------------------------------- #

# Description:
# We've got some buggy code, try running the code. The code will crash and give you a KeyError.
# This is because some of the posts in the facebook_posts don't have any "Likes". 

# Objective:
# Use what you've learnt about exception handling to prevent the program from crashing. 

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

def count_likes(posts):

    total_likes = 0
    for post in posts:
        try:
            like = post['Likes']
        except KeyError:
            like = 0
        else:
            like = post['Likes']
        total_likes = total_likes + like
    
    return total_likes

count_likes(facebook_posts)

# --------------------------------------------------------------------------- #
# NATO Alphabet Challenge
# --------------------------------------------------------------------------- #

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter:row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        result = [data_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else 
        print(result)

generate_phonetic()

# --------------------------------------------------------------------------- #
# JSON
# --------------------------------------------------------------------------- #

json.dump()     # write
json.load()     # read
json.update()   # update









