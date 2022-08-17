from tkinter import *


def mostrar ():
    if opciones.get()==1:
        label2.config(text="Haz elegido masculino")
    else:
        label2.config(text="Haz elegido Femenino")

def sumar():
    resultado.set(int(var1.get()) + int(var2.get()))

def restar():
    resultado.set(int(var1.get()) - int(var2.get()))

def dividir():
    resultado.set(int(var1.get()) / int(var2.get()))

def multiplicar():
    resultado.set(int(var1.get()) * int(var2.get()))

root = Tk() 
root.title("Interfaz grafica de python")
root.config(height=600, width=600)
opciones = IntVar()

frame= Frame(root)
frame.pack(expand=)



imagen = PhotoImage(file="2.gif")
label = Label(frame, image=imagen, cursor="pirate")
label.pack()


var1 = StringVar()
var2 = StringVar()
resultado = StringVar()

entrada1 = Entry(frame)
entrada1.pack()
entrada1.config(bd=5, bg="Aquamarine", font=("Curier, 10"), textvariable=var1)

entrada2 = Entry(frame)
entrada2.pack()
entrada2.config(bd=5, bg="Aquamarine", font=("Curier, 10"), textvariable=var2)

entrada3 = Entry(frame)
entrada3.pack()
entrada3.config(bd=5,  font=("Curier, 10"), textvariable=resultado, state="disable")

boton1 = Button(frame, text="Sumar")
boton1.pack()
boton1.config(bd=5, bg="red", font=("Curier, 10"), command=sumar)

boton2 = Button(frame, text="Restar")
boton2.pack()
boton2.config(bd=5, bg="red", font=("Curier, 10"), command=restar)

boton3 = Button(frame, text="Dividir")
boton3.pack()
boton3.config(bd=5, bg="red", font=("Curier, 10"), command=dividir)


boton4 = Button(frame, text="Multiplicar")
boton4.pack()
boton4.config(bd=5, bg="red", font=("Curier, 10"), command=multiplicar)

label1 = Label(root, text="Elige un  genero")
label1.pack()
label1.config(bg="Aquamarine")

Radiobutton(root, text="Masculino", variable=opciones, value=1, command=mostrar).pack()
Radiobutton(root, text="Femenino", variable=opciones, value=2, command=mostrar).pack()

label2=Label(root)
label2.pack()

root.mainloop()