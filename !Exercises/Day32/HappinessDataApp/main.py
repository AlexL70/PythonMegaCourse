import pandas as pd
import streamlit as st
import plotly.express as px

class DataTypes:
    DT_HAPPINESS = 'Happiness'
    DT_GDP = 'GDP'
    DT_SOCIAL_SUPPORT = 'Social Support'
    DT_LIFE_EXPECTANCY = 'Life Expectancy'
    DT_FREADOM_OF_CHOICE = 'Freedom of Choice'
    DT_GENEROSITY = 'Generosity'
    DT_CORRUPTION_RESISTANCE = 'Corruption Resistance'

DATA_TYPES = [ DataTypes.DT_HAPPINESS, DataTypes.DT_GDP, DataTypes.DT_SOCIAL_SUPPORT,
              DataTypes.DT_LIFE_EXPECTANCY, DataTypes.DT_FREADOM_OF_CHOICE,
              DataTypes.DT_GENEROSITY, DataTypes.DT_CORRUPTION_RESISTANCE]

dt_to_col = {
    DataTypes.DT_HAPPINESS: 'happiness',
    DataTypes.DT_GDP: 'gdp',
    DataTypes.DT_SOCIAL_SUPPORT: 'social_support',
    DataTypes.DT_LIFE_EXPECTANCY: 'life_expectancy',
    DataTypes.DT_FREADOM_OF_CHOICE: 'freedom_to_make_life_choices',
    DataTypes.DT_GENEROSITY: 'generosity',
    DataTypes.DT_CORRUPTION_RESISTANCE: 'corruption'
}

df = pd.read_csv("data/happy.csv")

st.title("In Search for Happiness")
x_axis = st.selectbox("Select the data for the x-axis", options=DATA_TYPES)
y_types = [dt for dt in DATA_TYPES if dt != x_axis]
y_axis = st.selectbox("Select the data for the y-axis", options=y_types)

data = df[[dt_to_col[x_axis], dt_to_col[y_axis]]]
figure = px.scatter(x=data[dt_to_col[x_axis]], y=data[dt_to_col[y_axis]], labels={"x": x_axis, "y": y_axis})
st.plotly_chart(figure)

