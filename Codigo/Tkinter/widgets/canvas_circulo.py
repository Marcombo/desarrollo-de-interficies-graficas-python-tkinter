from tkinter import Tk, Canvas
from random import randint

radio = 10
ancho = 400
alto = 200
desplazamiento_x = 1
desplazamiento_y = 1
intervalo = 2

centro_x = randint(radio, ancho)
centro_y = randint(radio, alto)

def mueve_pelota():
    global desplazamiento_x, desplazamiento_y
    
    x0, y0, x1, y1 = canvas.coords(pelota)
    if x0 < 0 or x1 > ancho: desplazamiento_x = -desplazamiento_x
    if y0 < 0 or y1 > alto: desplazamiento_y = -desplazamiento_y
    canvas.move(pelota, desplazamiento_x, desplazamiento_y)
    root.after(intervalo, mueve_pelota)


root = Tk()
root.resizable(False,False)
canvas = Canvas(width = ancho, height = alto)
canvas.pack()

pelota = canvas.create_oval(centro_x-radio, centro_y-radio, centro_x+radio, centro_y+radio, fill="blue", outline="blue")
mueve_pelota()

root.mainloop()

    
    
