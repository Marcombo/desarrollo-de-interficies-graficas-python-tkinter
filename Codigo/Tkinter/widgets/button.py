from tkinter import Tk, Label, Button, StringVar

hora=minuto=segundo=0
inicio=False

def actualizar_tiempo():
    global hora, minuto, segundo

    if inicio:  
        segundo += 1
        if segundo == 60:
            segundo = 0
            minuto += 1
        if minuto == 60:
            segundo = 0
            minuto = 0
            hora += 1
        if hora == 99:
            segundo = 0
            minuto = 0
            hora = 0
        if hora < 10: hora_str = "0"+str(hora)
        else: hora_str = str(hora)
        if minuto < 10: minuto_str = "0"+str(minuto)
        else: minuto_str = str(minuto)
        if segundo < 10: segundo_str = "0"+str(segundo)
        else: segundo_str = str(segundo)
        variable_control.set(hora_str+":"+minuto_str+":"+segundo_str)
        root.after(1000, actualizar_tiempo)

def start():
    global hora, minuto, segundo, inicio

    if not(inicio):
        variable_control.set("00:00:00")
        hora=minuto=segundo=0
        inicio=True
        root.after(1000, actualizar_tiempo)

def stop():
    global inicio
    inicio=False

root = Tk()
root.resizable(False, False)

variable_control = StringVar(value="00:00:00")

reloj = Label(textvariable= variable_control, fg="blue", font=("Arial", 18), padx=20, pady=20)
boton_start = Button(text="Start", padx=10,  fg="white", bg="green", command=start)
boton_stop = Button(text="Stop", padx=10, fg="white", bg="red", command=stop)

reloj.pack()
boton_start.pack(side="left", padx=10, pady=10)
boton_stop.pack(side="right", padx=10, pady=10)

root.mainloop()
