from tkinter import *
from tkinter.ttk import *

def crear_subVentana(Ventana_Padre):
    # Creamos una ventana hija de root
    otra_ventana = Toplevel(root)
    otra_ventana.title("Ventana hija")
    # Este es solo para decoracion
    etiqueta = Label(otra_ventana, text='Este es un ejemplo de transient')
    etiqueta.pack()
    otra_ventana.geometry("200x200+150+150")
    # Y ahora si llamamos a este metodo
    otra_ventana.transient(root)
    
def abrir_ventana():
    crear_subVentana(root)
    
root = Tk()
root.title("Ventana padre")
boton = Button(root, text="Abrir sub ventana", command=abrir_ventana)
boton.grid(column=0, row=0)
# Posicionamos las dos ventanas para que sea mas claro el ejemplo
root.geometry("400x400+100+100")
root.mainloop()