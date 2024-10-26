import os
import pandas as pd
import plotly.express as px
import streamlit as st
from file_path import FILE_PATH
from datetime import datetime

# st.title("Temperature Graph")
exists = os.path.exists(FILE_PATH)
if exists:
    df = pd.read_csv(FILE_PATH, parse_dates=[
                     "date"], date_parser=lambda x: datetime.strptime(x, '%y-%m-%d-%H-%M-%S'))
    # st.write(df)
    fig = px.line(x=df["date"], y=df["temperature"],
                  title="Temperature Graph", labels={"x": "Date/Time", "y": "Temperature (°C)"})
    st.plotly_chart(fig)
else:
    st.subheader("No data available!")
