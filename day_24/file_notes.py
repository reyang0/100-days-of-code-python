# ------------------------------------------------ #
# need to close the file at the end

file = open("my_file.txt") # default: read-only mode
contents = file.read()
print(contents)
file.close()


# ------------------------------------------------ #
# no longer need to remember to close the file

with open("my_file.txt") as file: # default: read-only mode
	contents = file.read()
	print(contents)

# ------------------------------------------------ #

# mode="w" : write
# rewrites entire file = deletes old text and writes new text
with open("my_file.txt", mode="w") as file:
	file.write("New text.")

# mode="a" : append
# adds to the file and does not delete old text
with open("my_file.txt", mode="a") as file:
	file.write("\nNew text.")

# if file does not exist and in write mode, then a new file is created
with open("my_file.txt", mode="w") as file:
	file.write("New text.")
	