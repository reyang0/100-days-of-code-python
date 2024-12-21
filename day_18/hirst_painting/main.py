# ------------------------------------------------------------------------------ #
# extract color schema from Hirst painting
# ------------------------------------------------------------------------------ #

import colorgram

# Extract colors from an image
colors = colorgram.extract('image.jpg', 10)  # Extract the top 10 colors

# Get the RGB values
rgb_colors = []
for color in colors:
    rgb = color.rgb  # Get the RGB object
    rgb_colors.append((rgb.r, rgb.g, rgb.b))  # Append the RGB tuple to the list

# Print the RGB values
#print(rgb_colors)

# ------------------------------------------------------------------------------ #
# draw randomized spot painting
# ------------------------------------------------------------------------------ #

# Requirements:
# (1) 10 x 10 spots
# (2) circles size = 20
# (3) circle distinct apart = 50


import turtle as t
import random

# Set up the turtle
timmy = t.Turtle()
timmy.speed("fastest")
t.colormode(255) # Set the color mode to 255 to use RGB values

# Set up the screen
screen = t.Screen()
screen.setup(width=600, height=600) # (0,0) is the center of the window

def draw_circle(circle_size):
	timmy.pendown()
	timmy.color(random.choice(rgb_colors))
	timmy.begin_fill()
	timmy.circle(circle_size)
	timmy.end_fill()

def draw_space(space_size):
	timmy.penup()
	timmy.forward(space_size)

def start_new_row(y_coordinate):
	timmy.penup()
	timmy.goto(-250,y_coordinate)
	timmy.pendown()

def draw_row(y_coordinate, circle_size, circle_count, space_size):
	start_new_row(y_coordinate)
	for _ in range(circle_count):
		draw_circle(circle_size)
		draw_space(space_size)

def draw_hirst_painting(circle_size, circle_count, space_size):
	for i in range(0,circle_count):
		draw_row(-250+(i*space_size), circle_size, circle_count, space_size)

circle_size = 20
circle_count = 10
space_size = 50

draw_hirst_painting(circle_size, circle_count, space_size)

screen.exitonclick()







