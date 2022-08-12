from tkinter import *

root = Tk()

imagen = PhotoImage(file="2.gif")
label = Label(root, image=imagen) 
label.pack()


"""
texto_nuevo= StringVar()
texto_nuevo.set("Python")

root.title("Bienvenidos")
root.iconbitmap("1.ico")  # Cambia el icono de la interdaz
root.config(width=400, height=300)

label = Label(root, text="Hola mundo")
label.place(x=100, y=70)
label.config(bg="aquamarine" , fg="green", font=("Curier", 20))


label = Label(root, text="Bienvenidos")
label.place(x=100, y=100)
label.config(bg="red" , fg="grey", font=("Curier", 20), textvariable=texto_nuevo)
"""



root.mainloop()