# -*- coding: utf-8 -*-
"""
 Autores: Lázaro Camasca Edson Nicks
           León Ríos Marco Naro
 Curso: CC471 - Biologia Computacional
 Proyecto : GATTACA
 Periodo : 2019 - I 
"""

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import scrolledtext
import os
from Bio_Tool import *

def get_species_names():
	input_dir = 'data_gen/fasta/' 
	names = [seq[:-6] for seq in os.listdir(input_dir)]
	return names

class SpecieOption():
    """
        La clase SpecieOption contiene en una fila las opciones para una especie,
        cono el checkButton(contiene etiqueta), botones. """

    """
        Autores: Lázaro Camasca Edson Nicks
                León Ríos Marco Naro
        Curso: CC471 - Biologia Computacional
        Proyecto : GATTACA
        Periodo : 2019 - I 
        """
    def __init__(self, master, txt):
        self.state = BooleanVar()
        self.master = master
        self.check_button = Checkbutton(
            master,
            text = txt,
            variable = self.state
        )
        self.info_button = Button(
            master,
            text = 'info',
            command = self.__display_specie_info,
            cursor = 'hand1'
        )
        self.sequence_button = Button(
            master,
            text = 'Seq',
            command = self.__display_sequence,
            cursor = 'hand1'
        )
    
    def get_state(self):
        return self.state.get()
    
    def get_specie_name(self):
        return self.check_button.cget('text')
    
    def __display_specie_info(self):
        
        specie_name = self.get_specie_name()
        
        image = ImageTk.PhotoImage(Image.open('Info/{}.png'.format(specie_name)))
        w = image.width()
        h = image.height()
        
        windows_info = Toplevel(self.master)
        windows_info.title(specie_name)
        windows_info.geometry("{}x{}+{}+{}".format(w, h, 100, 100))

        img = Label(windows_info, image=image)
        img.image = image
        img.grid(column = 0, row = 0)

    def __display_sequence(self):
        specie_name = self.get_specie_name()
        record = get_record_seq(specie_name)   # Optiene la secuencia utilizando BioTool

        windows_seq = Toplevel(self.master)
        windows_seq.title(specie_name)
        windows_seq.geometry('750x420')

        info_frame = Frame(windows_seq)
        title_label = Label(info_frame, text = specie_name, font = ('Calibri Bold', 14))
        title_label.grid(column = 1, row = 0)
        
        info_seq = Label(info_frame, text = str(record))
        info_seq.grid(column = 1, row = 2)

        label_search_N = Label(info_frame, text = 'Search Nucleotido', font = ('Calibri Bold', 12))
        label_search_N.grid(column = 1, row = 3)
        num_seq =  Spinbox(info_frame, from_=0, to=len(record.seq), width=5)
       
        num_seq.grid(column = 0, row = 4)
        label_nucle = Label(info_frame, text = '--')
        label_nucle.grid(column = 1, row = 4)

        boton_show_nucle = Button(info_frame, text='show', 
            command = lambda : label_nucle.configure(text = str(record.seq[int(num_seq.get())])))
        boton_show_nucle.grid(column = 2, row= 4)
        
        label_search_N = Label(info_frame, text = 'Search Block Sequence', font = ('Calibri Bold', 12))
        label_search_N.grid(column = 1, row = 5)
        fil = 6; col = 0
        
        var_Inf =IntVar()
        var_Inf.set(0)
        spin_Inf = Spinbox(info_frame, from_=0, to=len(record.seq)-1, 
                            width=5, textvariable=var_Inf)
        spin_Inf.grid(column = col, row = fil)
        
        var_Sup=IntVar()
        var_Sup.set(len(record.seq))
        spin_Sup =  Spinbox(info_frame, from_=int(spin_Inf.get()), to=len(record.seq), 
                            width=5,textvariable=var_Sup)
        spin_Sup.grid(column = col+1, row = fil)
        
        boton_block_seq = Button(info_frame, text='show', 
            command =lambda: txt_show_seq.insert(INSERT,
                '[{}:{}]'.format(int(spin_Inf.get()),int(spin_Sup.get()))
                +str(record.seq[int(spin_Inf.get()):int(spin_Sup.get())])+'\n'))
        
        boton_block_seq.grid(column = col+2, row= fil)
        
        label_show_seq = Label(info_frame, text = 'Sequence', font = ('Calibri Bold', 12))
        label_show_seq.grid(column=1, row=7, sticky='S')

        txt_show_seq = scrolledtext.ScrolledText(info_frame, width=50, height=6)
        txt_show_seq.grid(column=1, row=8,sticky='NSEW')
       
        boton_clear_seq = Button(info_frame, text='Clear',
            command = lambda: txt_show_seq.delete(1.0, END))
        boton_clear_seq.grid(column=1, row=9, sticky='NSEW')

        info_frame.grid(column = 0, row = 1, padx = 65, pady = 30)
        
        pass

    def grid(self, col, rw):
        self.check_button.grid(column = col, row = rw, sticky = 'w')
        self.info_button.grid(column = col + 1, row = rw, padx = 5, pady = 1)
        self.sequence_button.grid(column = col + 2, row = rw, padx = 5, pady = 1)
        

class ThreeOption():
    """
        Autores: Lázaro Camasca Edson Nicks
                León Ríos Marco Naro
        Curso: CC471 - Biologia Computacional
        Proyecto : GATTACA
        Periodo : 2019 - I 
        """
    def __init__(self, master):
        self.master = master

        self.phylo_label = Label(
            master,
            text = 'Phylogeny',
            font = ('Calibri Bold', 16),
            fg="#199FEB"
        )

        
        self.upgma_button = Button(
            master,
            text = 'UPGMA',
            command = self.__create_upgma_tree,
            cursor = 'hand1',
            font = ('Calibri Bold', 12),
            bg="#199FEB", fg="#FBFEFC"
        )
       
        self.neighbor_button = Button(
            master,
            text = 'Neighbor',
            command = self.__create__neighbor_tree,
            cursor = 'hand1',
            font = ('Calibri Bold', 12),
            bg="#199FEB", fg="#FBFEFC"
        )
        

    def __create_upgma_tree(self):
        secAli = leer_SecAli()
        tree = create_Tree(secAli, tipo = 'upgma')
        draw_Tree(tree)
    
    def __create__neighbor_tree(self):
        secAli = leer_SecAli()
        tree = create_Tree(secAli, tipo = 'nj')
        draw_Tree(tree)

    def grid(self, col, rw):
        self.phylo_label.grid(column = col, row = rw, padx=10)
        self.upgma_button.grid(column = col+1, row = rw)
        self.neighbor_button.grid(column = col+2, row = rw)

class AlingOption():
    """
        AlingOption es la clase que contiene la etiqueta(title) y botones para análisis del alineamiento
        recibe un frame o ventana, y la lista de opciones (sequencias escogidas)"""
    """
        Autores: Lázaro Camasca Edson Nicks
                León Ríos Marco Naro
        Curso: CC471 - Biologia Computacional
        Proyecto : GATTACA
        Periodo : 2019 - I 
        """
    def __init__(self, master):
        
        self.master = master

        self.title_analysis_aling = Label(
            master,
            text = 'Sequence analysis',
            font = ('Calibri Bold', 16),
            fg="#199FEB"
        )
       
        self.multiple_alingmnt_button = Button(
            master,
            text = 'Multiple',
            command = self.__multiple_alingmnt,
            cursor = 'hand1',
            font = ('Calibri Bold', 12),
            bg="#199FEB", fg="#FBFEFC"
        )


    def __multiple_alingmnt(self):
            # Cantidad de especies escogidas
        n_chose = 1
        """print("La cantidad de especies escogidas es:", n_chose )
        """
        # La verificacion se realizara con el archivo fasta
        if n_chose  == 0 :
            messagebox.showerror('Error','You gotta push Join button.')            

        elif n_chose  > 2 :
            messagebox.showerror('Error','Choose only 2 sequences.')
        else:
            alinear_Secuencias() 
            aln = leer_SecAli()

            title_windows = 'Aligment Multiple'
            windows_seq = Toplevel(self.master)
            windows_seq.title(title_windows)
            windows_seq.geometry('680x350')
            
            info_frame = Frame(windows_seq)
            title_label = Label(info_frame, text = title_windows, font = ('Calibri Bold', 14))

            chosen_scroll = scrolledtext.ScrolledText(info_frame, width=75, height=10)
            chosen_scroll.delete(1.0, END)
            chosen_scroll.insert(INSERT,aln)

            title_label.grid(column = 0, row = 0)
            chosen_scroll.grid(column = 0, row = 1)
            info_frame.grid(column = 0, row = 1, padx = 65, pady = 30)

    def grid(self, col, rw):
        self.title_analysis_aling.grid(column = col, row = rw, padx=10, pady=4)
        self.multiple_alingmnt_button.grid(column = col+2, row = rw, padx=10, pady=4)

class BioApp():
    """
        Autores: Lázaro Camasca Edson Nicks
                León Ríos Marco Naro
        Curso: CC471 - Biologia Computacional
        Proyecto : GATTACA
        Periodo : 2019 - I 
        """
    def __init__(self):
        self.chosen_species = []   #Lista de diccionarios, {index, name}
        self.root = Tk()
        self.root.title('GATTACA')
        
        background_image = ImageTk.PhotoImage(Image.open('data_gen/gattaca-logo.png'))
        w = background_image.width()
        h = background_image.height()
        self.root.geometry("{}x{}+{}+{}".format(w, h+150, 100, 100))
        background_label = Label(self.root, image=background_image)
        background_label.grid(column = 0, row = 1)

        self.root.resizable(width = False, height = False)
        self.__add_welcome_frames()

        self.root.mainloop()


    def __add_welcome_frames(self):
        """Agrega marcos, etiquetas y botones para la ventana de bienvenida"""

        team_frame = Frame(self.root)
        
        team_strng = 'writen by:\nLázaro Nick\nLeón Marco'
        team_label = Label(team_frame, text = team_strng, font = ('Calibri Bold', 12), fg="#4B6BFF")
        team_label.grid(column = 0, row = 1)

        team_frame.grid(column = 0, row = 2, padx = 10, pady = 10)

        button_frame = Frame(self.root)
        help_button = Button(
            button_frame,
            text = 'Help',
            command = self.__help_display,
            cursor = 'hand2',
            font = ('Calibri Bold', 12),
            bg="#01EB4C", fg="#EBFFDE"
        )
        go_button = Button(
            button_frame,
            text = 'Go!',
            activebackground = '#FF0011',
            command = self.__display_main_page,
            cursor = 'hand1',
            font = ('Calibri Bold', 12),
            bg="#01EB4C", fg="#EBFFDE"
        )
        help_button.grid(column = 0, row = 0, padx = 20, pady = 10)
        go_button.grid(column = 1, row = 0, padx = 20, pady = 10)
        button_frame.grid(column = 0, row = 3)

    
    def __add_main_page_frames(self):
        """Agrega los marcos, etiquetas y botones a la ventana principal"""
        self.root.resizable(width = True, height = True)
        self.__add_menubar()
        self.chosen_species = []

        # Frame donde se ubican las especies a escoger
        data_frame = Frame(self.root)   

        option_frame = Frame(data_frame)
        title_data_frame = Label(         # Titulo del frame data
            option_frame,
            text = 'Species',
            font = ('Calibri Bold', 14),
            fg="#199FEB"
        )
        title_data_frame.grid(column = 0, row = 0)

        names = get_species_names() 
            # Obtenemos los nombres de las especies a partir del directorio    
        specie_list = []
        chk_row = 1
        
        for name in names:
            # Creamos un objeto SpecieOption 
            option = SpecieOption(option_frame,txt = name) 
            specie_list.append(option)
            option.grid(col = 0, rw = chk_row)
            chk_row = chk_row + 1
        option_frame.grid(column= 0, row=0, padx=20)

        
        # Frame donde se ubican las especies escogidas
        selected_frame = Frame(data_frame)
        chosen_scroll = scrolledtext.ScrolledText(selected_frame, width=24, height=17)

        join_button = Button(
            selected_frame,
            text = 'Join',
            command = lambda : self.__join_chosen(specie_list, chosen_scroll),
            cursor = 'hand1',
            font = ('Calibri Bold', 12),
            bg="#199FEB", fg="#FBFEFC"
        )

        join_button.grid(column = 3, row = 0, pady = 4)
        chosen_scroll.grid(column = 3, row = 1)
        selected_frame.grid(column=1, row=0)

        data_frame.grid(column = 0, row = 0, padx=8)
        
        # Frame donde se ubican las opciones para el análisis.
        analysis_frame = Frame(self.root)

        
            # Creamos un objeto AlingOption
        aling = AlingOption(analysis_frame)
        aling.grid(col = 0, rw = 0)

            # Creamos un objeto ThreeOption
        three = ThreeOption(analysis_frame)
        three.grid(col = 0, rw = 1)

        analysis_frame.grid(column = 0, row = 1, padx = 10, pady=10)



    def __get_chosen_species(self, optionList):
        """
            Revisa cada opcion y si tiene un check lo agrega a la lista de elegidos
            Recibe la lista de todas las secuencias
            Retorna una lista de diccionarios de los elegidos {'index', 'name'} """

        index = 0
        chosen_species = []
            
        for option in optionList:

            if option.get_state() :
                name = option.get_specie_name()
                specie_chose = {'index': index, 'name':name}
                chosen_species.append(specie_chose)

            index = index + 1
        
        return chosen_species


    def __join_chosen(self, optionList, chosen_scroll):
        
        self.chosen_species = self.__get_chosen_species(optionList)

        if not any(self.chosen_species) or len(self.chosen_species) == 1 :
            self.chosen_species.clear()

            messagebox.showerror(
                title = 'Error!',
                message = 'You have to select at least two species'
            )
        
        else :        
            # Muestra las especies elegidas en pantalla
            name_chose = [i['name'] for i in self.chosen_species ]
            string = 'Selected sequences: \n\n'
            string = string + '\n'.join(name_chose)
            chosen_scroll.delete(1.0, END)
            chosen_scroll.insert(INSERT,string)

            # Genera el archivo fasta con las secuencias elegidas
            index = [i['index'] for i in self.chosen_species ]
            join_Fasta(index)


    def __add_menubar(self):
        menubar = Menu(self.root)
        self.root.config(menu = menubar)
        specie_list = Menu(menubar, tearoff = 0)
        specie_list.add_separator()
        specie_list.add_command(label = 'Exit', command = self.__exit)
        menubar.add_cascade(label = 'File', menu = specie_list)


    def __exit(self):
        messagebox.showwarning('Closing', 'All generated data will be lost.')
        exit()


    def __display_main_page(self):
        self.__clean_window()
        self.root.geometry('510x450+300+100')
        self.__add_main_page_frames()


    def __help_display(self):
        help_strng = 'Information that doesn\'t help at all...'
        messagebox.showinfo('Help', help_strng)
    

    def __clean_window(self):
        """Destruye los objetos en la ventana root para limpiarla."""
        for children in self.root.winfo_children():
            children.destroy()


if __name__ == '__main__':
    appx = BioApp()
        