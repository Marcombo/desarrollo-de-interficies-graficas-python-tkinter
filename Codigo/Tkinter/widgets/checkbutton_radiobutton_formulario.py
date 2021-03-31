from tkinter import Tk, Label, Button, Entry, Spinbox, OptionMenu, IntVar, StringVar, Radiobutton, Checkbutton, Frame, messagebox

edad_minima = 18
edad_maxima = 65

###################################################
#Funciones que se ejecutan al pulsar los botones
###################################################
def aceptar():
    selecciones=nombre=direccion=provincia=edad=sexo=aficiones=""
    
    nombre = nombre_entry.get()
    direccion = direccion_entry.get()
    provincia = var_provincia.get()
    edad = edad_entry.get()
    sexo = radio_var.get()
    aficion1 = check_var1.get()
    aficion2 = check_var2.get()
    aficion3 = check_var3.get()
    if aficion1: aficiones += "Música "
    if aficion2: aficiones += "Deporte "
    if aficion3: aficiones += "Lectura"
    
    if nombre:selecciones = "Nombre : "+nombre+"\n"
    if direccion:selecciones += "Dirección : "+direccion+"\n"
    if provincia != "Pulse para ver las permitidas":
        selecciones += "Provincia: "+provincia+"\n"
    selecciones += "Edad: "+edad+"\n"
    selecciones += "Sexo: "+sexo+"\n"
    if aficiones:selecciones += "Aficiones: "+aficiones+"\n"
    
    messagebox.showinfo("Selección", selecciones)

def cancelar():
    nombre_entry.delete(0, "end")
    direccion_entry.delete(0, "end")
    var_provincia.set("Pulse para ver las permitidas")
    edad_entry.delete(0, "end")
    edad_entry.insert(0, edad_minima)
    hombre_radiobutton.select()
    aficion1_checkbutton.deselect()
    aficion2_checkbutton.deselect()
    aficion3_checkbutton.deselect()

#Ventana principal
root = Tk()
root.title("Formulario")
root.resizable(True, False)
root.minsize(300, 100)


#Variables de control
var_provincia = StringVar()
radio_var = StringVar()
check_var1 = IntVar()
check_var2 = IntVar()
check_var3 = IntVar()

###################################################
#Creación de widgets
###################################################

#Creación de la etiqueta y el campo del nombre
nombre_label = Label(text="Nombre:")
nombre_entry = Entry(bd=5, highlightcolor="red", highlightthickness=2)

#Creación de la etiqueta y el campo de la dirección
direccion_label = Label(text="Dirección:")
direccion_entry = Entry(bd=5, highlightcolor="red", highlightthickness=2)

#Creación de la etiqueta y el campo de la provincia
provincia_label = Label(text="Provincia:")
provincia_menu = OptionMenu(root, var_provincia, "León", "Zamora", "Salamanca", "Valladolid", "Palencia")
var_provincia.set("Pulse para ver las permitidas")

#Creación de la etiqueta y el campo de la edad
edad_label = Label(text="Edad:")
edad_entry = Spinbox(from_=edad_minima, to=edad_maxima, width=3, bd=5, highlightcolor="red", highlightthickness=2)

#Creación de la etiqueta, los radiobuttons de sexo y el frame que los contiene
sexo_label = Label(text="Sexo:")
frame_radiobuttons = Frame()
hombre_radiobutton = Radiobutton(frame_radiobuttons, text="Hombre", variable=radio_var, value="Hombre")
mujer_radiobutton = Radiobutton(frame_radiobuttons, text="Mujer", variable=radio_var, value="Mujer")

#Creación de la etiqueta, los radiobuttons de las aficiones y el frame que los contiene
aficiones_label = Label(text="Aficiones:")
frame_checkbuttons = Frame()
aficion1_checkbutton = Checkbutton(frame_checkbuttons, text = "Música", variable = check_var1)
aficion2_checkbutton = Checkbutton(frame_checkbuttons, text = "Deporte", variable = check_var2)
aficion3_checkbutton = Checkbutton(frame_checkbuttons, text = "Lectura", variable = check_var3)

#creación de los botones
boton_aceptar = Button(text="ACEPTAR", command=aceptar)
boton_cancelar = Button(text="CANCELAR", command=cancelar)

###################################################
#Composición de los widgets en la interfaz
###################################################

#Composición de los widgets del nombre
nombre_label.grid(row=0, column=0, sticky= "w", padx=10, pady=10)
nombre_entry.grid(row=0, column=1, sticky= "ew", padx=10)

#Composición de los widgets de la dirección
direccion_label.grid(row=1, column=0, sticky= "w", padx=10, pady=10)
direccion_entry.grid(row=1, column=1, sticky= "ew", padx=10)

#Composición de los widgets de la provincia
provincia_label.grid(row=2, column=0, sticky= "w", padx=10, pady=10)
provincia_menu.grid(row=2, column=1, sticky= "w", padx=10)

#Composición de los widgets de la edad
edad_label.grid(row=3, column=0, sticky= "w", padx=10, pady=10)
edad_entry.grid(row=3, column=1, sticky= "w", padx=10)

#Permite que los campos de entrada de texto crezcan a lo ancho con la ventana
root.columnconfigure(1, weight=1)

#Composición de los widgets del sexo
sexo_label.grid(row=4, column=0, sticky= "w", padx=10, pady=10)
frame_radiobuttons.grid(row=4, column=1, sticky= "w", padx=10, pady=10)
hombre_radiobutton.pack(side= "left")
mujer_radiobutton.pack(side= "left")
hombre_radiobutton.select()

#Composición de los widgets de las aficiones
aficiones_label.grid(row=5, column=0, sticky= "w", padx=10, pady=10)
frame_checkbuttons.grid(row=5, column=1, sticky= "w", padx=10, pady=10)
aficion1_checkbutton.pack(side= "left")
aficion2_checkbutton.pack(side= "left")
aficion3_checkbutton.pack(side= "left")

#Composición de los widgets de los botones
boton_aceptar.grid(row=6, column=0, padx=10, pady=10, sticky= "W")
boton_cancelar.grid(row=6, column=1, padx=10, pady=10, sticky= "E")

root.mainloop()
