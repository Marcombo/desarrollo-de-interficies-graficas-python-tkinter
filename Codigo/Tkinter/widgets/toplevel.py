from tkinter import Tk, Label, Button, Entry, Toplevel

def aceptar():
    usuario = usuario_entry.get()
    if usuario:
        etiqueta.configure(text="Usuario: " + usuario)
    else:
        etiqueta.configure(text="Usuario no introducido")
    ventana_acceso.destroy()
    
def cancelar():
    usuario_entry.delete(0, "end")
    contraseña_entry.delete(0, "end")

def acceder():
    global ventana_acceso, usuario_entry, contraseña_entry
    
    ventana_acceso = Toplevel()
    ventana_acceso.title("Login")
    ventana_acceso.resizable(False, False)

    usuario_label = Label(ventana_acceso, text="USUARIO:")
    usuario_entry = Entry(ventana_acceso, bd=5, highlightcolor="red", highlightthickness=2)
    contraseña_label = Label(ventana_acceso, text="CONTRASEÑA:")
    contraseña_entry = Entry(ventana_acceso, bd=5, show='*', highlightcolor="red", highlightthickness=2)
    boton_aceptar = Button(ventana_acceso, text="ACEPTAR", command=aceptar)
    boton_cancelar = Button(ventana_acceso, text="CANCELAR", command=cancelar)

    usuario_label.grid(row=0, column=0, sticky= "W", padx=10, pady=10)
    usuario_entry.grid(row=0, column=1, padx=10)
    contraseña_label.grid(row=1, column=0, sticky= "W", padx=10, pady=10)
    contraseña_entry.grid(row=1, column=1, padx=10)
    boton_aceptar.grid(row=2, column=0, padx=10, pady=10, sticky= "W")
    boton_cancelar.grid(row=2, column=1, padx=10, pady=10, sticky= "E")

root = Tk()
root.title("Ventana de acceso")
root.geometry("300x150")
root.minsize(300, 150)
boton = Button(text="ACCEDER",command=acceder)
etiqueta = Label(text="Usuario no introducido")
boton.place(relx=0.5, rely=0.5, anchor="center")
etiqueta.pack(side="bottom", pady=5)

root.mainloop()
