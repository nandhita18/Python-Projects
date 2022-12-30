import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data (1).csv")
all_fur_color = list(data["Primary Fur Color"])
grey = 0
black = 0
red = 0
for i in all_fur_color:
    if i == "Gray":
        grey+=1
    elif i == "Cinnamon":
        red+=1
    elif i == "Black":
        black+=1
    else :
        pass
data_dict = {
    "Fur Color":["grey", "red", "black"],
    "Count":[grey, red , black]
}
file = (pandas.DataFrame(data_dict))
file.to_csv("squirrel_count.csv")
