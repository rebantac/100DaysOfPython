import pandas

squirrel_data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

gray_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count],
}

# print(data_dict)
data = pandas.DataFrame(data_dict)
print(data)

data.to_csv("squirrel-count.csv")