from imports.imports import *

def createtable(pdf,value):
    pdf.ln(30)
    table_cell_width = 21
    table_cell_height = 6
    pdf.set_font("Arial" ,'B',8)
    columns = ["Material" , "Code No. R" , "Moisture" , "Crude Fat" , "Crude Protien","Crude Fibre ","Total Aish","Sand silica","Remark"]
    for col in columns :
        pdf.cell(table_cell_width , table_cell_height,col , align = 'C' , border = 1)
    pdf.ln(table_cell_height)
    table_cell_height = 30
    for val in value:
        pdf.cell(table_cell_width,table_cell_height,val,align = 'C',border = 1)
    pdf.ln(table_cell_height)

def addText(pdf):
    pdf.ln(10)
    pdf.set_font("Arial" ,'',15)
    pdf.text(15,70,txt="To,")
    pdf.text(140,70,txt=f"Date : {str(date.today())} ")
    pdf.text(15,80,txt="Sequence No.....")
    pdf.ln(8)