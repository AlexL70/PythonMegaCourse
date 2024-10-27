import datetime as dt
import os
import requests as req
import selectorlib as sl
import sqlite3 as sql
from file_path import FILE_PATH


URL = "https://programmer100.pythonanywhere.com/"


def get_data(url: str) -> str:
    response = req.get(url)
    return response.text


def save_temperature(temperature: int) -> None:
    connection = sql.connect("./data/temperature.db")
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS temperature (date TEXT, temperature INTEGER)")
    date_str = dt.datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    cursor.execute("INSERT INTO temperature VALUES (?, ?)",
                   (date_str, temperature))
    connection.commit()


source = get_data(URL)
extracted = sl.Extractor.from_yaml_file("temperature.yml").extract(source)
save_temperature(int(extracted["temperature"]))
