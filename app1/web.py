import streamlit as st
import modules.functions as fn

class ControlKeys:
    TODO_INPUT: str = "__todo_input__"
    EDIT_BTN: str = "__edit_button__"
    COMPLETE_BTN: str = "__complete__button"
    TODO_ITEM: str = "__todo__item__"


todos = fn.get_todos()

def add_todo():
    item = st.session_state[ControlKeys.TODO_INPUT]
    todos.append(item)
    fn.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app.")
st.text("This app is to increase you productivity.")

col1, col2 = st.columns((4,1))

for index, todo in enumerate(todos):
    row = st.columns((4,1,1))
    with st.container():
        with row[0]:
            st.write(f"{index + 1} – {todo}")
        with row[1]:
            st.button("Edit", key=f"{ControlKeys.EDIT_BTN}{index}", use_container_width=True)
        with row[2]:
            st.button("Complete", key=f"{ControlKeys.COMPLETE_BTN}{index}", use_container_width=True)


st.text_input(label="Enter a todo to be added:", placeholder="New todo", on_change=add_todo, key=ControlKeys.TODO_INPUT)

print(st.session_state)