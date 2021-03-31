from tkinter import Tk, Label, Entry

root = Tk()
root.resizable(False, False)

etiqueta = Label(text="Campo:")
campo = Entry(relief ="sunken", bd=5)
etiqueta.pack(side="left", padx= 10, pady=20)
campo.pack(side="right", padx=10, pady=20)

