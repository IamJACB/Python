from tkinter import *  #Importa la libreria Tkinter que es la que permite ejecutar la intefaz

root=Tk()  #la raiz de tk

root.title("Interfaz grafica de python")
root.resizable(1,1)

root.iconbitmap("1.ico")  # Cambia el icono de la interdaz

miFrame = Frame(root)   #esto permite crear un espacio para modificar
miFrame.pack(fill="x", expand="1")  # Hace que la interfaz aparezca en el tamaño minimo
miFrame.config(width=150, height=150)  #da tamaño a la interfaz
miFrame.config(cursor="pirate")  #cambia el tipo del cursor
miFrame.config(bg="aquamarine")   #Color del background
miFrame.config(bd="20")  #Tamaño del borde
miFrame.config(relief="ridge")   #Tipo de borde



root.config(bd="20")
root.config(relief="ridge")


label = Label(root, text="Hola Mundo")
#label.pack()
label.place(x=100 , y=50)

label = Label(root, text="Bienvenidos a python")
#label.pack()
label.place(x=90 , y=40)

root.mainloop()