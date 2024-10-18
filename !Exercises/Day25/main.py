import os
from fpdf import FPDF
import pathlib as path

pdf = FPDF(orientation="portrait", unit="mm", format="A4")
for file_name in os.listdir("textfiles"):
    if file_name.endswith(".txt"):
        name = path.Path(f"textfiles/{file_name}").stem
        pdf.add_page()
        pdf.set_font("Times", size=16, style="B")
        pdf.cell(w=200, h=16, txt=name.capitalize(), ln=True, align="L")
    with open(f"textfiles/{file_name}", "r") as file:
        pdf.set_font("Times", size=12)
        for line in file:
            pdf.multi_cell(w=200, h=8, txt=line, align="L")
pdf.output("output.pdf")
