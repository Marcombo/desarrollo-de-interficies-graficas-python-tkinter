from gestion_clientes import *
from tkinter import Tk, Label, Entry, Button, Menu, Text, PhotoImage, Scrollbar, messagebox, Toplevel

datos_modificados = False

def mostrar_resultado_operacion(mensaje):
    area_texto.configure(state="normal")
    area_texto.delete(1.0, "end")
    area_texto.insert(1.0, mensaje)
    area_texto.configure(state="disabled")

#---------------------------------------------------------------------
#-------------------- FUNCIONES GESTIÓN DE BOTONES -------------------- 
#---------------------------------------------------------------------

def aceptar_alta():
    global datos_modificados
    
    dni = dni_entry.get()
    nombre_cliente = nombre_cliente_entry.get()
    nombre_perro = nombre_perro_entry.get()
    raza = raza_entry.get()
    cliente = obtener_cliente(dni)

    if cliente != None:
        dni_entry.delete(0, "end")
        dni_entry.focus()
    else:
        alta_cliente(dni, nombre_cliente, nombre_perro, raza)
        datos_modificados = True
        ventana_auxiliar.destroy()
        cliente = obtener_cliente(dni)
        tabla_cliente = informacion_cliente(cliente)
        mostrar_resultado_operacion("Cliente dado de alta correctamente\n\n"+tabla_cliente)

def aceptar_baja():
    global datos_modificados
    
    dni = dni_entry.get()
    cliente = obtener_cliente(dni)
    if cliente == None:
        dni_entry.delete(0, "end")
        dni_entry.focus()
    else:
        baja_cliente(cliente)
        datos_modificados = True
        ventana_auxiliar.destroy()
        mostrar_resultado_operacion("Cliente dado de baja correctamente")

def aceptar_modificacion():
    global datos_modificados
    
    dni = dni_entry.get()
    nombre_cliente = nombre_cliente_entry.get()
    nombre_perro = nombre_perro_entry.get()
    raza = raza_entry.get()

    cliente = obtener_cliente(dni)
    modificacion_cliente(cliente, nombre_cliente, nombre_perro, raza)
    
    datos_modificados = True
    ventana_auxiliar.destroy()
    tabla_cliente = informacion_cliente(cliente)
    mostrar_resultado_operacion("Cliente modificado correctamente\n\n"+tabla_cliente)

def aceptar_dni_modificacion():
    global nombre_cliente_entry, nombre_perro_entry, raza_entry

    dni = dni_entry.get()
    cliente = obtener_cliente(dni)
    if cliente == None:
        dni_entry.delete(0, "end")
        dni_entry.focus()
    else:
        dni_entry.configure(state="disabled")
        
        nombre_cliente_label = Label(ventana_auxiliar, text="Nombre cliente:")
        nombre_cliente_entry = Entry(ventana_auxiliar, bd=5, highlightcolor="red", highlightthickness=2)
        nombre_perro_label = Label(ventana_auxiliar, text="Nombre perro:")
        nombre_perro_entry = Entry(ventana_auxiliar, bd=5, highlightcolor="red", highlightthickness=2)
        raza_label = Label(ventana_auxiliar, text="Raza:")
        raza_entry = Entry(ventana_auxiliar, bd=5, highlightcolor="red", highlightthickness=2)

        nombre_cliente_entry.insert(0, cliente.nombre)
        nombre_perro_entry.insert(0, cliente.perro.nombre)
        raza_entry.insert(0, cliente.perro.raza)

        boton_aceptar.configure(command=aceptar_modificacion)

        nombre_cliente_label.grid(row=2, column=1, sticky= "W", padx=10, pady=10)
        nombre_cliente_entry.grid(row=2, column=2, padx=10)
        nombre_perro_label.grid(row=3, column=1, sticky= "W", padx=10, pady=10)
        nombre_perro_entry.grid(row=3, column=2, padx=10)
        raza_label.grid(row=4, column=1, sticky= "W", padx=10, pady=10)
        raza_entry.grid(row=4, column=2, padx=10)
        boton_aceptar.grid(row=5, column=1, padx=10, pady=10, sticky= "W")
        boton_cancelar.grid(row=5, column=2, padx=10, pady=10, sticky= "E")

def aceptar_consulta_cliente():    
    dni = dni_entry.get()
    cliente = obtener_cliente(dni)
    if cliente == None:
        dni_entry.delete(0, "end")
        dni_entry.focus()
    else:
        tabla_cliente = informacion_cliente(cliente)
        mostrar_resultado_operacion(tabla_cliente)
        ventana_auxiliar.destroy()

def cancelar():
    ventana_auxiliar.destroy()

#---------------------------------------------------------------------
#-------------------- FUNCIONES GESTIÓN DE OPCIONES ------------------- 
#---------------------------------------------------------------------

def alta():
    global ventana_auxiliar, dni_entry, nombre_cliente_entry, nombre_perro_entry, raza_entry
    
    ventana_auxiliar = Toplevel()
    ventana_auxiliar.title("Alta cliente")
    ventana_auxiliar.resizable(False, False)

    dni_label = Label(ventana_auxiliar, text="DNI:")
    dni_entry = Entry(ventana_auxiliar, bd=5, highlightcolor="red", highlightthickness=2)
    nombre_cliente_label = Label(ventana_auxiliar, text="Nombre cliente:")
    nombre_cliente_entry = Entry(ventana_auxiliar, bd=5, highlightcolor="red", highlightthickness=2)
    nombre_perro_label = Label(ventana_auxiliar, text="Nombre perro:")
    nombre_perro_entry = Entry(ventana_auxiliar, bd=5, highlightcolor="red", highlightthickness=2)
    raza_label = Label(ventana_auxiliar, text="Raza:")
    raza_entry = Entry(ventana_auxiliar, bd=5, highlightcolor="red", highlightthickness=2)
    boton_aceptar = Button(ventana_auxiliar, text="ACEPTAR", command=aceptar_alta)
    boton_cancelar = Button(ventana_auxiliar, text="CANCELAR", command=cancelar)

    dni_label.grid(row=1, column=1, sticky= "W", padx=10, pady=10)
    dni_entry.grid(row=1, column=2, padx=10)
    nombre_cliente_label.grid(row=2, column=1, sticky= "W", padx=10, pady=10)
    nombre_cliente_entry.grid(row=2, column=2, padx=10)
    nombre_perro_label.grid(row=3, column=1, sticky= "W", padx=10, pady=10)
    nombre_perro_entry.grid(row=3, column=2, padx=10)
    raza_label.grid(row=4, column=1, sticky= "W", padx=10, pady=10)
    raza_entry.grid(row=4, column=2, padx=10)
    boton_aceptar.grid(row=5, column=1, padx=10, pady=10, sticky= "W")
    boton_cancelar.grid(row=5, column=2, padx=10, pady=10, sticky= "E")

def baja():
    global ventana_auxiliar, dni_entry

    ventana_auxiliar = Toplevel()
    ventana_auxiliar.title("Baja cliente")
    ventana_auxiliar.resizable(False, False)

    dni_label = Label(ventana_auxiliar, text="DNI:")
    dni_entry = Entry(ventana_auxiliar, bd=5, highlightcolor="red", highlightthickness=2)
    boton_aceptar = Button(ventana_auxiliar, text="ACEPTAR", command=aceptar_baja)
    boton_cancelar = Button(ventana_auxiliar, text="CANCELAR", command=cancelar)

    dni_label.grid(row=1, column=1, sticky= "W", padx=10, pady=10)
    dni_entry.grid(row=1, column=2, padx=10)
    boton_aceptar.grid(row=2, column=1, padx=10, pady=10, sticky= "W")
    boton_cancelar.grid(row=2, column=2, padx=10, pady=10, sticky= "E")

def modificacion():
    global ventana_auxiliar, dni_entry, boton_aceptar, boton_cancelar

    ventana_auxiliar = Toplevel()
    ventana_auxiliar.title("Modificación cliente")
    ventana_auxiliar.resizable(False, False)

    dni_label = Label(ventana_auxiliar, text="DNI:")
    dni_entry = Entry(ventana_auxiliar, bd=5, highlightcolor="red", highlightthickness=2)
    boton_aceptar = Button(ventana_auxiliar, text="ACEPTAR", command=aceptar_dni_modificacion)
    boton_cancelar = Button(ventana_auxiliar, text="CANCELAR", command=cancelar)

    dni_label.grid(row=1, column=1, sticky= "W", padx=10, pady=10)
    dni_entry.grid(row=1, column=2, padx=10)
    boton_aceptar.grid(row=2, column=1, padx=10, pady=10, sticky= "W")
    boton_cancelar.grid(row=2, column=2, padx=10, pady=10, sticky= "E")

def consulta_cliente():
    global ventana_auxiliar, dni_entry

    ventana_auxiliar = Toplevel()
    ventana_auxiliar.title("Consulta cliente")
    ventana_auxiliar.resizable(False, False)

    dni_label = Label(ventana_auxiliar, text="DNI:")
    dni_entry = Entry(ventana_auxiliar, bd=5, highlightcolor="red", highlightthickness=2)
    boton_aceptar = Button(ventana_auxiliar, text="ACEPTAR", command=aceptar_consulta_cliente)
    boton_cancelar = Button(ventana_auxiliar, text="CANCELAR", command=cancelar)

    dni_label.grid(row=1, column=1, sticky= "W", padx=10, pady=10)
    dni_entry.grid(row=1, column=2, padx=10)
    boton_aceptar.grid(row=2, column=1, padx=10, pady=10, sticky= "W")
    boton_cancelar.grid(row=2, column=2, padx=10, pady=10, sticky= "E")

def consulta_clientes():
    tabla_clientes = informacion_clientes()
    mostrar_resultado_operacion(tabla_clientes)

def guardar_clientes():
    global datos_modificados
    
    guardar()
    mostrar_resultado_operacion("Clientes almacenados correctamente")
    datos_modificados = False

def salir():
    if datos_modificados:
        if messagebox.askyesno("Salir", "¿Desea guardar los cambios antes de salir?"):
            guardar()
    root.destroy()

def manual_usuario():
    messagebox.showinfo("Manual de usuario", "En construcción...")

def acerca_de():
    messagebox.showinfo("Acerca de...", "Versión 1.0")

#---------------------------------------------------------------------
#-------------------- FUNCIONES GESTIÓN DE EVENTOS ------------------- 
#---------------------------------------------------------------------

def eventos_menu(evento):
    tecla = evento.char
    if tecla == "a":alta()
    elif tecla == "b":baja()
    elif tecla == "m":modificacion()

#---------------------------------------------------------------------
#------------------------- VENTANA PRINCIPAL ------------------------- 
#---------------------------------------------------------------------

root = Tk()
root.title("Gestión de clientes")
root.minsize(400, 200)

barra_menus = Menu()
root.config(menu=barra_menus)
area_texto = Text(state="disabled", padx=10, pady=10, bd=5)
scrollbar = Scrollbar(command=area_texto.yview)
area_texto.config(yscrollcommand = scrollbar.set)

menu_archivo = Menu(tearoff=0)
menu_archivo.add_command(label="Guardar", command=guardar_clientes)
menu_archivo.add_separator()
img = PhotoImage(file="../imagenes/salir.gif")
menu_archivo.add_command(label="Salir", image=img, compound="left", command=salir)
barra_menus.add_cascade(label="Archivo", menu=menu_archivo)

menu_operaciones = Menu(tearoff=0)
menu_operaciones.add_command(label="Alta", accelerator="Alt-a", command=alta)
menu_operaciones.add_command(label="Baja", accelerator="Alt-b", command=baja)
menu_operaciones.add_command(label="Modificación", accelerator="Alt-m", command=modificacion)
menu_operaciones.add_separator()
menu_operaciones.add_command(label="Consulta cliente", command=consulta_cliente)
menu_operaciones.add_command(label="Consulta global", command=consulta_clientes)
barra_menus.add_cascade(label="Operaciones", menu=menu_operaciones)

menu_ayuda = Menu(tearoff=0)
menu_ayuda.add_command(label="Manual de usuario", command=manual_usuario)
menu_ayuda.add_command(label="Acerca de...", command=acerca_de)
barra_menus.add_cascade(label="Ayuda", menu=menu_ayuda)

area_texto.pack(expand=True, fill="both", side = "left")
scrollbar.pack(side = "right", fill = "y")

root.bind("<Alt-KeyPress>", eventos_menu)

root.protocol("WM_DELETE_WINDOW", salir)

root.mainloop()

