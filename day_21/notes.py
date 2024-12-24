# -------------------------------- #
# Class Inheritance
# -------------------------------- #

class Animal:
	def __init__(self):
		self.num_eyes = 2

	def breathe(self):
		print("Inhale, exhale.")

class Fish(Animal): # inherit another class
	def __init__(self):
		super().__init__()

	def breathe(self): # create custom method on top of superclass
		super().breathe()
		print("Doing this underwater.")

	def swim(self):
		print("Moving in water.")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

# -------------------------------- #
# Slicing
# -------------------------------- #

piano_keys = ["a", "b", "c", "d", "e", "f", "g"] 	# start at index 0
print(piano_keys[2:5]) 								# print index 2 to 5
print(piano_keys[4:]) 								# print index 4 to last
print(piano_keys[:2]) 								# print start to 2
print(piano_keys[2::2]) 							# print index 2 to last by 2 asc
print(piano_keys[::-1]) 							# print last to start by 1 desc

