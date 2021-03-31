import time, threading

segundos = 0

def interrumpir():
    while True:
        time.sleep(2)
        print("INTERRUMPO")
        
hilo = threading.Thread(target=interrumpir)
hilo.start()

while True:
    print(segundos)
    segundos += 1
    time.sleep(1)


    
