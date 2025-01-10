##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

# Extra: Use https://www.pythonanywhere.com/ to schedule an automated run on the cloud.

import private #my personal information
import smtplib
import datetime as dt
import pandas as pd
import random as r

today = dt.datetime.today().strftime('%m-%d')

data = pd.read_csv("birthdays.csv")

my_email = private.google_email
my_password = private.google_app_password

for index, record in data.iterrows():
	bday = f"{record["month"]:02d}-{record["day"]:02d}"
	if today == bday:
		with open(f"letter_templates/letter_{r.randint(1,3)}.txt") as file:
			template_text = file.read()
			template_text = template_text.replace("[NAME]",record["first name"])
		with smtplib.SMTP("smtp.gmail.com") as connection:
			connection.starttls()
			connection.login(user=my_email, password=my_password)
			connection.sendmail(
				from_addr=my_email, 
				to_addrs=record["email"], 
				msg=f"Subject:Happy Birthday!\n\n{template_text}"
			)
