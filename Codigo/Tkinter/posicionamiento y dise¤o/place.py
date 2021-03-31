from tkinter import Tk, Label

root = Tk()
root.geometry("200x200")

etiqueta = Label(text="Etiqueta")
#etiqueta.place(x=100, y=100, anchor="center")
etiqueta.place(relx=0.5, rely=0.5, anchor="center")

