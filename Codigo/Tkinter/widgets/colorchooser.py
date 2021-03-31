from tkinter import Tk, Button, colorchooser
  
def elegir_color(): 
    color = colorchooser.askcolor(title ="Elige un color")  
    boton.configure(bg=color[1])
  
root = Tk()
root.minsize(False, False)

boton = Button(text = "Selecciona un color", font=("Arial", "24", "bold"), fg="blue", bd=5, command = elegir_color)
boton.pack(padx=50, pady=50) 


