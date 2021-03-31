from tkinter import Tk, Label

root = Tk()
root.geometry("200x100")
root.configure(cursor="spider")

etiqueta = Label(relief="raised", text="Reloj", bitmap="hourglass", compound='left')
etiqueta.place(relx=0.5, rely=0.5, anchor="center")
