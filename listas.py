from tkinter import *

root = Tk()
root.geometry("400x400")

productos = Label(root, text="Productos")
productos.pack()


def agregar():
    listaProductos.insert(END, entrada.get())

def eliminar():
    e = listaProductos.curselection()
    listaProductos.delete(e)

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





root.mainloop()