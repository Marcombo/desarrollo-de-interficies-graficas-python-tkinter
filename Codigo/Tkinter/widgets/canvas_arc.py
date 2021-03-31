from tkinter import Tk, Canvas

ancho = 300
alto = 200

radio_ojo = 10
radio_cara = 100
angulo_inicial_max = angulo_inicial = 30
apertura = 300
incremento = 5

periodo = 50

def mueve_boca():
    global incremento, angulo_inicial, apertura

    angulo_inicial -= incremento
    apertura += 2*incremento
    if angulo_inicial <= incremento or angulo_inicial >= angulo_inicial_max:
        incremento = -incremento
        
    canvas.itemconfig(cara, extent=apertura, start=angulo_inicial)
    canvas.after(periodo, mueve_boca)
    
root = Tk()
root.resizable(False, False)

canvas = Canvas(width=ancho, height=alto)
cara = canvas.create_arc(ancho/2-radio_cara, alto/2-radio_cara, ancho/2+radio_cara, alto/2+radio_cara, start=angulo_inicial, extent=apertura, fill="blue", outline="")
ojo = canvas.create_oval(ancho/2-radio_ojo, alto/4-radio_ojo, ancho/2+radio_ojo, alto/4+radio_ojo, fill="yellow", outline="")

canvas.pack()

mueve_boca()

root.mainloop()
