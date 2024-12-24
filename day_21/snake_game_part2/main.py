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

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # turn off animation

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
	screen.update()
	time.sleep(0.1)
	
	snake.move()

	# - - - - - - - - - - - - - - - - - #
	# Detect collision with food
	# - - - - - - - - - - - - - - - - - #
	if snake.head.distance(food) < 15:
		food.refresh()
		snake.extend()
		scoreboard.increase_score()

	# - - - - - - - - - - - - - - - - - #
	# Detect collision with wall
	# - - - - - - - - - - - - - - - - - #
	if snake.head.xcor() > abs(280) or nake.head.ycor() > abs(280):
		game_is_on = False
		scoreboard.game_over()

	# - - - - - - - - - - - - - - - - - #
	# Detect collision with tail
	# - - - - - - - - - - - - - - - - - #
	# Solution 1: w/o slicing
	#for segment in snake.segments:
	#	if segment != snake.head:
	#		if snake.head.distance(segment) < 10:
	#			game_is_on = False
	#			scoreboard.game_over()
	# Solution 2: w/ slicing
	for segment in snake.segments[1:]:
		if snake.head.distance(segment) < 10:
			game_is_on = False
			scoreboard.game_over()

screen.exitonclick()












