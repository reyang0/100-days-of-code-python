from turtle import Turtle

ALIGNMENT = "center"
SCORE_FONT = ("Courier", 80, "normal")
GAME_OVER_FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.color("white")
		self.penup()
		self.hideturtle()
		self.l_score = 0
		self.r_score = 0
		self.update_scoreboard()

	def update_scoreboard(self):
		self.clear()
		self.goto(-100, 200)
		self.write(self.l_score, align=ALIGNMENT, font=SCORE_FONT)
		self.goto(0, 200)
		self.write(":", align=ALIGNMENT, font=SCORE_FONT)
		self.goto(100, 200)
		self.write(self.r_score, align=ALIGNMENT, font=SCORE_FONT)

	def l_point(self):
		self.l_score += 1
		self.update_scoreboard()

	def r_point(self):
		self.r_score += 1
		self.update_scoreboard()

	def game_over(self):
		self.goto(0,0)
		self.write("GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)
		self.goto(0,-30)
		if self.l_score > self.r_score:
			winner = "Left"
		else:
			winner = "Right"
		self.write(f"{winner} player wins!", align=ALIGNMENT, font=GAME_OVER_FONT)



