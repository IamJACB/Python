import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class App(tk.Tk):
    def __init__(self):
        super().__init__()


        #Configuracion de ventana
        self.title("Aplicacion")
        self.geometry("400x400")
        
        #Configuracion del label
        self.label = ttk.Label(self, text="Tkinter")
        self.label.pack()

        #Configuracion de boton
        self.boton = ttk.Button(self, text="Click aqui")
        self.boton["command"] = self.boton_accion
        self.boton.pack()

    def boton_accion(self):
        showinfo(title="Informacion", message="Hola mundo")

if __name__ == "__main__":
    app = App()
    app.mainloop()