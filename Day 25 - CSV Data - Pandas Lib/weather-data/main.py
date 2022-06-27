# with open("weather-data.csv") as weather_file:
#     weather_data = weather_file.readlines()
# print(weather_data)

# More efficient to use the csv library
# import csv

# with open("weather-data.csv") as weather_file:
#     weather_data = csv.reader(weather_file)
#     temperatures = []
#     for row in weather_data:
#         # print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
    
# More efficient is to use the pandas library

import pandas

weather_data = pandas.read_csv("weather-data.csv")
# print(weather_data)
# print(weather_data["temp"])

# weather_data_dict = weather_data.to_dict()
# print(weather_data_dict)

# temp_list = weather_data["temp"].to_list()
# print(temp_list)

# avg_temp = round(sum(temp_list)/len(temp_list))
# print(avg_temp)
# - Or -
# print(weather_data["temp"].mean())

# print(weather_data["temp"].max())

# Methods to get Data from columns:
# # Method 1:
# print(weather_data["condition"])
# # Method 2:
# print(weather_data.condition)

# Get Data from rows:
# print(weather_data[weather_data.day == "Monday"])
# print(weather_data[weather_data.temp == weather_data.temp.max()])

# Also:
# monday = weather_data[weather_data.day == "Monday"]
# temp_inF = (monday.temp * 1.8) + 32
# print(temp_inF)

# # Creating a DataFrame from scratch
# data_dict = {
#     "students" : ["Charles", "Henry", "John"],
#     "marks" : [78, 34, 43],
# }

# data = pandas.DataFrame(data_dict)
# print(data)
# # Converting above DataFrame in .csv file
# data.to_csv("student_marks.csv")
