from tkinter import Tk, Menu, Text, PhotoImage, filedialog, IntVar

fichero=""
extensiones = [("ficheros texto", "*.txt")]

##########################################################
#Funciones que se ejecutan seleccionar una opción del menú
##########################################################

def nuevo():
    global fichero
    
    area_texto.delete(1.0, "end")
    fichero = ""

def abrir():
    global fichero
    
    fichero = filedialog.askopenfilename(initialdir = ".", title = "Abrir archivo", \
                                         filetypes = extensiones)
    if fichero:
        f = open(fichero, "r", encoding='utf-8')
        area_texto.delete(1.0, "end")
        area_texto.insert("insert", f.read())
        f.close()

def guardar():
    global fichero
    if not(fichero): fichero = filedialog.asksaveasfilename(initialdir = ".", title = "Guardar", \
                                                            filetypes = extensiones, \
                                                            defaultextension=".txt")
    if fichero:
        texto = area_texto.get(1.0, "end")
        f = open(fichero, "w", encoding='utf-8')
        f.write(texto)
        f.close

def guardar_como():
    global fichero
    
    fichero = filedialog.asksaveasfilename(initialdir = ".", title = "Guardar como", filetypes = extensiones, defaultextension=[".txt", ".html"])
    if fichero:
        texto = area_texto.get(1.0, "end")
        f = open(fichero, "w", encoding='utf-8')
        f.write(texto)
        f.close

def gestion_extensiones():
    global extensiones

    extensiones = [("ficheros texto", "*.txt")]
    if extension_xml.get():
        extensiones.append(("ficheros xml", "*.xml"))
    if extension_html.get():
        extensiones.append(("ficheros html", "*.html"))

def salir():
    root.destroy()

#Ventana principal
root = Tk()
root.title("Editor de texto")

#Variables de control
extension_xml = IntVar()
extension_html = IntVar()

#Creación de widgets de la ventana principal
barra_menus = Menu()
area_texto = Text(padx=10, pady=10, bd=5)

#Menú Archivo
menu_archivo = Menu(tearoff=0)
menu_archivo.add_command(label="Nuevo", command=nuevo)

submenu_abrir = Menu(tearoff=0)
submenu_abrir.add_command(label="Explorar", command=abrir)
submenu_abrir.add_command(label="Recientes")
menu_archivo.add_cascade(label='Abrir', menu=submenu_abrir)

menu_archivo.add_command(label="Guardar", command=guardar)
menu_archivo.add_command(label="Guardar como", command=guardar_como)
menu_archivo.add_separator()

submenu_extensiones = Menu(tearoff=False)
submenu_extensiones.add_checkbutton(label="xml", variable=extension_xml, command=gestion_extensiones)
submenu_extensiones.add_checkbutton(label="html", variable=extension_html, command=gestion_extensiones)
menu_archivo.add_cascade(label='Extensiones', menu=submenu_extensiones)

menu_archivo.add_separator()
img = PhotoImage(file="./imagenes/salir.gif")
menu_archivo.add_command(label="Salir", image=img, compound="left", command=salir)
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
menu_ayuda.add_command(label="Acerca de...")
barra_menus.add_cascade(label="Ayuda", menu=menu_ayuda)

#Composición de los widgets de la ventana principal
root.config(menu=barra_menus)
area_texto.pack(expand= True, fill="both")

root.mainloop()

