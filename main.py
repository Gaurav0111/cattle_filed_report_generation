from imports.exports import *    


win = Tk()
win.title("LABORATORY ANALYSIS REPORT")
# win.geometry(f"{win.wininfo_screenwidth}x{win.wininfo_screenhei}")
# win.geometry("1500x820")
# win.attributes('-fullscreen',True)
win.state('zoomed')    

lable1 = Label(win,text="",font=("",15," "),width=10)#,height=2)
lable1.grid(row=1,column=1,padx=7,pady=10)

lable1 = Label(win,text="",font=("",15," "),width=10)#,height=2)
lable1.grid(row=2,column=1,padx=7,pady=10)

# lable2 = Label(win,text="",font=("",15," "),width=10)#,height=2)
# lable2.grid(row=2,column=2,padx=7,pady=10)

lable3 = Label(win,text="",font=("",15," "),width=10)#,height=2)
lable3.grid(row=2,column=3,padx=7,pady=10)

# lable4 = Label(win,text="",font=("",15," "),width=10)#,height=2)
# lable4.grid(row=2,column=4,padx=7,pady=10)

# lable7 = Label(win,text="",font=("",15," "),width=10)#,height=2)
# lable7.grid(row=2,column=4,padx=7,pady=10)

cattel_feed_factory = Label(win,text="CATTLE FEED FACTORY",font=("Arial",15,"bold"))#,width=10,height=2)
cattel_feed_factory.grid(row=2,column=5,padx=7,pady=10)

kichha_bypass_road = Label(win,text="Kichha By Pass Road , Rudrapur (U.S. Nagar)",font=("Arial",15,""))#,width=10,height=2)
kichha_bypass_road.grid(row=4,column=5,padx=7,pady=10)

report = Label(win,text="LABORATORY ANALYSIS REPORT",font=("Arial",15,"bold"))#,width=10,height=2)
report.grid(row=6,column=5,padx=7,pady=10)

report = Label(win,text="(RAW MATERIAL)",font=("Arial",15,""))#,width=10,height=2)
report.grid(row=8,column=5,padx=7,pady=10)

lable8 = Label(win,text="",font=("",15," "),width=10)#,height=2)
lable8.grid(row=10,column=7,padx=7,pady=10)

# date = dt.datetime.now()
date_text = Label(win,text=f"Date : {str(date.today())} ",font=('arial',13,'bold'))
date_text.grid(row=10,column=9,padx=10,pady=10)

lable9 = Label(win,text="",font=("",15," "),width=10)#,height=2)
lable9.grid(row=12,column=2,padx=7,pady=10)

# lable10 = Label(win,text="",font=("",15," "),width=10)#,height=2)
# lable10.grid(row=13,column=2,padx=7,pady=10)

# lable11 = Label(win,text="",font=("",15," "),width=10)#,height=2)
# lable11.grid(row=14,column=2,padx=7,pady=10)

# def selectt():
#     button2.deselect()
#     pass

button1 = IntVar()
button2 = IntVar()
button3 = IntVar()
button4 = IntVar()
button5 = IntVar()
button6 = IntVar()

checkbutton1 = Checkbutton(win, text="D.O.R.B",variable=button1,onvalue=1,offvalue=0,height=2,width=30,command=Material_1)
checkbutton1.grid(row=14,column=2)

checkbutton2 = Checkbutton(win , text="RICE POLISH",variable=button2,onvalue=1,offvalue=0,height=2,width=20,command=Material_2)
checkbutton2.grid(row=15,column=2)

checkbutton3 = Checkbutton(win , text="Material_3",variable=button3,onvalue=1,offvalue=0,height=2,width=10,command=Material_3)
checkbutton3.grid(row=16,column=2)

checkbutton4 = Checkbutton(win , text="Material_4",variable=button4,onvalue=1,offvalue=0,height=2,width=10,command=Material_4)
checkbutton4.grid(row=17,column=2)

checkbutton5 = Checkbutton(win , text="Material_5",variable=button5,onvalue=1,offvalue=0,height=2,width=10,command=Material_5)
checkbutton5.grid(row=18,column=2)

checkbutton6 = Checkbutton(win , text="Material_6",variable=button6,onvalue=1,offvalue=0,height=2,width=10,command=Material_6)
checkbutton6.grid(row=19,column=2)

# material_name_lable = Label(win,text="Name of Material : ",font=("Arial",15,""))
# material_name_lable.grid(row=14,column=8)
# material_name_input = Entry(win,width=30)
# material_name_input.grid(row=14,column=9,padx=20,pady=12)

r_number_lable = Label(win,text="R. Number : ",font=("Arial",15,""))
r_number_lable.grid(row=15,column=8)
r_number_input = Entry(win,width=30)
r_number_input.grid(row=15,column=9,padx=20,pady=12)

moisture_lable = Label(win,text="Moisture : ",font=("Arial",15,""))
moisture_lable.grid(row=16,column=8)
moisture_input = Entry(win,width=30)
moisture_input.grid(row=16,column=9,padx=20,pady=12)

fat_lable = Label(win,text="Crude Fat : ",font=("Arial",15,""))
fat_lable.grid(row=17,column=8)
fat_input = Entry(win,width=30)
fat_input.grid(row=17,column=9,padx=20,pady=12)

protein_lable = Label(win,text="Crude Protein : ",font=("Arial",15,""))
protein_lable.grid(row=18,column=8)
protein_input = Entry(win,width=30)
protein_input.grid(row=18,column=9,padx=20,pady=12)

fibre_lable = Label(win,text="Crude Fibre : ",font=("Arial",15,""))
fibre_lable.grid(row=19,column=8)
fibre_input = Entry(win,width=30)
fibre_input.grid(row=19,column=9,padx=20,pady=12)

aish_lable = Label(win,text="Total Aish : ",font=("Arial",15,""))
aish_lable.grid(row=20,column=8)
aish_input = Entry(win,width=30)
aish_input.grid(row=20,column=9,padx=20,pady=12)

silica_lable = Label(win,text="Sand Silica : ",font=("Arial",15,""))
silica_lable.grid(row=21,column=8)
silica_input = Entry(win,width=30)
silica_input.grid(row=21,column=9,padx=20,pady=12)

analysis_lable = Label(win,text="Other Analysis : ",font=("Arial",15,""))
analysis_lable.grid(row=22,column=8)
analysis_input = Entry(win,width=30)
analysis_input.grid(row=22,column=9,padx=20,pady=12)


submit = Button(win,text="Submit",width=7,font=('arial',13,'bold'),command=executing)
submit.grid(row=17,column=5)

# if material_name_input.get() != '' or r_number_input.get() != '' :
#     submit = Button(win,text="Submit",width=15,font=('arial',13,'bold'),command=executing)
#     submit.grid(row=18,column=6)

reset = Button(win,text="Reset",width=7,font=('arial',13,'bold'),command=reset_input)
reset.grid(row=20,column=5)


win.mainloop()