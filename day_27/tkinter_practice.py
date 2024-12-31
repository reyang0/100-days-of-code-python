
# tkinter documentation
# https://docs.python.org/3/library/tkinter.html#

# Mac Installation Instructions
# https://www.geeksforgeeks.org/how-to-install-tkinter-on-macos/

# no longer needs to mention tkinter for classes
from tkinter import *

def button_clicked():
	new_text = input.get()
	my_label.config(text=new_text)

# ------------------------- #
# Window
# ------------------------- #

window = Tk() # tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# ------------------------- #
# Label
# ------------------------- #

my_label = Label(text="I am a Label", font=("Arial", 24, "bold")) # tkinter.Label()
my_label.grid(column=0, row=0)
#my_label.config(padx=50, pady=50)

#my_label["text"] = "New Text" 		# change text value
#my_label.config(text="New Text") 	# change text value

# ------------------------- #
# Button
# ------------------------- #

button = Button(text="Click Me", command=button_clicked) # tkinter.Button()
button.grid(column=1, row=1)

button2 = Button(text="New Button", command=button_clicked) # tkinter.Button()
button2.grid(column=2, row=0)

# ------------------------- #
# Entry
# https://tcl.tk/man/tcl8.6/TkCmd/entry.htm
# ------------------------- #

input = Entry(width=10) #tkinter.Entry()
input.grid(column=3, row=2)






# pack - https://tcl.tk/man/tcl8.6/TkCmd/pack.htm
# place
# grid




window.mainloop() # keep window open