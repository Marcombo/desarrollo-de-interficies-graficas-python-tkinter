from tkinter import Tk, Label, Entry
from random import randint

texto= "tkinter"
periodo = 400

def modifica_foco(campo_actual):
    estado = "EN CURSO"
    
    texto_campo_actual = campo_actual.get()
    if texto[0:len(texto_campo_actual)] != texto_campo_actual:
        estado = "KO"
    elif texto == campo1.get() == campo2.get() == campo3.get() == campo4.get():
        estado = "OK"

    if estado == "EN CURSO" :
        if randint(0, 1):
            nuevo_campo = campo_actual.tk_focusNext()
        else:
            nuevo_campo = campo_actual.tk_focusPrev()
            
        nuevo_campo.focus_set()
        root.after(periodo, modifica_foco, nuevo_campo)
    else:
        if estado == "OK":
            etiqueta = Label(text="¡PRUEBA SUPERADA!", fg = "green", font=("Arial", 20, "bold"))
        else :
            etiqueta = Label(text="¡PRUEBA NO SUPERADA!", fg = "red", font=("Arial", 20, "bold"))

        campo1.configure(state="disabled")
        campo2.configure(state="disabled")
        campo3.configure(state="disabled")
        campo4.configure(state="disabled")
        etiqueta.pack(padx=10, pady=10)

root = Tk()
root.title("Deletrea")
root.resizable(False, False)

campo1 = Entry(font=("Arial", 24, "bold"), bd=5, highlightcolor="red", highlightthickness=2)
campo2 = Entry(font=("Arial", 24, "bold"), bd=5, highlightcolor="red", highlightthickness=2)
campo3 = Entry(font=("Arial", 24, "bold"), bd=5, highlightcolor="red", highlightthickness=2)
campo4 = Entry(font=("Arial", 24, "bold"), bd=5, highlightcolor="red", highlightthickness=2)

campo1.pack(padx=10, pady=10)
campo2.pack(padx=10, pady=10)
campo3.pack(padx=10, pady=10)
campo4.pack(padx=10, pady=10)

campo1.focus_set()

modifica_foco(campo1)


