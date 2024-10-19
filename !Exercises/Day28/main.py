import requests as rq
import os
import streamlit as st
from datetime import date

BASE_URL = "https://api.nasa.gov/planetary/apod"
API_KEY = os.environ.get("NASA_API_KEY")
today = date.today().strftime("%Y-%m-%d")
url: str = f"{BASE_URL}?api_key={API_KEY}&date={today}&concept_tags=True"

response = rq.get(url)
if response.status_code != 200:
    print(f"Error: {response.status_code}: {response.text}")
    exit(1)
image_url = response.json()["hdurl"]
img_response = rq.get(image_url)
with open("image.jpg", "wb") as file:
    file.write(img_response.content)
text = response.json()["explanation"]

st.set_page_config(page_title="NASA APOD", page_icon="🌌", layout="wide")
st.title("NASA Astronomy Picture of the Day")
st.subheader(today)
st.write("This is not a NASA site. This is a Streamlit app that uses the NASA API. So the image and text are from NASA.")
st.image("./image.jpg")
st.write(text)
