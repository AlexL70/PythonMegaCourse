import streamlit as st
import modules.functions as fn

todos = fn.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.text("This app is to increase you productivity.")

for index, todo in enumerate(todos):
    st.checkbox(f"{index + 1} – {todo}")

st.text_input(label="Enter a todo to be added:", placeholder="New todo")

