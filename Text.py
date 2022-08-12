from tkinter import *

root=Tk()

texto = Text(root) 
texto.pack()
texto.config(width=40, height=15, padx=15, pady=15, bg="#C83819", font="Curier, 10")

label = Label(root, text="Escribe aqui: ")
label.pack()
label.config(bg="aquamarine", font="Curier, 20")






root.mainloop()