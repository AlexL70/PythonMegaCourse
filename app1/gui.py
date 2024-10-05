import functools
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Please enter a to-do")
add_button = sg.Button("Add")
wnd = sg.Window('My To-Do App', layout=[[label],[input_box, add_button]])
wnd.read()
wnd.close()
