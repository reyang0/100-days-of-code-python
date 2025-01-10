# ----------------------------------- Version 2 Description ----------------------------------- #
# I created my own version of this capstone project. This version allows you to input an 
# answer to the French word and returns whether or not your input is correct. It is not case 
# sensitive, but the input must match exactly that of the solution in order for it to be 
# considered correction.

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
english_word = ""
is_known = None

# ----------------------------------- Next Card ----------------------------------- #

def next_card():
	global french_word, english_word
	if timer is not None:
		window.after_cancel(timer)
	french_word = choice(data.French)
	english_word = data.loc[data["French"] == french_word, "English"].tolist()
	word_entry.delete(0, END) # clear entry
	canvas.itemconfig(language_text, fill="black", text="French")
	canvas.itemconfig(word_text, fill="black", text=french_word)
	canvas.itemconfig(result_text, fill="black", text="")

def flip_card():
	global timer, data
	canvas.itemconfig(canvas_image, image=back_image)
	canvas.itemconfig(language_text, fill="white", text="English")
	canvas.itemconfig(word_text, fill="white", text=english_word)
	result = "Here is the answer."
	word_guess = word_entry.get()
	if is_known:
		if word_guess.lower() == english_word[0].lower():
			data = data[data["French"] != french_word] #remove word from data
			result = "You got it right!"
		else
			result = "You got it wrong."
	data.to_csv('data/words_to_learn.csv', index=False)
	canvas.itemconfig(result_text, fill="white", text=result)
	timer = window.after(5000, next_card) # 5000 miliseconds = 5 second
	
# ----------------------------------- Button Actions ----------------------------------- #

def is_unknown():
	is_known = False
	flip_card()

def is_known():
	is_known = True
	flip_card()

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

word_entry = Entry(width=10, bg="white", fg="black", highlightthickness=0)
canvas.create_window(400, 350, window=word_entry) 
result_text = canvas.create_text(400, 400, text="testing", font=("Ariel", 40, "italic"))

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