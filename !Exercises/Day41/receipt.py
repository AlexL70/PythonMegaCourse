from article import Article
from fpdf import FPDF


class Receipt:
    def __init__(self, article: Article):
        self.article = article

    def generate(self) -> None:
        pdf = FPDF(orientation='portrait', unit='mm', format='A4')
        pdf.add_page()
        pdf.set_font("Arial", size=16, style='B')
        pdf.cell(w=0, h=10, txt=f"Receipt nr.{self.article._id}", ln=True, align='L')
        pdf.cell(w=0, h=10, txt=f"Article: {self.article.name.title()}", ln=True, align='L')
        pdf.cell(w=0, h=10, txt=f"Price: {self.article.price:.2f}", ln=True, align='L')
        pdf.output(f"receipts/receipt_{self.article._id}.pdf")