from imports.imports import *
import main
from createRemark import *
from pdfData import *
from generatePDF import *

def executing():
    if (main.button1.get() == 0 and main.button2.get() == 0 and main.button3.get() == 0 and main.button4.get() == 0 and main.button5.get() == 0 and main.button6.get() == 0) :
        messagebox.showerror("Alert"," Please Select Material Name") 
    elif  main.r_number_input.get() == '':
        messagebox.showerror("Alert"," Please Enter R Number") 
    else:
        if messagebox.askquestion( "Confirmation", "Are You Sure") == "no":
            return
        value = []
        value.append(main.result())
        value.append(main.r_number_input.get())
        value.append(main.moisture_input.get())
        value.append(main.fat_input.get())
        value.append(main.protein_input.get())
        value.append(main.fibre_input.get())
        value.append(main.aish_input.get())
        value.append(main.silica_input.get())
        value.append(main.analysis_input.get())
        for i in range(len(value)):
            if value[i] == '':
                value[i] = "____"
            else:
                t = ""
                t += str(value[i])
                value[i] = t
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial" ,'B',20)
        generatepdf(pdf)
        createtable(pdf,value)
        createRemark(pdf)
        file_name = ""
        file_name += main.r_number_input.get()
        file_name += ".pdf"
        # pdf.output(f"report\\{file_name}")  
        pdf.output(file_name)  
        # print(file_name)
        messagebox.showinfo("Information" , "Report has been generated")  
        main.reset_input()
        os.system(file_name)
        # upload_to_drive(file_name)