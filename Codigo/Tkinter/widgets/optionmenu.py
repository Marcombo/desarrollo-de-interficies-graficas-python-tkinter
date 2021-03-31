from tkinter import Tk, Label, Button, Entry, Spinbox, OptionMenu, StringVar

edad_minima = 18
edad_maxima = 65

def aceptar():
    selecciones = ""
    
    nombre = nombre_entry.get()
    direccion = direccion_entry.get()
    provincia = var_provincia.get()
    edad = edad_entry.get()
    if nombre:selecciones = "Nombre : "+nombre+"\n"
    if direccion:selecciones += "Dirección : "+direccion+"\n"
    if provincia != "Pulse para ver las permitidas":
        selecciones += "Provincia : "+provincia+"\n"
    selecciones += "Edad: "+edad
    selecciones_label.config(text=selecciones)

def cancelar():
    nombre_entry.delete(0, "end")
    direccion_entry.delete(0, "end")
    var_provincia.set("Pulse para ver las permitidas")
    edad_entry.delete(0, "end")
    edad_entry.insert(0, 18)
    selecciones_label.config(text="")

root = Tk()
root.title("Formulario")
root.resizable(True, False)
root.minsize(300, 100)

var_provincia = StringVar()

nombre_label = Label(text="Nombre:")
nombre_entry = Entry(bd=5, highlightcolor="red", highlightthickness=2)
direccion_label = Label(text="Dirección:")
direccion_entry = Entry(bd=5, highlightcolor="red", highlightthickness=2)
provincia_label = Label(text="Provincia:")
provincia_menu = OptionMenu(root, var_provincia, "León", "Zamora", "Salamanca", "Valladolid", "Palencia")
var_provincia.set("Pulse para ver las permitidas")
edad_label = Label(text="Edad:")
edad_entry = Spinbox(from_=edad_minima, to=edad_maxima, width=3, bd=5, highlightcolor="red", highlightthickness=2)
selecciones_label = Label(text="", padx=10, justify="left")
boton_aceptar = Button(text="ACEPTAR", command=aceptar)
boton_cancelar = Button(text="CANCELAR", command=cancelar)

nombre_label.grid(row=0, column=0, sticky= "w", padx=10, pady=10)
nombre_entry.grid(row=0, column=1, sticky= "ew", padx=10)
direccion_label.grid(row=1, column=0, sticky= "w", padx=10, pady=10)
direccion_entry.grid(row=1, column=1, sticky= "ew", padx=10)
provincia_label.grid(row=2, column=0, sticky= "w", padx=10, pady=10)
provincia_menu.grid(row=2, column=1, sticky= "w", padx=10)
edad_label.grid(row=3, column=0, sticky= "w", padx=10, pady=10)
edad_entry.grid(row=3, column=1, sticky= "w", padx=10)

root.columnconfigure(1, weight=1)

selecciones_label.grid(row=4, column=0, columnspan=2, sticky= "W")
boton_aceptar.grid(row=5, column=0, padx=10, pady=10, sticky= "W")
boton_cancelar.grid(row=5, column=1, padx=10, pady=10, sticky= "E")

root.mainloop()
