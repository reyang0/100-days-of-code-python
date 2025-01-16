import requests
from datetime import datetime
import math
import smtplib
import private #personal email information
import time

MY_LAT = 51.507351  # London
MY_LONG = -0.127758 # London

#Your position is within +5 or -5 degrees of the ISS position.

def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    my_pos = {
        "x": MY_LAT,
        "y": MY_LONG
    }

    iss_pos = {
        "x": iss_latitude
        "y": iss_longitude
    }

    distance = math.sqrt((my_pos["x"] – iss_pos["x"])**2 + (my_pos["y"] – iss_pos["y"])**2)

    return distance <= 5

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    now_hour = datetime.now().hour

    return sunset_hour >= now_hour or now_hour =< sunrise_hour

#If the ISS is close to my current position and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60) #sleep for 60 seconds
    if is_overhead() and is_dark():
        my_email = private.google_email
        my_password = private.google_app_password

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls() # secure connection to email server
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=my_email, 
                msg=f"Subject:Look Up!\n\nISS is in position at night"
            )




