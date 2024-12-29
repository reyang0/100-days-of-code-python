
# -------------------------------------------------- #
# Version 1 (Native)
# -------------------------------------------------- #

def read_v1():
	with open("weather_data.csv") as data_file:
		data = data_file.readlines()
		return data

# -------------------------------------------------- #
# Version 2 (CSV)
# -------------------------------------------------- #

import csv

def read_v2():
	with open("weather_data.csv") as data_file:
		data = csv.reader(data_file) # csv reader object
		temperatures = []
		for row in data:
			if row[1] != "temp":
				temperatures.append(int(row[1]))
		return data

# -------------------------------------------------- #
# Version 3 (Pandas)
# -------------------------------------------------- #

import pandas #pip install pandas

def read_v3():
	data = pandas.read_csv("weather_data.csv")
	return data

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

data = read_v3()
#print(type(data)) 						# <class 'pandas.core.frame.DataFrame'>
#print(type(data["temp"])) 				# <class 'pandas.core.series.Series'>

data_dict = data.to_dict()

temp_list = data["temp"].to_list()
avg_temp = data["temp"].mean() 			# avg = sum(temp_list) / len(temp_list)
max_temp = data["temp"].max()

# - - - - - - - - - - - - - - - - #
#Get Data in Columns
# - - - - - - - - - - - - - - - - #

condition1 = data["condition"]
condition2 = data.condition

# - - - - - - - - - - - - - - - - #
#Get Data in Rows
# - - - - - - - - - - - - - - - - #

monday = data[data.day == "Monday"]

# - - - - - - - - - - - - - - - - #
#Get DoW with highest temperature
# - - - - - - - - - - - - - - - - #

max_temp_day = data[data.temp == data["temp"].max()]

# - - - - - - - - - - - - - - - - #
#Get Monday's temperature in Fahrenheit
# - - - - - - - - - - - - - - - - #

monday_temp_F = celsius_to_fahrenheit(monday.temp[0])

# - - - - - - - - - - - - - - - - #
#Create a dataframe from scratch
# - - - - - - - - - - - - - - - - #

data_dict = {
	"students": ["Amy", "James", "Angela"],
	"scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv") 			# name of new csv file





































