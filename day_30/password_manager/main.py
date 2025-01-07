from tkinter import * 							#all classes
from tkinter import messagebox 					#messagebox module
from random import randint, choice, shuffle 	#password_generator
import pyperclip 								#save password to clipboard
import json 									#json module

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
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

def save():
	website = website_entry.get()
	email = email_entry.get()
	password = password_entry.get()

	new_data = {
		website: {
			"email": email,
			"password": password,
		}
	}

	if len(website) == 0 or len(email) == 0 or len(password) == 0:
		messagebox.showwarning(title="ERROR", message="Do not leave any fields empty.")
	else:
		try: 
			with open("data.json", "r") as file:
				data = json.load(file)
		except FileNotFoundError:
			with open("data.json", "w") as file:
				json.dump(new_data, file, indent=4)
			messagebox.showinfo(title="SUCCESS", message="New password has been added.")
			website_entry.delete(0, END)
			password_entry.delete(0, END)
		else:
			is_new_website = True
			for data_website in data:
				if data_website in new_data:
					is_new_website = False
			if not is_new_website:
				messagebox.showwarning(title="ERROR", message="Website already exists.")
			else:
				data.update(new_data)
				file = open("data.json", "w")
				json.dump(data, file, indent=4)
				messagebox.showinfo(title="SUCCESS", message="New password has been added.")
				website_entry.delete(0, END)
				password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search():
	website = website_entry.get()

	if len(website) == 0:
		messagebox.showwarning(title="ERROR", message="Website field is empty.")
	else:
		try: 
			with open("data.json", "r") as file:
				data = json.load(file)
				email = data[website]["email"]
				password = data[website]["password"]
		except FileNotFoundError:
			messagebox.showwarning(title="ERROR", message="File not found.")
		except KeyError:
			messagebox.showwarning(title="ERROR", message="Website not found.")
		else:
			messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")

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
website_entry = Entry(width=21)
email_entry = Entry(width=38)
password_entry = Entry(width=21)

website_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)

website_entry.focus() 						# start curser inside the textbox
email_entry.insert(0, "dummy@email.com") 	# pre-populated value

#Buttons
generate_password_button = Button(text="Generate Password", width=12, command=generate)
add_button = Button(text="Add", width=36, command=save)
search_button = Button(text="Search", width=12, command=search)

generate_password_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)
search_button.grid(row=1, column=2)

window.mainloop()