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
# Solution 1 (Me)
# -------------------------------------------------------------------------------------------------- #

# create new column in dataframe to track correct state answers
# note: cannot create new column with data.correct = 0
data["correct"] = 0 

label = turtle.Turtle()
label.hideturtle()
label.penup()

while (data.correct == 0).any():
	if sum(data["correct"]) == 0:
		answer_state = screen.textinput(title="Guess the State",
										prompt="What's a state's name?")
	else:
		updated_title = f"{sum(data["correct"])}/{len(data["correct"])} States Correct"
		answer_state = screen.textinput(title=updated_title,
										prompt="What's another state's name?")

	match = data["state"].str.contains(answer_state, case=False) # ignore case sensitivity
	state_data = data[match]

	if answer_state.lower() == "exit":
		missing_states = data[data.correct == 0].state
		new_data = pandas.DataFrame(missing_states)
		new_data.to_csv("states_to_learn.csv")
		break # end while loop prematurely

	if not state_data.empty:
		state_name = state_data.state.item()
		state_xcor = state_data.x.item()
		state_ycor = state_data.y.item()
		label.goto(state_xcor, state_ycor)
		label.write(state_name)
		data.loc[data.state == state_name, "correct"] = 1

# -------------------------------------------------------------------------------------------------- #
# Solution 2 (Udemy)
# -------------------------------------------------------------------------------------------------- #

#all_states = data.state.to_list()
#guessed_states = []

#answer_state = screen.textinput(title=updated_title, 
#								prompt="What's another state's name?").title()

#if answer_state == "Exit":
#	missing_states = []
#	for states in all_states:
#		if state not in guessed_states:
#			missing_states.append(state)
#	new_data = pandas.DataFrame(missing_states)
#	new_data.to_csv("states_to_learn.csv")
#	break # end while loop prematurely

#if answer_state in all_states:
#	if answer_state not in guessed_states: 		# added to avoid double counting states
#		guessed_states.append(answer_state)
#		t = turtle.Turtle()
#		t.hideturtle()
#		t.penup()
#		state_data = data[data.state == answer_state]
#		t.goto(state_data.x.item(), state_data.y.item())
#		t.write(answer_state)

# -------------------------------------------------------------------------------------------------- #

screen.exitonclick()