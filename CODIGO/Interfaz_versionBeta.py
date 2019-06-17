from Bio_Tool import *
#========================================================================
# 7. Interfaz grafica

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from PIL import Image, ImageTk

def get_name_esp():
	input_dir = 'data_gen/fasta/' 
	name = [seq[:-6] for seq in os.listdir(input_dir)]
	return name

def get_elegidos():
    """Retorna una lista con las especies elegidas"""
    elegidos = []
    for i in range(len(check_state)):
        if check_state[i].get() == 1:
            elegidos.append(i)
    return elegidos

def join_Sec():
	elegidos = get_elegidos()
	if len(elegidos) > 1 :
		mens_elegidas = [str(sec+1) for sec in elegidos]
		mens_elegidas = ",".join(mens_elegidas)
		label_mesj_Join.configure(text=mens_elegidas)
		join_Fasta(elegidos)

	if len(elegidos) < 2 :
		messagebox.showerror('Error','Escoger más de 2 especies')

def alineamiento_Multiple():
    alinear_Secuencias()

def alineamiento_Simple():
    elegidos = get_elegidos()
    if len(elegidos) != 2 :
        messagebox.showerror('Error','Escoger solo 2 secuencias')
    else:
        alinear_Secuencias()        

def create_tree_upgma():
	secAli = leer_SecAli()
	tree = create_Tree(secAli, tipo = 'upgma')
	draw_Tree(tree)

def create_tree_nj():
	secAli = leer_SecAli()
	tree = create_Tree(secAli, tipo = 'nj')
	draw_Tree(tree)

#=======================================================================

window = Tk()
window.title("App Biologia Computacional")
window.geometry('850x380')


#=======================================================================
frame0 = Frame(window) 

titulo = """PhyloZofia"""
 
#Titulo
lbl_tile = Label(frame0, text=titulo, font=("Calibri Bold", 14))
lbl_tile.grid(column=1, row=0)
#----------------------------------------------------------------------- 
frame0.grid(column = 1, row = 0)

#======================FRAME 1=================================

frame1 = Frame(window)
#-----------------------------------------------------------------------
#Etique especies
lbl = Label(frame1, text="Especies", font=("Calibri Bold", 14))
lbl.grid(column=0, row=1)
#-----------------------------------------------------------------------

# Botones y Check de las especies a seleccionar

num_especies = 10
check = []   #Lista de checks
check_state = []   #Estado de cada checks
boton = []   #Lista de botones
name_check = get_name_esp()

# Configuraciones
for i in range(num_especies):
    # checks
    state = IntVar()    
    ch = Checkbutton(frame1, text = str(i+1)+") "+name_check[i], var=state, width=32)
    check_state.append(state)
    check.append(ch)

    # botones
    btn = Button(frame1, text="Info", width=10) 
    boton.append(btn)

boton_join_Sec = Button(frame1, text="Unir Secuencias", command=join_Sec)   
label_mesj_Join = Label(frame1, text = "Secuencias unidas 0", font=("Calibri Bold", 10))

# Mostrar check
k_row = 3
for i in range(num_especies):
    k_row += 1
    check[i].grid(column=0, row=k_row)
    boton[i].grid(column=1, row=k_row, rowspan=1)
  
boton_join_Sec.grid(column=1, row=k_row+1)	
label_mesj_Join.grid(column=1, row=k_row+2)
#-----------------------------------------------------------------------   
frame1.grid(column = 0, row = 1)

#=======================FRAME 2=================================  

frame2=Frame(window)

#----------------------------------------------------------------------- 
#Boton de alimeamiento
label_ali = Label(frame2, text="Alinear secuencias", font=("Calibri Bold", 14))
boton_ali_simple = Button(frame2, text = "Alineamiento Simple", command=alineamiento_Simple) 
boton_ali_multiple = Button(frame2, text = "Alineamiento Multiple", command= alineamiento_Multiple) 
label_ali.grid(column = 1, row = 0)
boton_ali_simple.grid(column = 0, row = 1)
boton_ali_multiple.grid(column = 2, row = 1)

#----------------------------------------------------------------------- 
#Boton de generar arbol
label_tree = Label(frame2, text="General arbol", font=("Calibri Bold", 14))
boton_get_tree_UPGMA = Button(frame2, text = "UPGMA", command = create_tree_upgma) 
boton_get_tree_Vecinos = Button(frame2, text = "Union de vecinos", command = create_tree_nj) 

label_tree.grid(column = 1,row = 2)
boton_get_tree_UPGMA.grid(column = 0, row = 3)
boton_get_tree_Vecinos.grid(column = 2, row = 3)

#----------------------------------------------------------------------- 
# abrimos una imagen
im = Image.open('PhyloZofia_opt.jpg')
# Convertimos la imagen a un objeto PhotoImage de Tkinter
photo = ImageTk.PhotoImage(im)  

cv = Canvas(frame2, width=160, height=160)  
cv.create_image(0, 0, image = photo, anchor='nw')
cv.grid(column = 1, row = 4) 

frame2.grid(column = 2, row = 1)
#----------------------------------------------------------------------- 
window.mainloop()