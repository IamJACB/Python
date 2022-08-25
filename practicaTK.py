import tkinter as tk
from tkinter import ttk

root = tk.Tk()


def seleccionar(opcion):    #La funcion recibe parametros e importando ttk
    print(opcion)

ttk.Button(root, text="Python", command=lambda: seleccionar("Python")).pack()
ttk.Button(root, text="Java", command=lambda: seleccionar("Java")).pack()
ttk.Button(root, text="C#", command=lambda: seleccionar("C#")).pack()







root.mainloop()