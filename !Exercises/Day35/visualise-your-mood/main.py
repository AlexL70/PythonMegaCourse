import streamlit as st
import os
import nltk
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer

st.title("Diary tone")

files = os.listdir("diary")
files.sort(reverse=False)
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

scores = []
dates = []
for file in files:
    print(file)
    dates.append(file.split(".")[0])
    with open(f"diary/{file}", "r") as f:
        text = f.read()
        score = sia.polarity_scores(text)
        scores.append(score)

st.subheader("Positivity")
figure = px.line(x=dates, y=[score["pos"] for score in scores], labels={
                 "x": "Date", "y": "Positivity"})
st.plotly_chart(figure)

st.subheader("Negativity")
figure = px.line(x=dates, y=[score["neg"] for score in scores], labels={
                 "x": "Date", "y": "Negativity"})
st.plotly_chart(figure)

# st.write(scores)
# st.write(dates)
