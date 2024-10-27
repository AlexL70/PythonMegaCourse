import pandas as pd
import plotly.express as px
import sqlite3 as sql
import streamlit as st
from file_path import FILE_PATH
from datetime import datetime

connection = sql.connect("./data/temperature.db")
cursor = connection.cursor()
try:
    data = cursor.execute("SELECT * FROM temperature").fetchall()
except sql.OperationalError:
    data = []
if data and len(data) > 0:
    data = [(datetime.strptime(row[0], "%y-%m-%d-%H-%M-%S"), row[1])
            for row in data]
    df = pd.DataFrame(data, columns=["date", "temperature"])
    fig = px.line(x=df["date"], y=df["temperature"],
                  title="Temperature Graph", labels={"x": "Date/Time", "y": "Temperature (°C)"})
    st.plotly_chart(fig)
else:
    st.subheader("No data available!")
cursor.close()
