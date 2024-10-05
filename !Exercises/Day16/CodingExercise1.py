import FreeSimpleGUI as sg

feet_lbl = sg.Text("Enter feet:")
feet_inp = sg.Input()
inches_lbl = sg.Text("Input inches:")
inches_inp = sg.Input()
cnv_btn = sg.Button("Convert")

wnd = sg.Window("Convertor", layout=[[feet_lbl, feet_inp],
                                     [inches_lbl, inches_inp],
                                     [cnv_btn]])
wnd.read()
wnd.close()