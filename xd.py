from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("100x100")
root.title("Jajajja")

Label(root, text="Queeee Ondaaaaa!", font=("Verdana", 15)).pack(side = TOP, pady=10)

foto = ImageTk.PhotoImage(file=r"C:\Users\PRACTICANTE.SISTEMAS\Documents\Juan\Python\Curso Python\3.gif")

photoimage = foto

boton1 = Button(root, text="No me hagas click!", image=photoimage, compound=LEFT).pack(side = TOP)
root.mainloop()