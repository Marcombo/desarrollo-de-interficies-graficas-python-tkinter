from tkinter import Tk, Canvas

periodo = 200
var_aux = False

def mueve_dash():
    global var_aux
    
    if var_aux: patron=(6, 4, 2, 4)
    else:patron=(6, 4, 2, 4, 2, 4)
    canvas.itemconfigure(rectangulo, dash=patron)
    var_aux = not(var_aux)
    root.after(periodo, mueve_dash)
    
root = Tk()
root.geometry("400x200")
root.resizable(False, False)

canvas = Canvas()
rectangulo = canvas.create_rectangle(50, 50, 350, 150, fill="yellow", outline="blue", width=5)
canvas.pack()

mueve_dash()

root.mainloop()

