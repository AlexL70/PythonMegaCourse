import FreeSimpleGUI as sg

class ControlKeys:
    INCHES_LBL = "__inches_lbl_"
    FEET_LBL = "__feet_lbl__"
    INCHES_INP = "__inches_inp__"
    FEET_INP = "__feet_inp__"
    CONVERT_BTN = "__convert_btn__"
    RESULT_LBL = "__result_lbl___"

feet_lbl = sg.Text("Enter feet:", key=ControlKeys.FEET_LBL)
feet_input = sg.InputText(tooltip="Feet", key=ControlKeys.FEET_INP)
inches_lbl = sg.Text("Enter inches:", key=ControlKeys.INCHES_LBL)
inches_input = sg.InputText(tooltip="Inches", key=ControlKeys.INCHES_INP)
convert_btn = sg.Button("Convert", key=ControlKeys.CONVERT_BTN)
result_lbl = sg.Text("", key=ControlKeys.RESULT_LBL)

wnd = sg.Window("Convertor", layout=[
    [feet_lbl, feet_input],
    [inches_lbl, inches_input],
    [convert_btn, result_lbl]],
                font=('Times', 20))

while True:
    event, values = wnd.read()
    match event:
        case sg.WIN_CLOSED:
            break
        case ControlKeys.CONVERT_BTN:
            feet = float(values[ControlKeys.FEET_INP])
            inches = float(values[ControlKeys.INCHES_INP])
            result = feet * 0.3048 + inches * 0.0254
            wnd[ControlKeys.RESULT_LBL].update(value=str(result))
wnd.close()