import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor

root = tk.Tk()
root.title("Tkinter color")
root.geometry("300x150")

def seleccionar(opcion):    #La funcion recibe parametros e importando ttk
    print(opcion)

ttk.Button(root, text="Python", command=lambda: seleccionar("Python")).pack()
ttk.Button(root, text="Java", command=lambda: seleccionar("Java")).pack()
ttk.Button(root, text="C#", command=lambda: seleccionar("C#")).pack()

def cambiarcolor():
    colores = askcolor(title="Colores")
    root.configure(bg=colores[1])

tk.Button(root, text="Cambio de color", command=cambiarcolor).pack(expand=True)

root.mainloop()