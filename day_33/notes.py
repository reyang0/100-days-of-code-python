import requests
from datetime import datetime

# ---------------------------------------------------------------------- #
# Exercise: iss
# ---------------------------------------------------------------------- #

endpoint = "http://api.open-notify.org/iss-now.json"
response = requests.get(url=endpoint)
response.raise_for_status() # raise an error if response not found

data = response.json()

longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

iss_position = (longitude, latitude)
print(iss_position)

# ---------------------------------------------------------------------- #
# Exercise: Sunrise / Sunset
# ---------------------------------------------------------------------- #

MY_LAT = 51.507351 #for London from latlong.net
MY_LNG = -0.127758 #for London from latlong.net

parameters = {
	"lat": MY_LAT,
	"lng": MY_LNG,
	"formatted": 0
}

endpoint = "https://api.sunrise-sunset.org/json"
response = requests.get(endpoint, params=parameters)
response.raise_for_status()

data = response.json()

sunrise = data["results"]["sunrise"]
sunrise_hour = int(sunrise.split("T")[1].split(":")[0])

sunset = data["results"]["sunset"]
sunset_hour = int(sunset.split("T")[1].split(":")[0])

print(sunrise)

time_now = datetime.now()
print(time_now)