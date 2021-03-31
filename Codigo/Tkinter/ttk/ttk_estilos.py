from tkinter import Tk, ttk

root = Tk()
root.minsize(200, 100)

estilo = ttk.Style()
estilo.configure("miEstilo.TLabel", foreground="white", background="blue", font=("Arial", 20, "bold italic"), anchor="center")

etiqueta = ttk.Label(text="Botón ttk", style="miEstilo.TLabel")
etiqueta.pack(expand= True, padx= 20, pady=20, ipadx=10, ipady=10)

##MODIFICACIÓN DE LAS OPCIONES DE UN ESTILO PREDETERMINADO
##from tkinter import Tk, ttk
##
##root = Tk()
##root.minsize(200, 100)
##
##estilo = ttk.Style()
##estilo.configure("TLabel", foreground="white", background="red", font=("Arial", 20, "bold"), anchor="center")
##
##etiqueta = ttk.Label(text="Botón ttk")
##etiqueta.pack(expand= True, padx= 20, pady=20, ipadx=10, ipady=10)
