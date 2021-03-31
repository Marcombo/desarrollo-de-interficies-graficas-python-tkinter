from tkinter import Tk, Label

incremento = 2
periodo = 50
tamanio_max = 40
tamanio = tamanio_min = 10

def modifica_tamanio():
    global tamanio, incremento
    

    if tamanio > tamanio_max or tamanio < tamanio_min:
        incremento = -incremento
    tamanio += incremento

    etiqueta.configure( font=("Arial", str(tamanio), "bold"))
    
    etiqueta.after(periodo, modifica_tamanio)

root = Tk()
root.geometry("400x200")

etiqueta = Label(text="¡Qué mareo!", font=("Arial", str(tamanio), "bold"))

etiqueta.pack(expand=True)

modifica_tamanio()
