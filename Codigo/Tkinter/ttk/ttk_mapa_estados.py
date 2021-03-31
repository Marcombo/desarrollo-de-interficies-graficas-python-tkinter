from tkinter import Tk, ttk

root = Tk()

estilo = ttk.Style()
estilo.configure('miEstilo.TButton', font=('Arial', 24))
estilo.map('miEstilo.TButton', foreground=[('pressed', 'blue'),('active', 'orange')], font=[('active', ('Arial', 28, 'bold'))])

boton = ttk.Button(style='miEstilo.TButton', text="Botón")
boton.pack(padx=10, pady=10, ipadx=5, ipady=5)
