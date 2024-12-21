from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

power_on = True

this_coffee_maker = CoffeeMaker()
this_money_maker = MoneyMachine()
this_menu = Menu()

while power_on:

	order = input(f"What would you like? ({this_menu.get_items}): ")		# 1. Prompt user

	if order == "off": 														# 2. Turn off the Coffee Machine
		power_on = False

	elif order == "report": 												# 3. Print report
		this_coffee_maker.report()
		this_money_maker.report()

	else:
		this_drink = this_menu.find_drink(order)
		if this_drink is not None:
			if this_coffee_maker.is_resource_sufficient(this_drink): 		# 4. Check resources sufficient
				#this_money_maker.process_coins() 							# 5. Process coins (done in make_payment)
				if this_money_maker.make_payment(this_drink.cost): 			# 6. Check transction successful
					this_coffee_maker.make_coffee(this_drink) 				# 7. Make Coffee








