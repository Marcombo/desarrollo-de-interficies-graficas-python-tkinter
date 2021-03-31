from tkinter import Tk, Label, TOP, BOTTOM, LEFT, RIGHT

root = Tk()
root.geometry("200x200")

etiqueta1 = Label(text="Etiqueta1")
etiqueta2 = Label(text="Etiqueta2")
etiqueta3 = Label(text="Etiqueta3")
etiqueta4 = Label(text="Etiqueta4")

##etiqueta1.pack(padx=10, pady=5)
##etiqueta2.pack(padx=10, pady=5)
##etiqueta3.pack(padx=10, pady=5)
##etiqueta4.pack(padx=10, pady=5)

etiqueta1.pack(side=TOP, pady=10)
etiqueta2.pack(side=BOTTOM, pady=10)
etiqueta3.pack(side=LEFT, padx=10)
etiqueta4.pack(side=RIGHT, padx=10)


