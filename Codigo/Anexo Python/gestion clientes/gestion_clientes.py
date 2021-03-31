import clases
import os
import pickle
from tabulate import tabulate

fichero_clientes = "clientes.pkl"
datos_modificados = False
lista_clientes = []
if os.path.exists(fichero_clientes):
    with open(fichero_clientes, 'rb') as f:
        lista_clientes = pickle.load(f)


def mostrar_opciones():
    print("\n")
    print("1- Alta")
    print("2- Baja")
    print("3- Modificación")
    print("4- Consultar cliente")
    print("5- Consulta global")
    print("6- Salvar")
    print("7- Salir")
    opcion = input("Elija una opción: ")
    print("\n")
    return opcion

def datos_cliente(dni):
    for cliente in lista_clientes:
        if cliente.dni == dni: return cliente
    return None

def alta():
    global datos_modificados
    print("Por favor, introduzca el valor de los siguientes campos")
    dni = input("DNI: ")
    if datos_cliente(dni) == None:
        nombre_cliente = input("Nombre del cliente: ")
        nombre_perro = input("Nombre del perro: ")
        raza = input("Raza: ")

        perro = clases.Perro(nombre_perro, raza)
        cliente = clases.Cliente(nombre_cliente, dni, perro)
        
        lista_clientes.append(cliente)
        print("---Cliente dado de alta---")
        datos_modificados = True
    else: print("---Ya existe un cliente con el DNI " + dni + "---")

def modificacion():
    global datos_modificados
    dni = input("DNI del cliente a modificar: ")
    cliente = datos_cliente(dni)
    if cliente == None: print("---El cliente con DNI " + dni + " no existe---")
    else:
        print("Por favor, rellene los siguientes campos")
        nombre_cliente = input("Nombre del cliente: ")
        if nombre_cliente != "": cliente.nombre = nombre_cliente
        nombre_perro = input("Nombre del perro: ")
        if nombre_perro != "":cliente.perro.nombre = nombre_perro
        raza = input("Raza: ")
        if raza != "":cliente.perro.raza = raza
        print("---Cliente modificado---")
        datos_modificados = True
    
def baja():
    global datos_modificados
    dni = input("DNI del cliente a dar de baja: ")
    cliente = datos_cliente(dni)
    if cliente == None: print("---El cliente con DNI " + dni + " no existe---")
    else:
        lista_clientes.remove(cliente)
        print("---Cliente borrado---")
        datos_modificados = True

def consulta_cliente():
    dni = input("DNI del cliente a consultar: ")
    cliente = datos_cliente(dni)
    if cliente == None: print("---El cliente con DNI " + dni + " no existe---")
    else:
        tabla = [[cliente.nombre, cliente.dni, cliente.perro.nombre, cliente.perro.raza]]
        tabla_con_formato = tabulate(tabla, ["Cliente", "DNI", "Perro", "Raza"])
        print(tabla_con_formato)

def consulta_global():
    tabla = []
    for cliente in lista_clientes:
        fila = [cliente.nombre, cliente.dni, cliente.perro.nombre, cliente.perro.raza]
        tabla.append(fila)
    tabla_con_formato = tabulate(tabla, ["Cliente", "DNI", "Perro", "Raza"])
    print(tabla_con_formato)

def salvar():
    with open(fichero_clientes, 'wb') as f:
        pickle.dump(lista_clientes, f)
    print("---Información de cliente guardada---")
    datos_modificados = False

while True:
    opcion = mostrar_opciones()
    if opcion == "1": alta()
    elif opcion == "2": baja()
    elif opcion == "3": modificacion()
    elif opcion == "4": consulta_cliente()
    elif opcion == "5": consulta_global()
    elif opcion == "6": salvar()
    elif opcion == "7":
        if datos_modificados :
            respuesta = input("¿Quiere guardar los cambios realizados?(s/n) ")
            if respuesta == "s" : salvar()
        break
    else:print("---Opción no válida---")
    






