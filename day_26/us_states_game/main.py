# -------------------------------------------------------------------------------------------------- #
# Setup
# -------------------------------------------------------------------------------------------------- #

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

# -------------------------------------------------------------------------------------------------- #
# Solution 2 (Udemy)
# -------------------------------------------------------------------------------------------------- #

all_states = data.state.to_list()
guessed_states = []

answer_state = screen.textinput(title=updated_title, 
								prompt="What's another state's name?").title()

if answer_state == "Exit":
	# original 
	#missing_states = []
	#for states in all_states:
	#	if state not in guessed_states:
	#		missing_states.append(state)
	
	# simplification (list comprehension)
	missing_states = [state for state in all_states if state not in guessed_states]

	new_data = pandas.DataFrame(missing_states)
	new_data.to_csv("states_to_learn.csv")
	break # end while loop prematurely

if answer_state in all_states:
	if answer_state not in guessed_states: 		# added to avoid double counting states
		guessed_states.append(answer_state)
		t = turtle.Turtle()
		t.hideturtle()
		t.penup()
		state_data = data[data.state == answer_state]
		t.goto(state_data.x.item(), state_data.y.item())
		t.write(answer_state)

# -------------------------------------------------------------------------------------------------- #

screen.exitonclick()