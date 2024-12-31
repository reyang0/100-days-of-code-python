# ----------------------------------- #
#Arguments with Default Values
# ----------------------------------- #
def my_function(a=1, b=2, c=3):
	#Do this with a
	#Then do this with b
	#Finally do this with c

# ----------------------------------- #
#Unlimited Arguments
# ----------------------------------- #

#fixed arguments
def add_v1(n1, n2):
	return n1 + n2

#args = arguments (type: tuple)
def add_v2(*args):
	result = 0
	for n in args:
		result += n
	return result

#kwargs = keyword arguments (type: dictionary)
def calculate(n, **kwargs):
	#for key, value in kwargs.items():
	#	print(key)
	n += kwargs["add"]
	n *= kwargs["multiply"]

calculate(2, add=3, multiply=5)

# ----------------------------------- #
#class Car
# ----------------------------------- #

class Car:
	def __init__(self, **kw):
		#this will return an error if not provided in initialization
		#self.make = kw["make"]
		#self.model = kw["model"]

		#this will return None if not provided in initialization
		self.make = kw.get("make")
		self.model = kw.get("model")
		self.colour = kw.get("colour")
		self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="GT-R")


