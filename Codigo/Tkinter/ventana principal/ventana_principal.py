from tkinter import Tk, Label

root = Tk()
root.geometry("200x50")
root.resizable(True, False)
root.minsize(50, 50)
root.maxsize(400, 50)

etiqueta = Label(text="\n  ¡Hola Mundo!  \n")
etiqueta.pack()
