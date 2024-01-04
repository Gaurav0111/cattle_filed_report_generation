import main

def reset_input():
    # material_name_input.delete(0,END)
    main.r_number_input.delete(0,main.END)
    main.moisture_input.delete(0,main.END)
    main.fat_input.delete(0,main.END)
    main.protein_input.delete(0,main.END)
    main.fibre_input.delete(0,main.END)
    main.aish_input.delete(0,main.END)
    main.silica_input.delete(0,main.END)
    main.analysis_input.delete(0,main.END)
    main.checkbutton1.deselect()
    main.checkbutton2.deselect()
    main.checkbutton3.deselect()
    main.checkbutton4.deselect()
    main.checkbutton5.deselect()
    main.checkbutton6.deselect()
    
    