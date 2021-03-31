from tkinter import Tk, Canvas, Menu, colorchooser

ancho_canvas = 600
alto_canvas = 300

objeto_pulsado = False
dimension_objeto = 50
posicion_x_previa = posicion_y_previa = 0

#---------------------------------------------------------------------
#------------------------- MENÚS CONTEXTUALES ------------------------ 
#---------------------------------------------------------------------

def mostrar_popup_canvas(evento):
    global objeto_pulsado

    x = evento.x
    y = evento.y
    if not(objeto_pulsado) and x-dimension_objeto > 0 and x+dimension_objeto < ancho_canvas and y-dimension_objeto > 0 and y+dimension_objeto < alto_canvas:
        menu_canvas = Menu(tearoff=0)
        menu_canvas.add_command(label="Cuadrado", command=lambda:crear_cuadrado(x, y))
        menu_canvas.add_command(label="Círculo", command=lambda:crear_circulo(x, y))
        menu_canvas.add_command(label="Triángulo", command=lambda:crear_triangulo(x, y))
        menu_canvas.post(evento.x_root, evento.y_root)

    objeto_pulsado = False

def mostrar_popup_objeto(evento):
    global objeto_pulsado
    objeto_pulsado = True

    id = canvas.find_withtag('current')[0]
    
    menu_objeto = Menu(tearoff=0)
    menu_objeto.add_command(label="Color", command=lambda:pintar(id))
    menu_objeto.add_command(label="Traer al frente", command=lambda:enviar_al_frente(id))
    menu_objeto.add_command(label="Enviar al fondo", command=lambda:enviar_al_fondo(id))
    menu_objeto.add_command(label="Borrar", command=lambda:borrar(id))
    menu_objeto.post(evento.x_root, evento.y_root)

#---------------------------------------------------------------------
#------------------------- OPCIONES DE MENÚS ------------------------- 
#---------------------------------------------------------------------

def crear_cuadrado(x, y):
    id = canvas.create_rectangle(x-dimension_objeto, y-dimension_objeto, x+dimension_objeto, y+dimension_objeto, fill="white")
    canvas.tag_bind(id, "<Button-3>", mostrar_popup_objeto)

def crear_circulo(x, y):
    id = canvas.create_oval(x-dimension_objeto, y-dimension_objeto, x+dimension_objeto, y+dimension_objeto, fill="white")
    canvas.tag_bind(id, "<Button-3>", mostrar_popup_objeto)

def crear_triangulo(x, y):
    puntos = [x, y-dimension_objeto, x+dimension_objeto, y+dimension_objeto, x-dimension_objeto, y+dimension_objeto]
    id = canvas.create_polygon(puntos, fill="white", outline="black")
    canvas.tag_bind(id, "<Button-3>", mostrar_popup_objeto)

def pintar(id):
    color = colorchooser.askcolor(title ="Elige un color")
    if color:
        canvas.itemconfigure(id, fill=color[1], outline=color[1])

def enviar_al_frente(id):
    canvas.tag_raise(id)

def enviar_al_fondo(id):
    canvas.tag_lower(id)

def borrar(id):
    canvas.delete(id)

#---------------------------------------------------------------------
#------------------ MOVIMIENTO DE OBJETOS GRÁFICOS ------------------- 
#---------------------------------------------------------------------

def iniciar_movimiento(evento):
    global posicion_x_previa, posicion_y_previa
    
    posicion_x_previa = evento.x
    posicion_y_previa = evento.y
    
def mover_objeto(evento):
    global posicion_x_previa, posicion_y_previa
    
    lista_id = canvas.find_withtag('current')
    if lista_id != ():
        incremento_x = evento.x - posicion_x_previa
        incremento_y = evento.y - posicion_y_previa
        id= lista_id[0]
        esquinas = canvas.bbox(id) #(x1, y1, x2, y2)
        if esquinas[0]+incremento_x > 0 and esquinas[2]+incremento_x < ancho_canvas and esquinas[1]+incremento_y > 0 and esquinas[3]+incremento_y < alto_canvas:
            canvas.move(id, incremento_x, incremento_y)
        posicion_x_previa = evento.x
        posicion_y_previa = evento.y
#---------------------------------------------------------------------
#------------------------- VENTANA PRINCIPAL ------------------------- 
#---------------------------------------------------------------------

root = Tk()
root.resizable(False, False)
root.title("Editor gráfico")
canvas = Canvas(width = ancho_canvas, height = alto_canvas)
canvas.pack()

canvas.bind("<Button-3>", mostrar_popup_canvas)
canvas.bind("<Button-1>", iniciar_movimiento)
canvas.bind("<B1-Motion>", mover_objeto)

root.mainloop()
