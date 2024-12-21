#####Turtle Intro######

import turtle as t
import random

timmy = t.Turtle()
#timmy.shape("turtle")
#timmy.color("red")
#timmy.forward(100)
#timmy.backward(200)
#timmy.right(90)
#timmy.left(180)
#timmy.setheading(0)

# ----------------------------------------------------- #
######## Challenge 1 - Draw a Square ############
# ----------------------------------------------------- #

def draw_a_square():
	timmy.pensize(1) # default size
	timmy.speed(1) # default speed
	for _ in range(4):
		timmy.forward(100) 	# 100 steps
		timmy.left(90) 		# turn 90 degress

# draw_a_dashed_line()

# ----------------------------------------------------- #
######## Challenge 2 - Draw a Dashed Line ############
# ----------------------------------------------------- #

def draw_a_dashed_line(length, dash_length):
	timmy.pensize(1) # default size
	timmy.speed(1) # default speed
	for _ in range(length // (2 * dash_length)):
		timmy.forward(dash_length)
		timmy.penup()
		timmy.forward(dash_length)
		timmy.pendown()

#draw_a_dashed_line(200, 10)

# ----------------------------------------------------- #
######## Challenge 3 - Draw Different Shapes ############
# ----------------------------------------------------- #

# each shape is a random color
# each side length = 100

# triangle: 03 sides
# square: 	04 sides
# pentagon: 05 sides
# hexagon: 	06 sides
# heptagon: 07 sides
# octagon: 	08 sides
# nonagon: 	09 sides
# decagon: 	10 sides

def get_random_color():
	t.colormode(255) # Set the color mode to 255 to use RGB values
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	return (r, g, b)

def draw_shape(length, sides):
	for _ in range(sides):
		timmy.forward(length)
		timmy.right(360/sides)

def draw_different_shapes():
	timmy.pensize(1) # default size
	timmy.speed(1) # default speed
	for i in range(3,11):
		timmy.color(get_random_color())
		draw_shape(100,i)

#draw_different_shapes()

# ----------------------------------------------------- #
######## Challenge 4 - Draw a Random Walk ############
# ----------------------------------------------------- #

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#timmy.color(random.choice(colors))

moves = ["left", "right", "forward", "back"]

def random_walk(length, steps):
	timmy.speed(10) # change speed to 10
	timmy.pensize(10) # change size to 10
	for _ in range(steps):
		move_choice = random.choice(moves)
		timmy.color(random.choice(colors))
		if move_choice == "left":
			timmy.left(90)
		elif move_choice == "right":
			timmy.right(90)
		elif move_choice == "forward":
			timmy.forward(length)
		else:
			timmy.back(length)

#random_walk(25,200)

# ----------------------------------------------------- #
######## Challenge 4 - Draw a Spirograph ############
# ----------------------------------------------------- #

# radius = radius of circles
# count = number of circles
def draw_a_spirograph(radius, count):
	timmy.pensize(1) # default size
	timmy.speed("fastest")
	for _ in range(count):
		timmy.color(get_random_color())
		timmy.circle(radius)
		timmy.left(360/count)

draw_a_spirograph(100,50)

# ----------------------------------------------------- #
# Keep screen open
# ----------------------------------------------------- #

screen = t.Screen()
screen.exitonclick()












