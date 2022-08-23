from tkinter import *
from tkinter import messagebox, filedialog

def salir():
    i = messagebox.askquestion("Salir", "Estas seguro de salir?")
    if i == "yes":
        root.destroy()

def acerca():
    messagebox.showinfo("Informacion", "Creado e implementado por IamJACB")

def licencia():
    messagebox.showinfo("Licencia", "Licencia publica hasta el 2100")

def error():
    messagebox.showerror("Error", "Accion no disponible")

def deshacer():
    messagebox.askquestion("Seguro?", "Desea deshacer los cambios?")

def abrir():
    archivo1=filedialog.askopenfilename(title="abrir", initialdir="Descargas")
    print(archivo1)

root = Tk()
root.geometry("400x300")

barraMenu = Menu(root)
root.config(menu=barraMenu)

archivoMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
archivoMenu.add_command(label="Abrir Archivo", command=abrir)
archivoMenu.add_command(label="Nueva Ventana", command=error)
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=salir)

archivoEditar = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Editar", menu=archivoEditar)
archivoEditar.add_command(label="Deshacer", command=deshacer)
archivoEditar.add_command(label="Rehacer")


archivoAyuda = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)
archivoAyuda.add_command(label="Acerca de...", command=acerca)
archivoAyuda.add_command(label="Ver Licencia", command=licencia)




root.mainloop()