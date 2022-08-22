from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry("400x400")

w = Spinbox(root, values=("Python", "Html5", "Java", "Javascript"))
w.pack()


root.mainloop()