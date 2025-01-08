from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
	data = pandas.read_csv("data/french_words.csv")

timer = None
french_word = ""

# ----------------------------------- Next Card ----------------------------------- #

def next_card():
	global french_word, timer
	if timer is not None:
		window.after_cancel(timer)
	french_word = choice(data.French)
	canvas.itemconfig(language_text, fill="black", text="French")
	canvas.itemconfig(word_text, fill="black", text=french_word)
	timer = window.after(3000, flip_card) # 3000 miliseconds = 3 second

def flip_card():
	english_word = data.loc[data["French"] == french_word, "English"].tolist()
	canvas.itemconfig(canvas_image, image=back_image)
	canvas.itemconfig(language_text, fill="white", text="English")
	canvas.itemconfig(word_text, fill="white", text=english_word)
	
# ----------------------------------- Button Actions ----------------------------------- #

def is_unknown():
	data.to_csv('data/words_to_learn.csv', index=False)
	next_card()

def is_known():
	global data
	data = data[data["French"] != french_word] #remove word from data
	data.to_csv('data/words_to_learn.csv', index=False)
	next_card()

# ----------------------------------- UI Setup ----------------------------------- #

window = Tk()
window.title("flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(410, 263, image=front_image)
language_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

#Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=is_unknown)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=is_known)
right_button.grid(row=1, column=1)

next_card() # default start program with a word

window.mainloop()