import tkinter as tk
from tkinter.colorchooser import askcolor

root = tk.Tk()
root.title("Tkinter color")
root.geometry("300x150")

def cambiarcolor():
    colores = askcolor(title="Colores")
    root.configure(bg=colores[1])

tk.Button(root, text="Cambio de color", command=cambiarcolor).pack(expand=True)


root.mainloop()