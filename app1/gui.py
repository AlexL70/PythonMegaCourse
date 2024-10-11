import modules.functions as fn
import FreeSimpleGUI as sg
import time
import os

# Check if file exists and create one if it does not
if not os.path.exists(fn.FILE_PATH):
    with open(fn.FILE_PATH, "w") as file:
        pass

sg.theme("DarkTeal10")

"""
Keys used to identify controls
"""
class ControlKeys:
    TODO_INPUT: str="__todo_input__"
    TODO_LST: str="__todo_lst__"
    ADD_BTN: str="__add_btn__"
    EDIT_BTN: str="__edit_btn__"
    COMPLETE_BTN: str="__complete_btn__"
    EXIT_BTN: str="__exit_btn__"
    TIME_LBL: str="__time_lbl__"

# Read todo list from the file
todos = fn.get_todos()

clock_label=sg.Text(key=ControlKeys.TIME_LBL)
label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Please enter a to-do", key=ControlKeys.TODO_INPUT)
add_button = sg.Button(key=ControlKeys.ADD_BTN, size=(10,1), image_source="./add.png", mouseover_colors="LightBlue2", tooltip="Add new item.")
edit_button = sg.Button("Edit", key=ControlKeys.EDIT_BTN, mouseover_colors="LightBlue2", tooltip="Edit selected item")
complete_button = sg.Button(key=ControlKeys.COMPLETE_BTN, size=(10, 1), image_source="./complete.png", mouseover_colors="LightBlue2")
exit_button = sg.Button("Exit", key=ControlKeys.EXIT_BTN, mouseover_colors="LightBlue2", tooltip="Complete (remove) selected item")
todo_list = sg.Listbox(values=todos, key=ControlKeys.TODO_LST, select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, bind_return_key=True, auto_size_text=True, enable_events=True, size=(40,10))
wnd = sg.Window('My To-Do App',
                layout=[[clock_label],
                        [label],
                        [input_box, add_button],
                        [todo_list, edit_button, complete_button],
                        [exit_button]],
                font=('Helvetica', 18))

while True:
    event, values = wnd.read(timeout=200)
    wnd[ControlKeys.TIME_LBL].update(value=f"It is {time.strftime('%b %d, %Y %H:%M:%S')}")
    match event:
        case ControlKeys.ADD_BTN:
            todos.append(values[ControlKeys.TODO_INPUT])
            fn.write_todos(todos)
            wnd[ControlKeys.TODO_LST].update(values=todos)
        case ControlKeys.EDIT_BTN:
            try:
                list_item = values[ControlKeys.TODO_LST][0]
                edit_line = values[ControlKeys.TODO_INPUT]
                index = todos.index(list_item)
                todos[index] = edit_line
                fn.write_todos(todos)
                wnd[ControlKeys.TODO_LST].update(values=todos)
            except IndexError:
                sg.popup("Before pressing \"Edit\", please select the item and change it as you wish.",
                         font=('Helvetica', 24))
        case ControlKeys.COMPLETE_BTN:
            try:
                list_item = values[ControlKeys.TODO_LST][0]
                index = todos.index(list_item)
                todos.pop(index)
                fn.write_todos(todos)
                wnd[ControlKeys.TODO_LST].update(values=todos)
                list_item = values[ControlKeys.TODO_LST][0]
                wnd[ControlKeys.TODO_INPUT].update(value='')
            except IndexError:
                sg.popup("Before pressing \"Complete\", please select the item.", font=('Helvetica', 24))
        case ControlKeys.TODO_LST:
            list_item = values[ControlKeys.TODO_LST][0]
            wnd[ControlKeys.TODO_INPUT].update(value=list_item)
        case ControlKeys.EXIT_BTN:
            break
        case sg.WIN_CLOSED:
            break

wnd.close()