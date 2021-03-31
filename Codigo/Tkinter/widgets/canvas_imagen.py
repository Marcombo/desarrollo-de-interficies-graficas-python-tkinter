from tkinter import Tk, Canvas, PhotoImage
from random import randint

radio = 20
ancho = 400
alto = 200
desplazamiento_x = 1
desplazamiento_y = 1
intervalo = 2

centro_x = randint(radio, ancho)
centro_y = randint(radio, alto)

def mueve_pelota():
    global desplazamiento_x, desplazamiento_y
    
    x, y = canvas.coords(pelota)
    if x-radio < 0 or x+radio > ancho: desplazamiento_x = -desplazamiento_x
    if y-radio < 0 or y+radio > alto: desplazamiento_y = -desplazamiento_y
    canvas.move(pelota, desplazamiento_x, desplazamiento_y)
    root.after(intervalo, mueve_pelota)

root = Tk()
root.resizable(False,False)
canvas = Canvas(width = ancho, height = alto, bg="white")
canvas.pack()

img = PhotoImage(file="../imagenes/pelota.gif")
pelota = canvas.create_image(centro_x, centro_y, image=img, anchor="center")

mueve_pelota()

root.mainloop()
