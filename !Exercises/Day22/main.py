"""
Day 22: Student Project: Create a Company Website
"""
import streamlit as st
import pandas as pnd

df = pnd.read_csv("data.csv", sep=',')

st.set_page_config(layout="wide")
st.title("The best company")
description = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
st.write(description)
st.write("<h2>Our team</h2>", unsafe_allow_html=True)

col_len = int(len(df.index) / 3)
col1, space1, col2, space2, col3 = st.columns([8,1,8,1,8])

with col1:
    for index, row in df[:col_len].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(f"{row['role'].title()}")
        st.image(image=f"./images/{row['image']}")

with col2:
    for index, row in df[col_len:col_len*2].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(f"{row['role'].title()}")
        st.image(image=f"./images/{row['image']}")

with col3:
    for index, row in df[col_len*2:].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(f"{row['role'].title()}")
        st.image(image=f"./images/{row['image']}")
