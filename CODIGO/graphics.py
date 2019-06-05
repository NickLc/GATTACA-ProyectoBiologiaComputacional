# -*- coding: utf-8 -*-

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
            text = 'Info',
            #command = self.__display_specie_info,
            command = self.__display_sequence,
            cursor = 'hand1'
        )
        self.sequence_button = Button(
            master,
            text = 'Sequence',
            command = self.__display_sequence,
            cursor = 'hand1'
        )
    
    def get_state(self):
        return self.state.get()
    
    def get_specie_name(self):
        return self.check_button.cget('text')
    
    def __display_specie_info(self):
        specie = self.check_button.cget('text')
        info_strng = 'This info shows nothing...' + specie
        messagebox.showinfo('Info about ' + specie, info_strng)
    
    def __display_sequence(self):
        specie_name = self.get_specie_name()
        #seq = get_seq()   # Optiene la secuencia utilizando BioTool

        windows_seq = Toplevel(self.master)
        windows_seq.title(specie_name)
        windows_seq.geometry('600x450')
        
        info_frame = Frame(windows_seq)
        title_label = Label(info_frame, text = specie_name, font = ('Calibri Bold', 14))
        title_label.grid(column = 1, row = 0)
        
        caract_seq = """
        ID = 19244
        Name = Protein
        ...
        ..
        .
        """

        info_seq = Label(info_frame, text = caract_seq)
        info_seq.grid(column = 1, row = 2)

        label_search_N = Label(info_frame, text = 'Search Nucleotido', font = ('Calibri Bold', 12))
        label_search_N.grid(column = 1, row = 3)
        num_seq =  Spinbox(info_frame, from_=0, to=100, width=5)
        num_seq.grid(column = 0, row = 4)
        label_nucle = Label(info_frame, text = '--')
        
        label_nucle.grid(column = 1, row = 4)
        boton_show_nucle = Button(info_frame, text='show', 
            command = lambda : label_nucle.configure(text = 'Aqui'))
        boton_show_nucle.grid(column = 2, row= 4)
        
        label_search_N = Label(info_frame, text = 'Search Block Sequence', font = ('Calibri Bold', 12))
        label_search_N.grid(column = 1, row = 5)
        fil = 6; col = 0
        spin_lim_inf_seq = Spinbox(info_frame, from_=0, to=100, width=5)
        spin_lim_inf_seq.grid(column = col, row = fil)
        spin_lim_sup_seq =  Spinbox(info_frame, from_=0, to=100, width=5)
        spin_lim_sup_seq.grid(column = col+1, row = fil)
        
        boton_block_seq = Button(info_frame, text='show', 
            command =lambda: txt_show_seq.insert(INSERT,'You text goes here'))
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
        self.info_button.grid(column = col + 1, row = rw, padx = 15, pady = 1)

class BioApp():

    def __init__(self):
        self.n_chsn = 0
        self.root = Tk()
        self.root.title('Phylozoophya')
        self.root.geometry('250x250')
        self.root.resizable(width = False, height = False)
        self.__add_welcome_frames()

        self.root.mainloop()

    def __add_welcome_frames(self):
        """Agrega marcos, etiquetas y botones para la ventana de bienvenida"""

        title_frame = Frame(self.root)
        title_label = Label(
            title_frame,
            text = 'Phylozophya',
            font = ('Calibri Bold', 14)
        )
        title_label.grid(column = 0, row = 1)
        title_frame.grid(column = 0, row = 1, padx = 65, pady = 30)

        team_frame = Frame(self.root)
        
        team_strng = 'writen by:\nLázaro Nick\nLeón Marco'
        team_label = Label(team_frame, text = team_strng, font = ('Calibri', 10))
        team_label.grid(column = 0, row = 1)

        team_frame.grid(column = 0, row = 2, padx = 10, pady = 10)

        button_frame = Frame(self.root)
        help_button = Button(
            button_frame,
            text = 'Help',
            command = self.__help_display,
            cursor = 'hand2'
        )
        go_button = Button(
            button_frame,
            text = 'Go!',
            activebackground = '#FF0011',
            command = self.__display_main_page,
            cursor = 'hand1'
        )
        help_button.grid(column = 0, row = 0, padx = 20, pady = 10)
        go_button.grid(column = 1, row = 0, padx = 20, pady = 10)
        button_frame.grid(column = 0, row = 3)

    
    def __add_main_page_frames(self):
        """Agrega los marcos, etiquetas y botones a la ventana principal"""
        self.root.resizable(width = True, height = True)
        self.__add_menubar()

        data_frame = Frame(self.root)

        option_frame = Frame(data_frame)
        data_label = Label(
            option_frame,
            text = 'Species',
            font = ('Calibri Bold', 14)
        )
        data_label.grid(column = 0, row = 0)

        names = get_species_names()
        options = []
        chk_row = 1
        
        for name in names:
            option = SpecieOption(option_frame,txt = name)
            options.append(option)
            option.grid(col = 0, rw = chk_row)
            chk_row = chk_row + 1
        option_frame.grid(column= 0, row=0, padx=20)

        selected_frame = Frame(data_frame)
        info_lbl = scrolledtext.ScrolledText(selected_frame, width=24, height=17)

        join_button = Button(
            selected_frame,
            text = 'Join',
            command = lambda : self.__join_chosen(options, info_lbl),
            cursor = 'hand1'
        )
        join_button.grid(column = 3, row = 0, pady = 4)
        info_lbl.grid(column = 3, row = 1)
        selected_frame.grid(column=1, row=0)

        data_frame.grid(column = 0, row = 0, padx=8)
        
        
        analysis_frame = Frame(self.root)
        analysis_label = Label(
            analysis_frame,
            text = 'Sequence analysis',
            font = ('Calibri Bold', 14)
        )
        analysis_label.grid(column = 0, row = 0)
        simple_alingmnt_button = Button(
            analysis_frame,
            text = 'Simple',
            command = self.__simple_alingmnt,
            cursor = 'hand1'
        )
        simple_alingmnt_button.grid(column = 1, row = 0)
        multiple_alingmnt_button = Button(
            analysis_frame,
            text = 'Multiple',
            command = self.__multiple_alingmnt,
            cursor = 'hand1'
        )
        multiple_alingmnt_button.grid(column = 2, row = 0)

        phylo_label = Label(
            analysis_frame,
            text = 'Phylogeny',
            font = ('Calibri Bold', 14)
        )
        phylo_label.grid(column = 0, row = 1)
        upgma_button = Button(
            analysis_frame,
            text = 'UPGMA',
            command = self.__create_upgma_tree,
            cursor = 'hand1'
        )
        upgma_button.grid(column = 1, row = 1)
        neighbor_button = Button(
            analysis_frame,
            text = 'Neighbor',
            command = self.__create__neighbor_tree,
            cursor = 'hand1'
        )
        neighbor_button.grid(column = 2, row = 1)

        photo_handle = Image.open('PhyloZofia_opt.jpg')
        photo = ImageTk.PhotoImage(photo_handle)
        cnv = Canvas(analysis_frame, width = 160, height = 160)  
        cnv.create_image(0, 0, image = photo, anchor = 'nw')
        cnv.grid(column = 1, row = 4) 

        analysis_frame.grid(column = 0, row = 1, padx = 10, pady=10)

        """
        clustering_frame = Frame(self.root)
        clustering_label = Label(
            clustering_frame,
            text = 'Clustering',
            font = ('Calibri Bold', 14)
        )
        clustering_label.grid(column = 0, row = 0)
        option_button = Button(
            clustering_frame,
            text = 'Option',
            command = self.__clustering_option
        )
        option_button.grid(column = 0, row = 1)
        clustering_frame.grid(column = 1, row = 1)"""

    def __get_chosen_species(self, optionList, v = False):
        chosen = []
        index = 0
        n = 0
        if v :
            name = []
        for option in optionList:
            if option.get_state() :
                chosen.append(index)
                n = n + 1
                if v :
                    name.append(option.get_specie_name())
            index = index + 1
        if v :
            return chosen, n, name
        return chosen, n

    def __join_chosen(self, optionList, info_lbl):
        chosen, self.n_chsn, name = self.__get_chosen_species(optionList, v = True)

        if not any(chosen) or len(chosen) == 1 :
            self.n_chsn = 0
            messagebox.showerror(
                title = 'Error!',
                message = 'You have to select at least two species'
            )
        
        else :
            string = 'Selected sequences: \n\n'
            string = string + '\n'.join(name)
            info_lbl.delete(1.0, END)
            info_lbl.insert(INSERT,string)
            join_Fasta(chosen)

    def __add_menubar(self):
        menubar = Menu(self.root)
        self.root.config(menu = menubar)
        options = Menu(menubar, tearoff = 0)
        options.add_separator()
        options.add_command(label = 'Exit', command = self.__exit)
        menubar.add_cascade(label = 'File', menu = options)
    
    def __exit(self):
        messagebox.showwarning('Closing', 'All generated data will be lost.')
        exit()

    def __simple_alingmnt(self):
        print(self.n_chsn)
        
        if self.n_chsn == 0 :
            messagebox.showerror('Error','You gotta push Join button.')            

        if self.n_chsn > 2 :
            messagebox.showerror('Error','Choose only 2 sequences.')
        else:
            alinear_Secuencias() 
        
    def __multiple_alingmnt(self):
        alinear_Secuencias()

    def __clustering_option(self):
        pass


    def __create_upgma_tree(self):
        secAli = leer_SecAli()
        tree = create_Tree(secAli, tipo = 'upgma')
        draw_Tree(tree)

    
    def __create__neighbor_tree(self):
        secAli = leer_SecAli()
        tree = create_Tree(secAli, tipo = 'nj')
        draw_Tree(tree)


    def __display_main_page(self):
        self.__clean_window()
        self.root.geometry('510x440+300+100')
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
        
        
