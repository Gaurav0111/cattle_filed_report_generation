from  imports.imports import *
from pdfData import *

def generatepdf(pdf):
    # pdf.ln(10)
    pdf.set_font("Arial" ,'',30)
    pdf.text(43,25,txt="CATTLE FEED FACTORY")
    pdf.ln(5)
    pdf.set_font("Arial" ,'',20)
    pdf.text(30,34,txt="Kichha By Pass Road , Rudrapur (U.S. Nagar)")
    pdf.ln(5)
    pdf.set_font("Arial" ,'B',20)
    pdf.text(45,43,txt="LABORATORY ANALYSIS REPORT")
    pdf.ln(5)
    pdf.set_font("Arial" ,'',20)
    pdf.text(70,52,txt="(RAW MATERIAL)")
    pdf.ln(23)
    addText(pdf)