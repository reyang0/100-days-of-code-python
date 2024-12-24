# ------------------------------------------------------------ #
# Project: Snake Game
# ------------------------------------------------------------ #
# Part 1:
# 1. Create a snake body
# 2. Move the snake
# 3. Control the snake with keyboard
# ------------------------------------------------------------ #
# Part 2:
# 4. Detect collision with food
# 5. Create a scoreboard
# 6. Detect collision with wall
# 7. Detect collision with tail
# ------------------------------------------------------------ #
# Module: Turtle
# ------------------------------------------------------------ #
# https://docs.python.org/3/library/turtle.html
# ------------------------------------------------------------ #

from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
# 0 - east - right
# 90 - north - up
# 180 - west - left
# 270 - south - down
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:

	# - - - - - - - - - - - - - - - - - -
	# 1. Create a snake body
	# - - - - - - - - - - - - - - - - - -

	def __init__(self):
		self.segments = []
		self.create_snake()
		self.head=self.segments[0]

	def create_snake(self):
		for position in STARTING_POSITIONS:
			self.add_segment(position)

	def add_segment(self, position):
		segment = Turtle("square")
		segment.color("white")
		segment.penup()
		segment.goto(position)
		self.segments.append(segment)

	def extend(self):
		# append new segment with last segment in last segment's position
		self.add_segments(self.segments[-1].position())

	# - - - - - - - - - - - - - - - - - -
	# 2. Move the snake
	# - - - - - - - - - - - - - - - - - -

	def move(self):
		for i in range(len(self.segments)-1,0,-1):
			self.segments[i].goto(self.segments[i-1].position())
		self.head.forward(MOVE_DISTANCE)

	# - - - - - - - - - - - - - - - - - -
	# 3. Control the snake with keyboard
	# - - - - - - - - - - - - - - - - - -

	# 0 - east - right
	# 90 - north - up
	# 180 - west - left
	# 270 - south - down

	def up(self):
		if self.head.heading() != DOWN:
			self.head.setheading(UP)

	def down(self):
		if self.head.heading() != UP:
			self.head.setheading(DOWN)

	def left(self):
		if self.head.heading() != RIGHT:
			self.head.setheading(LEFT)

	def right(self):
		if self.head.heading() != LEFT:
			self.head.setheading(RIGHT)






