#
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len (data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len (data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len (data[data["Primary Fur Color"] == "Black"])

print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)



data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count,red_squirrels_count,black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrels_count.csv")

# print(data["Primary Fur Color"])


# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
#
# # # print(data["temp"])
# # data_dict = data.to_dict()
# # #print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# #
# # print (len(temp_list))
# #
# # print(data["temp"].mean())
# # print(data["temp"].max())
# # average = sum(temp_list) / len(temp_list)
# # print(average)
#
# #Get data in columns
# #name_of_variable["name_of_column"].name_of_function !!!
# #print (data["contition"])   = print(data.condition) same way
#
#
# #get data in row
# # print(data[data.temp == data.temp.max()])
# # print(data[data.day == "Monday"])
#
# # monday = data[data.day == "Monday"]
# # monday_temp = int(monday.temp)
# # monday_tempF = ((monday.temp) * 9/5 ) + 32
# # print(monday_tempF)
#
# #create dataframe from scratch
# data_dict = {
#     "students":["Amy", "James", "Angela"],
#     "scores": [ 79, 56, 68]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
