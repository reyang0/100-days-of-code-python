from tkinter import * 							#all classes
from tkinter import messagebox 					#messagebox module
import os 										#check if data.txt exists
from random import randint, choice, shuffle 	#password_generator
import pyperclip 								#save password to clipboard

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	password_letters = [choice(letters) for _ in range(randint(8, 10))]
	password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
	password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

	password_list = password_letters + password_numbers + password_symbols
	shuffle(password_list)
	password = "".join(password_list)

	password_entry.delete(0, END)
	password_entry.insert(0, password)
	pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def entry_exists():
	website = website_entry.get()
	email = email_entry.get()
	password = password_entry.get()
	new_entry = f"{website} | {email} | {password}\n"

	#check if file exists
	if os.path.exists("data.txt"):
	    file_exist = True
	else:
	    file_exist = False

	#check if new entry already exists in data.txt
	if file_exist:
		with open('data.txt', 'r') as file:
			for line in file.readlines():
				if line == new_entry:
					return True

	return False

def has_blank_entry():
	website = website_entry.get()
	email = email_entry.get()
	password = password_entry.get()
	return (not website) or (not email) or (not password)

def save_password():
	website = website_entry.get()
	email = email_entry.get()
	password = password_entry.get()
	new_entry = f"{website} | {email} | {password}\n"

	# catch if any fields are left blank
	if has_blank_entry():
		messagebox.showwarning(title="ERROR", message="Empty fields.")
		return

	# catch if entry already exists in data.txt
	if entry_exists():
		messagebox.showwarning(title="ERROR", message="Entry already exists.")
		return

	# catch if user cancels messagebox
	is_ok = messagebox.askokcancel(title=website, message=
												f"These are the details entered"
												f"\nWebsite: {website}"
												f"\nEmail: {email}"
												f"\nPassword: {password}"
												f"\nIs it ok to save?"
												)
	if is_ok:
		with open('data.txt', 'a') as file:
			file.write(new_entry)
		#clear entries
		website_entry.delete(0, END)
		password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img) 	# x_position=100, y_position=100
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website")
email_label = Label(text="Email/Username")
password_label = Label(text="Password")
status_label = Label(text="")

website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)
status_label.grid(row=5, column=1)

#Entries
website_entry = Entry(width=38) 			# per lecture, width=35 did not align the columns for my screen
email_entry = Entry(width=38) 				# per lecture, width=35 did not align the columns for my screen
password_entry = Entry(width=21)

website_entry.grid(row=1, column=1, columnspan=2)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)

website_entry.focus() 						# start curser inside the textbox
email_entry.insert(0, "dummy@email.com") 	# pre-populated value

#Buttons
generate_password_button = Button(text="Generate Password", command=password_generator)
add_button = Button(text="Add", width=36, command=save_password)

generate_password_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()