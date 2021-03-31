from tkinter import Tk, Text, Button, Frame
   
root = Tk()
root.title("Frames")
root.minsize(400, 200)

frame_izquierdo = Frame(root)
frame_derecho = Frame(root)
frame_inferior = Frame(root)

frame_izquierdo.grid(row=0, column=0, sticky="nsew")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame_derecho.grid(row=0, column=1, sticky="n", padx=5)
frame_inferior.grid(row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

area_texto = Text(frame_izquierdo, padx=10, pady=10, bd=5)
area_texto.pack(expand= True, fill="both")

boton_nuevo = Button(frame_derecho, text="  NUEVO  ")
boton_abrir = Button(frame_derecho, text="    ABRIR   ")
boton_guardar = Button(frame_derecho, text="GUARDAR")
boton_nuevo.pack(pady=5)
boton_abrir.pack()
boton_guardar.pack(pady=5)

boton_ayuda = Button(frame_inferior, text="   AYUDA  ")
boton_salir = Button(frame_inferior, text="  SALIR  ", width=8)
boton_ayuda.pack(side="left")
boton_salir.pack(side="right")

root.mainloop()
