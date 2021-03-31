from tkinter import Tk, Label, StringVar

texto = "¡Hola Mundo!"
intervalo = 200

texto_auxiliar = texto + " " * len(texto)

def avanza():
    global texto_auxiliar

    ultimo_caracter = texto_auxiliar[len(texto_auxiliar) - 1]
    texto_auxiliar = texto_auxiliar[:-1]
    texto_auxiliar = ultimo_caracter + texto_auxiliar
    variable_control.set(texto_auxiliar[0:len(texto)])
    root.after(intervalo, avanza)

root = Tk()
root.title("Letrero deslizante")

variable_control = StringVar()

etiqueta = Label(textvariable=variable_control, width= len(texto), padx=10, pady=10, fg="blue", font=("Arial", "48", "bold"))
etiqueta.pack()

avanza()

root.mainloop()



