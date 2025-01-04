from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
	global reps
	reps = 0
	window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():

	global reps
	reps += 1

	work_sec = WORK_MIN * 60
	short_break_sec = SHORT_BREAK_MIN * 60
	long_break_sec = LONG_BREAK_MIN * 60

	# rep 1 = 25min work
	# rep 2 = 5min break
	# rep 3 = 25min work
	# rep 4 = 5min break
	# rep 5 = 25min work
	# rep 6 = 5min break
	# rep 7 = 25min work
	# rep 8 = 20min break

	if reps % 2 == 1: 								# odd reps (1,3,5,7)
		timer_label.config(text="Work", fg=GREEN)
		countdown(work_sec)
	elif reps != 8:									# even reps excl 8 (2,4,6)
		timer_label.config(text="Break", fg=PINK)
		countdown(short_break_sec)
	else: 											# rep 8
		timer_label.config(text="Break", fg=RED)
		countdown(long_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(n_sec):
	mins = math.floor(n_sec / 60)
	secs = n_sec % 60
	canvas.itemconfig(timer_text, text=f"{mins:02}:{secs:02}")
	if n_sec > 0:
		global timer
		timer = window.after(1000, countdown, n_sec-1) # 1000 miliseconds = 1 second
	else:
		start_timer()
		marks = "" # marks of work sessions
		for _ in range(math.floor(reps/2)):
			marks += "✔"
		check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro") # "Tomato" in Italian
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", highlightthickness=0, highlightbackground=YELLOW, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0, highlightbackground=YELLOW, command=reset_timer)
reset_btn.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()

# - - - - - - - #
# Button Issue  #
# - - - - - - - #
# highlightthickness=0: this did not help with the border issue on a mac
# highlightbackground=YELLOW: this was the solution found