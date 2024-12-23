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
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # turn off animation

# - - - - - - - - - - - - - - - - - -
# 1. Create a snake body
# - - - - - - - - - - - - - - - - - -

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# - - - - - - - - - - - - - - - - - -
# 2. Move the snake
# - - - - - - - - - - - - - - - - - -

game_is_on = True

while game_is_on:
	screen.update()
	time.sleep(0.1)

	# - - - - - - - - - - - - - - - - - -
	# 3. Control the snake with keyboard
	# - - - - - - - - - - - - - - - - - -
	
	snake.move()
	



screen.exitonclick()