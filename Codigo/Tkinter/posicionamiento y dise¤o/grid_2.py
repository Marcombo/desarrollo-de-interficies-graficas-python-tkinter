from tkinter import Tk, Label

filas = 3
columnas = 4

root = Tk()

for fila in range(filas):
   root.rowconfigure(fila, weight=1)
   for columna in range(columnas):
      etiqueta = Label(text="Etiqueta"+str(fila)+str(columna), bg="yellow")
      etiqueta.grid(row=fila,column=columna, padx=2, pady=2, sticky="nsew")
      #etiqueta.grid(row=fila,column=columna, padx=2, pady=2)
      root.columnconfigure(columna, weight=1)
