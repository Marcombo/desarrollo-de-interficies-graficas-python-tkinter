from tkinter import Tk, Menu, Text, filedialog, Scrollbar, messagebox

fichero=""

##########################################################
#Funciones que se ejecutan seleccionar una opción del menú
##########################################################

def nuevo():
    global fichero
    
    area_texto.delete(1.0, "end")
    fichero = ""

def abrir():
    global fichero
    
    fichero = filedialog.askopenfilename(initialdir = ".", title = "Abrir archivo", filetypes = [("ficheros texto", "*.txt")])
    if fichero:
        f = open(fichero, "r", encoding='utf-8')
        area_texto.delete(1.0, "end")
        area_texto.insert("insert", f.read())
        f.close()

def guardar():
    global fichero
    if not(fichero): fichero = filedialog.asksaveasfilename(initialdir = ".", title = "Guardar", filetypes = [("ficheros texto", "*.txt")], defaultextension=".txt")
    if fichero:
        texto = area_texto.get(1.0, "end")
        f = open(fichero, "w", encoding='utf-8')
        f.write(texto)
        f.close

def guardar_como():
    global fichero
    
    fichero = filedialog.asksaveasfilename(initialdir = ".", title = "Guardar como", filetypes = [("ficheros texto", "*.txt")], defaultextension=".txt")
    if fichero:
        texto = area_texto.get(1.0, "end")
        f = open(fichero, "w", encoding='utf-8')
        f.write(texto)
        f.close

def salir():
    root.destroy()

def cerrar_ventana():
    if messagebox.askokcancel("Salir", "¿Desea realmente salir?"):
        root.destroy()

def eventos_menu(evento):
    opcion = evento.char
    if opcion == "a":abrir()
    elif opcion == "g":guardar()
    elif opcion == "s":salir()

#Ventana principal
root = Tk()
root.title("Editor de texto")

#Creación de widgets de la ventana principal
barra_menus = Menu()
area_texto = Text(padx=10, pady=10, bd=5)
scrollbar = Scrollbar(command=area_texto.yview)
area_texto.config(yscrollcommand = scrollbar.set)

#Menú Archivo
menu_archivo = Menu(tearoff=0)
menu_archivo.add_command(label="Nuevo", command=nuevo)

submenu_abrir = Menu(tearoff=0)
submenu_abrir.add_command(label="Archivo", command=abrir, accelerator="Alt-a")
submenu_abrir.add_command(label="Recientes")
menu_archivo.add_cascade(label='Abrir', menu=submenu_abrir)

menu_archivo.add_command(label="Guardar", command=guardar, accelerator="Alt-g")
menu_archivo.add_command(label="Guardar como", command=guardar_como)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir, accelerator="Alt-s")
barra_menus.add_cascade(label="Archivo", menu=menu_archivo)

#Menú edición
menu_edicion = Menu(tearoff=0)
menu_edicion.add_command(label="Deshacer")
menu_edicion.add_command(label="Rehacer")
menu_edicion.add_separator()
menu_edicion.add_command(label="Copiar")
menu_edicion.add_command(label="Pegar")
menu_edicion.add_command(label="Borrar")
menu_edicion.add_command(label="Seleccionar todo")
barra_menus.add_cascade(label="Edición", menu=menu_edicion)

#Menú ayuda
menu_ayuda = Menu(tearoff=0)
menu_ayuda.add_command(label="Manual de usuario")
menu_ayuda.add_command(label="About...")
barra_menus.add_cascade(label="Ayuda", menu=menu_ayuda)

#Composición de los widgets de la ventana principal
root.config(menu=barra_menus)
area_texto.pack(expand=True, fill="both", side = "left")
scrollbar.pack(side = "right", fill = "y")

root.bind("<Alt-KeyPress>", eventos_menu)

root.protocol("WM_DELETE_WINDOW", cerrar_ventana)

root.mainloop()

