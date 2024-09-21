import math


def get_average():
    with open("files/data.txt") as file:
        data = file.readlines()
    data = data[1:]
    values = [float(d) for d in data]
    return sum(values) / len(values)

average = get_average()
print(average)