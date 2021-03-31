from tkinter import Tk, Label, Spinbox

def validar_edad(edad):
    return edad == "" or edad.isdigit() and len(edad) <= 2
                           
root = Tk()
root.resizable(False, False)

edad_label = Label(text="Edad:")
identificador = root.register(validar_edad)
vc = (identificador, '%P')
edad_entry = Spinbox(from_=1, to=99, width=3, bd=5, highlightcolor="red", highlightthickness=2, validate="key", validatecommand=vc)

edad_label.grid(row=0, column=0, sticky= "w", padx=20, pady=10)
edad_entry.grid(row=0, column=1, sticky= "w", padx=20, pady=10)
