from tkinter import Tk, Label

def mostrar_posicion():
    (x, y) = root.winfo_pointerxy()
    root_x = root.winfo_rootx()
    root_y = root.winfo_rooty()
    ancho_pantalla = root.winfo_width()
    alto_pantalla = root.winfo_height()
    mouse_x = x - root_x
    mouse_y = y - root_y
    if mouse_x < 0 or mouse_x > ancho_pantalla or mouse_y < 0 or mouse_y > alto_pantalla:
        mouse_x = -1
        mouse_y = -1 
    
    etiqueta.configure(text=str(mouse_x) + ", " + str(mouse_y))
    root.after(10, mostrar_posicion)

root = Tk()
root.geometry("400x200")

etiqueta = Label(text="-1, -1", font=("Arial", 20, "bold"))

etiqueta.pack(expand=True)

mostrar_posicion()
