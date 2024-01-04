from imports.imports import *

def createRemark(pdf):
    pdf.ln(10)
    result = 3
    pdf.set_font("Arial" ,'B',15)
    pdf.text(15,145,txt='Remarks : ')
    
    if result == 1:
        pdf.set_font("Arial" ,'B',18)
        pdf.text(35,157,txt='1.  Accepted')
        pdf.set_font("Arial" ,'',15)
        pdf.text(36,163,txt='2.  Suitable with Rebate')
        pdf.text(36,170,txt='3.  Rejected')
        pdf.text(36,177,txt='4.  Suitable with high rebate')
        pdf.text(45,184,txt="with Factory Manager's Approval")
    
    elif result == 2:
        pdf.set_font("Arial" ,'',15)
        pdf.text(36,152,txt='1.  Accepted')
        pdf.set_font("Arial" ,'B',18)
        pdf.text(35,159,txt='2.  Suitable with Rebate')
        pdf.set_font("Arial" ,'',15)
        pdf.text(36,166,txt='3.  Rejected')
        pdf.text(36,173,txt='4.  Suitable with high rebate')
        pdf.text(42,180,txt="with Factory Manager's Approval")
    
    elif result == 3:
        pdf.set_font("Arial" ,'',15)
        pdf.text(36,152,txt='1.  Accepted')
        pdf.text(36,159,txt='2.  Suitable with Rebate')
        pdf.set_font("Arial" ,'B',18)
        pdf.text(35,166,txt='3.  Rejected')
        pdf.set_font("Arial" ,'',15)
        pdf.text(36,173,txt='4.  Suitable with high rebate')
        pdf.text(42,180,txt="with Factory Manager's Approval")
    
    elif result == 4:
        pdf.set_font("Arial" ,'',15)
        pdf.text(36,152,txt='1.  Accepted')
        pdf.text(36,158,txt='2.  Suitable with Rebate')
        pdf.text(36,165,txt='3.  Rejected')
        pdf.set_font("Arial" ,'B',18)
        pdf.text(35,172,txt='4.  Suitable with high rebate')
        pdf.text(43,180,txt="with Factory Manager's Approval")