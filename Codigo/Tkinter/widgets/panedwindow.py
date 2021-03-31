from tkinter import Tk, Label, Text, LabelFrame, PanedWindow, RAISED, BOTH, VERTICAL, NE

root = Tk()
root.title("Paneles")
root.minsize(800, 400)

cabecera = Label(text="Editores de texto", pady=10, fg="blue", font=("Arial", "24", "bold"))
cabecera.pack()

root_panel = PanedWindow(sashrelief = RAISED)
root_panel.pack(fill=BOTH, expand=True)

frame_izquierdo = LabelFrame(root_panel, text=" Editor izquierdo ", font=("Arial", "12"))
text_izquierdo = Text(frame_izquierdo, padx=10, pady=10, bd=5, width=50)
text_izquierdo.pack(fill=BOTH, expand=True)
root_panel.add(frame_izquierdo)

subpanel_derecho = PanedWindow(root_panel, orient=VERTICAL, showhandle= True)
root_panel.add(subpanel_derecho)

frame_superior = LabelFrame(root_panel, text=" Editor derecho superior ", font=("Arial", "12"), labelanchor=NE)
text_superior = Text(frame_superior, padx=10, pady=10, bd=5, width=50, height=10)
text_superior.pack(fill=BOTH, expand=True)
subpanel_derecho.add(frame_superior)

frame_inferior = LabelFrame(root_panel, text=" Editor derecho inferior ", font=("Arial", "12"), labelanchor=NE)
text_inferior = area_texto = Text(frame_inferior, padx=10, pady=10, bd=5, width=50, height=10)
text_inferior.pack(fill=BOTH, expand=True)
subpanel_derecho.add(frame_inferior)

root.mainloop()
