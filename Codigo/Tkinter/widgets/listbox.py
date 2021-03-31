from tkinter import Tk, Button, Label, Listbox, StringVar

def traducir():
    entrada = lista_idiomas.curselection()
    if entrada != ():
        idioma = lista_idiomas.get(entrada)
        if idioma == "Inglés": traduccion = "Hi there"
        elif idioma == "Francés": traduccion = "Salut"
        elif idioma == "Italiano": traduccion = "Ciao"
        elif idioma == "Alemán": traduccion = "Hallo"
        palabra_traducida.configure(text=traduccion)

root = Tk()
root.resizable(False, False)

var_control_idiomas = StringVar(value="Inglés Francés Italiano Alemán")

palabra_original = Label(text="Hola", font=("Arial", 12, "bold italic"))
boton = Button(text="-->", command=traducir)
palabra_traducida = Label(text="¿?", font=("Arial", 12, "bold italic"))
lista_idiomas = Listbox(listvariable=var_control_idiomas, height=4, bd=3)


palabra_original.grid(row=0, column=0, padx= 5, pady=5)
boton.grid(row=0, column=1, padx= 5, pady=5)
palabra_traducida.grid(row=0, column=2, padx= 5, pady=5)
lista_idiomas.grid(row=1, column=1, pady=5)
