
# ------------------------------------------------------------------------ #

menu = {
	"espresso": {
		"cost": 1.50,
		"ingredients": {
			"water": 50,
			"milk": 0,
			"coffee": 18,
		},
	},
	"latte": {
		"cost": 2.50,
		"ingredients": {
			"water": 200,
			"milk": 250,
			"coffee": 24,
		},
	},
	"cappuccino": {
		"cost": 3.00,
		"ingredients": {
			"water": 250,
			"milk": 100,
			"coffee": 24,
		},
	},
}

resources = {
	"water": 300,
	"milk": 200,
	"coffee": 100,
}

coins = {
	"penny": 0.01,
	"nickel": 0.05,
	"dime": 0.10,
	"quarter": 0.25,
}

balance = 0.0

# ------------------------------------------------------------------------ #

def report():
	print(f"Water: {resources["water"]}ml")
	print(f"Milk: {resources["milk"]}ml")
	print(f"Coffee: {resources["coffee"]}g")
	print(f"Money: ${balance}")

def refill():
	global resources
	resources["water"] = 300
	resources["milk"] = 200
	resources["coffee"] = 100
	print(f"Water: {resources["water"]}ml")
	print(f"Milk: {resources["milk"]}ml")
	print(f"Coffee: {resources["coffee"]}g")
	print("Resources have been refilled.")

def take_order(order):
	if sufficient_resources(order):
		print("Please insert coins.")
		amount = 0.0
		amount += round(coins["quarter"]*int(input("How many quarters?: ")),2)
		amount += round(coins["dime"]*int(input("How many dimes?: ")),2)
		amount += round(coins["nickel"]*int(input("How many nickels?: ")),2)
		amount += round(coins["penny"]*int(input("How many pennies?: ")),2)
		if sufficient_funds(order, amount):
			change = make_drink(order, amount)
			print(f"Here is ${change} in change.")
			print(f"Here is your {order}. Enjoy!")

def make_drink(order, amount):
	# add money to balance
	global balance 
	balance += amount
	# calculate change
	change = round(amount - menu[order]["cost"],2)
	# deduct resources to make drink
	global resources
	resources["water"] -= menu[order]["ingredients"]["water"]
	resources["milk"] -= menu[order]["ingredients"]["milk"]
	resources["coffee"] -= menu[order]["ingredients"]["coffee"]
	return change

def sufficient_funds(order, amount):
	if menu[order]["cost"]>amount:
		print("Sorry that's not enough money. Money refunded.")
		return False
	else:
		return True

def sufficient_resources(order):
	# TO DO: make a forloop to go through all ingredients instead of one-by-one
	if resources["water"]<menu[order]["ingredients"]["water"]:
		print(f"Sorry there is not enough water.")
		return False
	elif resources["milk"]<menu[order]["ingredients"]["milk"]:
		print(f"Sorry there is not enough milk.")
		return False
	elif resources["coffee"]<menu[order]["ingredients"]["coffee"]:
		print(f"Sorry there is not enough coffee.")
		return False
	else:
		return True

# ------------------------------------------------------------------------ #

machine_on = True

while machine_on:
	order = input("What would you like? (espresso/latte/cappuccino): ")
	if order == "report":
		report()
	elif order == "refill":
		refill()
	elif order == "off":
		machine_on = False
	else:
		take_order(order)



