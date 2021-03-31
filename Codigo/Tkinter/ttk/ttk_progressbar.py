from tkinter import Tk, ttk
import time, threading

def proceso():
    boton.configure(state='disabled')
    barra_progreso.grid(row=1)
    for i in range (0, 100, 10):
        time.sleep(0.5)
        barra_progreso.step(10)
    barra_progreso.grid_forget()
    boton.configure(state='enabled')

def arrancar_proceso():
    hilo = threading.Thread(target=proceso)
    hilo.start()

root = Tk()
root.geometry("200x100")
root.resizable(False, False)
root.columnconfigure(0,weight=1)

boton = ttk.Button(text="PULSAR", command=arrancar_proceso)
boton.grid(row=0, pady=20)

barra_progreso = ttk.Progressbar()

root.mainloop()
