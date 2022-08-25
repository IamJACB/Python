import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.colorchooser import askcolor

root = Tk()
root.geometry("330x310")
root.title("Calculadora")

i = 0

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
    archivo1=filedialog.askopenfilename(title="abrir", initialdir="Descargas", filetypes=((("Archivos pdf", "*.pdf")),("Archivo de texto","*.txt")))
    print(archivo1)

def click(valor):
    global i
    entrada.insert(i, valor)
    i += 1

def borrar():
    entrada.delete(0, END)
    i = 0

def operaciones():
    operacion = entrada.get()
    resultado = eval(operacion)
    entrada.delete(0, END)
    entrada.insert(0, resultado)
    i = 0

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

#Entrada de datos 

entrada = Entry(root, font="Curier 20")
entrada.config(bd=5, relief="sunken")
entrada.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

#Creacion de botones

boton1= Button(root, text="1", width=5, height=2, command=lambda:click(1))
boton1.config(bd="2", bg="aquamarine")
boton2= Button(root, text="2", width=5, height=2, command=lambda:click(2))
boton2.config(bd="2", bg="aquamarine")
boton3= Button(root, text="3", width=5, height=2, command=lambda:click(3))
boton3.config(bd="2", bg="aquamarine")
boton4= Button(root, text="4", width=5, height=2, command=lambda:click(4))
boton4.config(bd="2", bg="aquamarine")
boton5= Button(root, text="5", width=5, height=2, command=lambda:click(5))
boton5.config(bd="2", bg="aquamarine")
boton6= Button(root, text="6", width=5, height=2, command=lambda:click(6))
boton6.config(bd="2", bg="aquamarine")
boton7= Button(root, text="7", width=5, height=2, command=lambda:click(7))
boton7.config(bd="2", bg="aquamarine")
boton8= Button(root, text="8", width=5, height=2, command=lambda:click(8))
boton8.config(bd="2", bg="aquamarine")
boton9= Button(root, text="9", width=5, height=2, command=lambda:click(9))
boton9.config(bd="2", bg="aquamarine")
boton0= Button(root, text="0", width=16, height=2, command=lambda:click(0))
boton0.config(bd="2", bg="aquamarine")

boton_borrar= Button(root, text="Borrar", width=5, height=2, command=lambda:borrar())
boton_borrar.config(bd="2", bg="red")
boton_parentesis1= Button(root, text="(", width=5, height=2, command=lambda:click("("))
boton_parentesis1.config(bd="2", bg="red")
boton_parentesis2= Button(root, text=")", width=5, height=2, command=lambda:click(")"))
boton_parentesis2.config(bd="2", bg="red")
boton_punto= Button(root, text=".", width=5, height=2, command=lambda:click("."))
boton_punto.config(bd="2", bg="aquamarine")

boton_suma= Button(root, text="+", width=5, height=2, command=lambda:click("+"))
boton_suma.config(bd="2", bg="purple")
boton_resta= Button(root, text="-", width=5, height=2, command=lambda:click("-"))
boton_resta.config(bd="2", bg="purple")
boton_div= Button(root, text="/", width=5, height=2, command=lambda:click("/"))
boton_div.config(bd="2", bg="purple")
boton_mult= Button(root, text="*", width=5, height=2, command=lambda:click("*"))
boton_mult.config(bd="2", bg="purple")
boton_igual= Button(root, text="=", width=5, height=2, command=lambda:operaciones())
boton_igual.config(bd="2", bg="purple")

#Colocar botones

boton_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_parentesis1.grid(row=1, column=1, padx=5, pady=5)
boton_parentesis2.grid(row=1, column=2, padx=5, pady=5)
boton_punto.grid(row=1, column=3, padx=5, pady=5)

boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
boton_mult.grid(row=1, column=3, padx=5, pady=5)


boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_suma.grid(row=2, column=3, padx=5, pady=5)

boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton_resta.grid(row=3, column=3, padx=5, pady=5)

boton0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
boton_punto.grid(row=5, column=2, padx=5, pady=5)
boton_igual.grid(row=5, column=3, padx=5, pady=5)
boton_div.grid(row=4, column=3, padx=5, pady=5)



















root.mainloop()