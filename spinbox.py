from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry("400x300")

w = Spinbox(root, values=("Python", "Html5", "Java", "Javascript"))
w.pack()


e = Spinbox(root, values=("Nodejs", "Html5", "Java", "Javascript"))
e.pack()



root.mainloop()