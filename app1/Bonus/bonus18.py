import FreeSimpleGUI as sg
import zip_extractor as extr

class ControlKeys:
    ARCH_LBL: str="__arch_lbl__"
    ARCH_INP: str="__arch_input__"
    ARCH_BTN: str="__arch_button__"
    DEST_LBL: str="__dest_lbl__"
    DEST_INP: str="__dest_input__"
    DEST_BTN: str="__dest_button__"
    EXTR_BTN: str="__extract_button__"
    OUT_LBL: str="__output_lbl__"

sg.theme('DarkTeal10')

arch_lbl=sg.Text("Select archive:", key=ControlKeys.ARCH_LBL, size=(22, 1))
arch_inp=sg.Input(key=ControlKeys.ARCH_INP)
arch_btn=sg.FileBrowse("Choose", key=ControlKeys.ARCH_BTN)
dest_lbl=sg.Text("Select destination dir:", key=ControlKeys.DEST_LBL, size=(22, 1))
dest_inp=sg.Input(key=ControlKeys.DEST_INP)
dest_btn=sg.FolderBrowse("Choose", key=ControlKeys.DEST_BTN)
extr_btn=sg.Button("Extract", key=ControlKeys.EXTR_BTN)
out_lbl=sg.Text("", key=ControlKeys.OUT_LBL, text_color="green")

wnd = sg.Window("Archive Extractor",
                layout=[[arch_lbl, arch_inp, arch_btn],
                        [dest_lbl, dest_inp, dest_btn],
                        [extr_btn, out_lbl]])
while True:
    event, values = wnd.read()
    match event:
        case ControlKeys.EXTR_BTN:
            arch_path = values[ControlKeys.ARCH_BTN]
            destination = values[ControlKeys.DEST_BTN]
            extr.extract_archive(arch_path, destination)
            wnd[ControlKeys.OUT_LBL].update(value="Extracted successfully!")
        case sg.WIN_CLOSED:
            break
wnd.close()