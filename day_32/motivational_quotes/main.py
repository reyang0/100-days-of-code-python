
# SMTP = Simple Mail Transfer Protocol
# TLS = Transport Layer Security

import private #my personal information
import smtplib
import datetime as dt
import random as r

my_email = private.google_email
my_password = private.google_app_password

dow = {
	"Monday": 0,
	"Tuesday": 1,
	"Wednesday": 2,
	"Thursday": 3,
	"Friday": 4,
	"Saturday": 5,
	"Sunday": 6,
}

today_is_monday = (dt.datetime.now().weekday() == dow["Monday"])
today_is_friday = (dt.datetime.now().weekday() == dow["Friday"]) # for testing

if today_is_friday:
	with open("quotes.txt") as file:
		lines = file.readlines()
		quote_of_the_week = r.choice(lines)
	with smtplib.SMTP("smtp.gmail.com") as connection:
		connection.starttls() # secure connection to email server
		connection.login(user=my_email, password=my_password)
		connection.sendmail(
			from_addr=my_email, 
			to_addrs=my_email, 
			msg=f"Subject:Monday Motivation\n\n{quote_of_the_week}"
		)
