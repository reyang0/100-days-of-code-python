from turtle import Turtle

START_SPEED = 0.1

class Ball(Turtle):

	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.color("white")
		self.penup()
		self.x_move = 10
		self.y_move = 10
		self.move_speed = START_SPEED

	def move(self):
		new_xcor = self.xcor() + self.x_move
		new_ycor = self.ycor() + self.y_move
		self.goto(new_xcor, new_ycor)

	def bounce_y(self):
		self.y_move *= -1

	def bounce_x(self):
		self.x_move *= -1
		self.move_speed *= 0.9 # make game more challenging over time

	def refresh(self):
		self.goto(0,0)
		self.move_speed = START_SPEED
		self.bounce_x()






