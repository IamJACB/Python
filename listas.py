from tkinter import *

root = Tk()
root.title("Interfaz grafica de python")
root.geometry("600x600")

barraMenu = Menu(root)
root.config(menu=barraMenu)

archivoMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
archivoMenu.add_command(label="Nuevo Archivo")
archivoMenu.add_command(label="Nueva Ventana")
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir")

archivoEditar = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Editar", menu=archivoEditar)
archivoEditar.add_command(label="Deshacer")
archivoEditar.add_command(label="Rehacer")


archivoAyuda = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)
archivoAyuda.add_command(label="Acerca de...")
archivoAyuda.add_command(label="Ver Licencia...")


productos = Label(root, text="Productos")
productos.pack()

queso = IntVar()
lechuga = IntVar()

def agregar():
    listaProductos.insert(END, entrada.get())
    entrada.clipboard_clear()

def eliminar():
    e = listaProductos.curselection()
    listaProductos.delete(e)

def orden():
    lista=""
    if(queso.get()):
        lista += "Con queso"
    else:
        lista += "Sin queso"
    
    if(lechuga.get()):
        lista += "Con lechuga"
    else:
        lista += "Sin lechuga"
    imprimir.config(text=lista)

#Listar productos - crea una lista con unos productos
listaProductos = Listbox(root, width=50)
listaProductos.insert(0, "Carne")
listaProductos.insert(1, "Leche")
listaProductos.insert(2, "Arroz")
listaProductos.insert(3, "Jugo")
listaProductos.pack()


#Eliminar un producto
#listaProductos.delete(0)

entrada = Entry(root, bd=10)
entrada.pack()

boton = Button(root, text="Agregar", bd=10, command=agregar)
boton.pack()

boton1 = Button(root, text="Eliminar", bd=10, command=eliminar)
boton1.pack()

imagen = PhotoImage(file="h.gif")
Label(root, image=imagen).pack(side=LEFT)

frame = Frame(root)
frame.pack(side=RIGHT)
frame.config(bg="goldenrod3")

Label(frame, text="Como quieres tu hamburguesa " , bg="goldenrod3", font="Curier 15").pack(anchor="w")
Checkbutton(frame, text="Con Queso", variable=queso, onvalue=1, offvalue=0, bg="goldenrod3", font="Curier 15", command="orden").pack(anchor="w")
Checkbutton(frame, text="Con Lechuga", variable=lechuga, onvalue=1, offvalue=0, bg="goldenrod3", font="Curier 15", command="orden").pack(anchor="w")

imprimir = Label(frame, bg="red")
imprimir.pack()
imprimir.config(font="Curier 10")

root.mainloop()