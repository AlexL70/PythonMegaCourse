import FreeSimpleGUI as sg
from zip_creator import make_archive

class ControlKeys:
    CHOOSE_FILES: str = "__choose_files__"
    CHOOSE_FOLDER: str = "__chose_folder__"
    COMPRESS_BTN: str = "__compress_btn__"
    OUTPUT_LBL: str = "__output_lbl__"

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_btn1 = sg.FilesBrowse("Choose", key=ControlKeys.CHOOSE_FILES)
label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_btn2 = sg.FolderBrowse("Choose", key=ControlKeys.CHOOSE_FOLDER)
compress_btn = sg.Button("Compress", key=ControlKeys.COMPRESS_BTN)
output_lbl=sg.Text("", key=ControlKeys.OUTPUT_LBL)


wnd = sg.Window("File Compressor",
                layout=[[label1, input1, choose_btn1],
                        [label2, input2, choose_btn2],
                        [compress_btn, output_lbl]])

while True:
    event, values = wnd.read()
    match event:
        case sg.WIN_CLOSED:
            break
        case ControlKeys.COMPRESS_BTN:
            file_paths = values[ControlKeys.CHOOSE_FILES].split(";")
            dest_path = values[ControlKeys.CHOOSE_FOLDER]
            make_archive(file_paths, dest_path)
            wnd[ControlKeys.OUTPUT_LBL].update(value="Compression completed!")
wnd.close()