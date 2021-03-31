from tkinter import Tk, Canvas

root = Tk()
root.resizable(False,False)
canvas = Canvas(width = 400, height = 200)
texto=canvas.create_text(200, 100, anchor="center", text="Acerca el ratón al texto", font=("Arial", "20", "bold"), fill="blue", activefill="red")

canvas.pack()

root.mainloop()
