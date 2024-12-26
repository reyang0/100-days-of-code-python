# ------------------------------------------------------------ #
# Project: Pong Game
# ------------------------------------------------------------ #
# 1. Create the screen
# 2. Create and move a paddle
# 3. Create another paddle
# 4. Create the ball and make it move
# 5. Detect collision with wall and bounce
# 6. Detect collision with paddle
# 7. Detect when paddle misses
# 8. Keep score
# ------------------------------------------------------------ #

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0) # turn off animation

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
scoreboard = Scoreboard()
max_points = 5

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
	time.sleep(ball.move_speed) # slower ball movement
	screen.update()
	ball.move()

	# Detect collision with top/bottom walls
	if abs(ball.ycor()) > 280:
		ball.bounce_y()

	# Detect collision with right paddle:
	collision_right = ball.distance(r_paddle) < 50 and ball.xcor() > 320
	collision_left = ball.distance(l_paddle) < 50 and ball.xcor() < -320
	if collision_right or collision_left:
		ball.bounce_x()

	# Detect R paddle misses
	if ball.xcor() > 380:
		ball.refresh()
		scoreboard.l_point()

	# Detect L paddle misses
	if ball.xcor() < -380:
		ball.refresh()
		scoreboard.r_point()

	if scoreboard.l_score == max_points or scoreboard.r_score == max_points:
		game_is_on = False
		scoreboard.game_over()

screen.exitonclick()







