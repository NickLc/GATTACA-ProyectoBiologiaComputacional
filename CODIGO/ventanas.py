import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

from Bio_Tool import *
#==================================================================================

from tkinter.ttk import *

def get_name_esp():
	input_dir = 'data_gen/fasta/' 
	name = [seq[:-6] for seq in os.listdir(input_dir)]
	return name

def get_elegidos():
    """Muestra las especies elegidas"""
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
		messagebox.showerror('Error','Debe escoger al menos 2 especies')

def create_tree_upgma():
	secAli = leer_SecAli()
	tree = create_Tree(secAli, tipo = 'upgma')
	draw_Tree(tree)

def create_tree_nj():
	secAli = leer_SecAli()
	tree = create_Tree(secAli, tipo = 'nj')
	draw_Tree(tree)

#==================================================================================
#==================================================================================
class SampleApp(tk.Tk):

    def __init__(self, root):
        self.root = root
        self.root.geometry('600x600')
        self.root.title('WELCOME')
        self.root.resizable(1,1)
        self.root.config(cursor="arrow", bg="green", bd=15, relief="ridge")

        #--------------------------------------------------------------------------
        self.title_font = tkfont.Font(family='Calibri', size=18, weight="bold")
        #--------------------------------------------------------------------------
        #En el conteiner es un frame donde estaran los Widgets
        container = tk.Frame(self.root)
        container.pack(side="top", fill="both", expand=True)
        container.config(cursor="pirate",bg="lightgray",bd=25, relief="sunken")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #--------------------------------------------------------------------------

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(contenedor=container, controller=self)
            self.frames[page_name] = frame
            # Poner todas las ventanas en la misma ubicacion;
            # Poner la pagina principal como primero de la lista, porque 
            # esta estara siempre visible
            frame.grid(row=0, column=0, sticky="nsew")
        
        #--------------------------------------------------------------------------
        
        # Ventana Principal
        self.show_frame("StartPage")

        #--------------------------------------------------------------------------

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

#==================================================================================

class StartPage(tk.Frame):

    def __init__(self, contenedor, controller):
        tk.Frame.__init__(self, contenedor)        
        self.controller = controller

        label = tk.Label(self, text="Phylo-Zofia", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"), bg="green", anchor="center")
        button2 = tk.Button(self, text="Alineamiento",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()

#==================================================================================

class PageOne(tk.Frame):

    def __init__(self, contenedor, controller):
        tk.Frame.__init__(self, contenedor)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

#==================================================================================

class PageTwo(tk.Frame):

    def __init__(self, contenedor, controller):
        tk.Frame.__init__(self, contenedor)
        self.controller = controller
        
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        #label.pack(side="top", fill="x", pady=10)
        label.grid(column= 1, row = 0)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        #button.pack()
        button.grid(column=2, row=0)
        #----------------------------------------------------------------------- 
        #                      Boton de alimeamiento
        #----------------------------------------------------------------------- 

        label_ali = tk.Label(self, text="Alinear secuencias", font=("Calibri Bold", 14))
        boton_ali_simple = tk.Button(self, text = "Alineamiento Simple") 
        boton_ali_multiple = tk.Button(self, text = "Alineamiento Multiple") 
        label_ali.grid(column = 1, row = 1)
        boton_ali_simple.grid(column = 0, row = 2)
        boton_ali_multiple.grid(column = 2, row = 2)

        #----------------------------------------------------------------------- 
        #                      Boton de generar arbol
        #----------------------------------------------------------------------- 

        label_tree = tk.Label(self, text="General arbol", font=("Calibri Bold", 14))
        boton_get_tree_UPGMA = tk.Button(self, text = "UPGMA", command = create_tree_upgma) 
        boton_get_tree_Vecinos = tk.Button(self, text = "Union de vecinos", command = create_tree_nj) 
        
        label_tree.grid(column = 1,row = 3,sticky='NSEW')
        boton_get_tree_UPGMA.grid(column = 0, row = 4,sticky='EN')
        boton_get_tree_Vecinos.grid(column = 2, row = 4, sticky='E')

        
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)
        
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)
        self.grid_rowconfigure(2,weight=1)
        self.grid_rowconfigure(3,weight=1)
        self.grid_rowconfigure(4,weight=1)

        #----------------------------------------------------------------------- 
        #                       Abrimos una imagen
        #----------------------------------------------------------------------- 

        #im = Image.open('PhyloZofia_opt.jpg')
        # Convertimos la imagen a un objeto PhotoImage de Tkinter
        #photo = ImageTk.PhotoImage(im)  

        #cv = tk.Canvas(self, width=160, height=160)  
        #cv.create_image(0, 0, image = photo, anchor='nw')
        #cv.grid(column = 1, row = 4) 


#==================================================================================

if __name__ == "__main__":

    root = tk.Tk()
    app = SampleApp(root)
    root.mainloop()


#==============================================================
"""	sticky:
	
		NW 		N  		NE 
	WN						EN
	
	W 		  NSEW	    	E

	WS                      ES
		SW      S       SE
"""
