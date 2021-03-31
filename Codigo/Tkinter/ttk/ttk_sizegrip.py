from tkinter import Tk, Text, Button, PhotoImage, filedialog, messagebox, ttk
from pathlib import Path

###################################################
#Funciones que se ejecutan al pulsar los botones
###################################################
def anadir_pestana():
    marco_editor = ttk.Frame()
    area_texto = Text(marco_editor)
    scrollbar = ttk.Scrollbar(marco_editor, command=area_texto.yview)
    area_texto.config(yscrollcommand = scrollbar.set)
    area_texto.pack(expand= True, fill="both", side = "left")
    scrollbar.pack(side = "right", fill = "y")
    editor.add(marco_editor, text="(vacío)")
    if len(editor.tabs()) > 1: editor.select(editor.index('current')+1)

def borrar_pestana():
    if len(editor.tabs()) > 0:
        posicion_etiqueta = editor.index('current')
        editor.forget(posicion_etiqueta)

def guardar():
    posicion_etiqueta = editor.index('current')
    etiqueta = editor.tab(posicion_etiqueta, option='text')
    id_marco_editor = editor.select()
    marco_editor = editor.nametowidget(id_marco_editor)
    lista_widgets = marco_editor.winfo_children()
    area_texto = lista_widgets[0]

    if etiqueta == "(vacío)":
        fichero = filedialog.asksaveasfilename(initialdir = ".", title = "Guardar", filetypes = [("ficheros texto", "*.txt")], defaultextension=".txt")
        etiqueta = Path(fichero).stem
        editor.tab(posicion_etiqueta, text=etiqueta)
    else:
        fichero = etiqueta + ".txt"

    texto = area_texto.get(1.0, "end")
    f = open(fichero, "w", encoding='utf-8')
    f.write(texto)
    f.close
    messagebox.showinfo("Guardar", fichero+" guardado correctamente.")

def abrir():
    fichero = filedialog.askopenfilename(initialdir = ".", title = "Abrir archivo", filetypes = [("ficheros texto", "*.txt")])
    etiqueta = Path(fichero).stem
    if fichero:
        marco_editor = ttk.Frame()
        area_texto = Text(marco_editor)
        scrollbar = ttk.Scrollbar(marco_editor, command=area_texto.yview)
        area_texto.config(yscrollcommand = scrollbar.set)
        area_texto.pack(expand= True, fill="both", side = "left")
        scrollbar.pack(side = "right", fill = "y")
        editor.add(marco_editor, text=etiqueta)
        if len(editor.tabs()) > 1: editor.select(editor.index('current')+1)

        f = open(fichero, "r", encoding='utf-8')
        area_texto.insert(1.0, f.read())
        f.close()
    
###################################################
#Ventana principal
###################################################
root = Tk()
root.title("Editor de texto")
root.minsize(600, 300)

###################################################
#Barra de herramientas
###################################################
barra_herramientas = ttk.Frame()
img_anadir_pestana = PhotoImage(file="./imagenes/anadir_pestana.gif")
img_borrar_pestana = PhotoImage(file="./imagenes/borrar_pestana.gif")
img_abrir_archivo = PhotoImage(file="./imagenes/abrir_archivo.gif")
img_guardar_archivo = PhotoImage(file="./imagenes/guardar_archivo.gif")
boton_anadir_pestana = Button(barra_herramientas,image=img_anadir_pestana, background="white", command=anadir_pestana)
boton_borrar_pestana = Button(barra_herramientas,image=img_borrar_pestana, background="white", command=borrar_pestana)
boton_abrir_archivo = Button(barra_herramientas,image=img_abrir_archivo, background="white", command=abrir)
boton_guardar_archivo = Button(barra_herramientas,image=img_guardar_archivo, background="white", command=guardar)
boton_anadir_pestana.pack(side="left", padx=5, pady=5)
boton_borrar_pestana.pack(side="left")
boton_guardar_archivo.pack(side="right", padx=5, pady=5)
boton_abrir_archivo.pack(side="right")
barra_herramientas.pack(fill="x")

###################################################
#Notebook
###################################################
editor = ttk.Notebook()
editor.pack(expand= True, fill="both")

###################################################
#Sizegrip
###################################################
sg = ttk.Sizegrip()
sg.pack(side="right")

root.mainloop()
