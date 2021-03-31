from tkinter import Tk, Label, Button, Entry

def aceptar():
    root.destroy()

def cancelar():
    usuario_entry.delete(0, "end")
    contraseña_entry.delete(0, "end")

root = Tk()
root.title("Login")
root.resizable(False, False)

usuario_label = Label(text="USUARIO:")
usuario_entry = Entry(bd=5, highlightcolor="red", highlightthickness=2)
contraseña_label = Label(text="CONTRASEÑA:")
contraseña_entry = Entry(bd=5, show='*', highlightcolor="red", highlightthickness=2)
boton_aceptar = Button(text="ACEPTAR", command=aceptar)
boton_cancelar = Button(text="CANCELAR", command=cancelar)

usuario_label.grid(row=0, column=0, sticky= "W", padx=10, pady=10)
usuario_entry.grid(row=0, column=1, sticky= "E", padx=10)
contraseña_label.grid(row=1, column=0, sticky= "W", padx=10, pady=10)
contraseña_entry.grid(row=1, column=1, sticky= "E", padx=10)
boton_aceptar.grid(row=2, column=0, padx=10, pady=10, sticky= "W")
boton_cancelar.grid(row=2, column=1, padx=10, pady=10, sticky= "E")

root.mainloop()
