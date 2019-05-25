#========================================================================
# 7. Interfaz grafica

# In[1]:


from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

window = Tk()
window.title("App Biologia Computacional")
window.geometry('800x380')

#=======================================================================
frame0 = Frame(window) 

titulo = """PhyloZofia"""
 
#Titulo
lbl = Label(window, text=titulo, font=("Calibri Bold", 14))
lbl.grid(column=1, row=0)

#----------------------------------------------------------------------- 
frame0.grid(column = 1, row = 0)

#======================FRAME 1=================================

frame1 = Frame(window)
#-----------------------------------------------------------------------
#Etique especies
lbl = Label(frame1, text="Especies", font=("Calibri Bold", 14))
lbl.grid(column=1, row=1)
#-----------------------------------------------------------------------

# Botones y Check de las especies a seleccionar

check_state = []
num_especies = 10
#configuraciones
for i in range(num_especies):
    ch_st = BooleanVar()
    ch_st.set(0) #uncheck - aparesca deseleccionado
    check_state.append(ch_st)
    

check = []   #Lista de checks
boton = []   #Lista de botones
for i in range(num_especies):
    # checks
    ch = Checkbutton(frame1, text = 'Especie '+str(i+1), var = check_state[i])
    check.append(ch)
    # botones
    btn = Button(frame1, text="Info") 
    boton.append(btn)
    
#mostrat check
for i in range(num_especies):
    check[i].grid(column = 0, row = 3+i)
    boton[i].grid(column = 2, row = 3+i, rowspan=1)
    
#-----------------------------------------------------------------------   
frame1.grid(column = 0, row = 1)

#=======================FRAME 2=================================  

frame2=Frame(window)

#----------------------------------------------------------------------- 
#Boton de alimeamiento
label_ali = Label(frame2, text="Alinear secuencias", font=("Calibri Bold", 14))
boton_ali_simple = Button(frame2, text = "Alineamiento Simple") 
boton_ali_multiple = Button(frame2, text = "Alineamiento Multiple") 
label_ali.grid(column = 1, row = 0)
boton_ali_simple.grid(column = 0, row = 1)
boton_ali_multiple.grid(column = 2, row = 1)

#----------------------------------------------------------------------- 
#Boton de generar arbol
label_tree = Label(frame2, text="General arbol", font=("Calibri Bold", 14))
boton_get_tree_UPGMA = Button(frame2, text = "UPGMA") 
boton_get_tree_Vecinos = Button(frame2, text = "Union de vecinos") 

label_tree.grid(column = 1,row = 2)
boton_get_tree_UPGMA.grid(column = 0, row = 3)
boton_get_tree_Vecinos.grid(column = 2, row = 3)
#----------------------------------------------------------------------- 

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