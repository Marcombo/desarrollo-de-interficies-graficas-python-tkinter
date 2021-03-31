from tkinter import Tk, Canvas
    
root = Tk()
root.resizable(False, False)

canvas = Canvas(width=400, height=200)
rectangulo = canvas.create_polygon(100, 50, 300, 150, 300, 50, 100, 150, fill="yellow", outline="orange", width=5)
canvas.pack()

