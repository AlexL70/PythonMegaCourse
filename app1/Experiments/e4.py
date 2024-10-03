import csv
from sys import exception

with open("files/weather.csv", 'r') as file:
    data = list(csv.reader(file))[1:]
tmpr_dict = {}
for datum in data:
    tmpr_dict[datum[0]] = int(datum[1])
city = input("Enter city: ")
try:
    tmpr = tmpr_dict[city]
    print(f"Temperature in {city} is {tmpr}")
except KeyError:
    print(f"{city} city not found in our DB.")
