import datetime as dt
import os
import requests as req
import selectorlib as sl


URL = "https://programmer100.pythonanywhere.com/"
FILE_PATH = "data/temperature.txt"


def get_data(url: str) -> str:
    response = req.get(url)
    return response.text


def save_temperature(temperature: int) -> None:
    exsts = os.path.exists(FILE_PATH)
    if not exsts:
        with open(FILE_PATH, "w") as file:
            file.write("date,temperature\n")
    with open(FILE_PATH, "a") as file:
        date_str = dt.datetime.now().strftime("%y-%m-%d-%H-%M-%S")
        file.write(f"{date_str},{temperature}\n")


source = get_data(URL)
extracted = sl.Extractor.from_yaml_file("temperature.yml").extract(source)
save_temperature(int(extracted["temperature"]))
