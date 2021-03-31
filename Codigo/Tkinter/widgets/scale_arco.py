from tkinter import Tk, Canvas, Scale

ancho = 400
alto = 200
radio = 75

def modifica_arco(angulo):
    canvas.itemconfig(arco, extent=angulo)
    
root = Tk()
root.title("Arco")
root.resizable(False, False)

canvas = Canvas(width=ancho, height=alto)
arco = canvas.create_arc(ancho/2-radio, alto/2-radio, ancho/2+radio, alto/2+radio, start=0, extent=0, fill="blue", outline="")
barra_deslizamiento = Scale(label='ÁNGULO', from_=0, to=360, orient="horizontal", length=ancho, command=modifica_arco, tickinterval=90)

canvas.pack()
barra_deslizamiento.pack()

root.mainloop()
