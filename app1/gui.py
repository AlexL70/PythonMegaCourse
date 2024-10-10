import modules.functions as fn
import FreeSimpleGUI as sg

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

# Read todo list from the file
todos = fn.get_todos()

label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Please enter a to-do", key=ControlKeys.TODO_INPUT)
add_button = sg.Button("Add", key=ControlKeys.ADD_BTN)
edit_button = sg.Button("Edit", key=ControlKeys.EDIT_BTN)
complete_button = sg.Button("Complete", key=ControlKeys.COMPLETE_BTN)
exit_button = sg.Button("Exit", key=ControlKeys.EXIT_BTN)
todo_list = sg.Listbox(values=todos, key=ControlKeys.TODO_LST, select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, bind_return_key=True, auto_size_text=True, enable_events=True, size=(40,10))
wnd = sg.Window('My To-Do App',
                layout=[[label],
                        [input_box, add_button],
                        [todo_list, edit_button, complete_button],
                        [exit_button]],
                font=('Helvetica', 18))

while True:
    event, values = wnd.read()
    #print(event)
    #print(values)
    match event:
        case ControlKeys.ADD_BTN:
            todos.append(values[ControlKeys.TODO_INPUT])
            fn.write_todos(todos)
            wnd[ControlKeys.TODO_LST].update(values=todos)
        case ControlKeys.EDIT_BTN:
            list_item = values[ControlKeys.TODO_LST][0]
            edit_line = values[ControlKeys.TODO_INPUT]
            index = todos.index(list_item)
            todos[index] = edit_line
            fn.write_todos(todos)
            wnd[ControlKeys.TODO_LST].update(values=todos)
        case ControlKeys.COMPLETE_BTN:
            list_item = values[ControlKeys.TODO_LST][0]
            index = todos.index(list_item)
            todos.pop(index)
            fn.write_todos(todos)
            wnd[ControlKeys.TODO_LST].update(values=todos)
            list_item = values[ControlKeys.TODO_LST][0]
            wnd[ControlKeys.TODO_INPUT].update(value='')
        case ControlKeys.TODO_LST:
            list_item = values[ControlKeys.TODO_LST][0]
            wnd[ControlKeys.TODO_INPUT].update(value=list_item)
        case ControlKeys.EXIT_BTN:
            break
        case sg.WIN_CLOSED:
            break

wnd.close()