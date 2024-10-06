import modules.functions as fn
import FreeSimpleGUI as sg


"""
Keys used to identify controls
"""
TODO_INPUT: str="todo_input"
ADD_BTN: str="add_btn"

label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Please enter a to-do", key=TODO_INPUT)
add_button = sg.Button("Add", key=ADD_BTN)
wnd = sg.Window('My To-Do App',
                layout=[[label],[input_box, add_button]],
                font=('Helvetica', 18))

todos = fn.get_todos()
while True:
    event, values = wnd.read()
    match event:
       case sg.WIN_CLOSED:
           break
       case ADD_BTN:
           todos.append(values[TODO_INPUT])
           fn.write_todos(todos)

wnd.close()