import clases
import os
import pickle
from tabulate import tabulate

fichero_clientes = "clientes.pkl"
lista_clientes = []
if os.path.exists(fichero_clientes):
    with open(fichero_clientes, 'rb') as f:
        lista_clientes = pickle.load(f)

def obtener_cliente(dni):
    for cliente in lista_clientes:
        if cliente.dni == dni: return cliente
    return None

def alta_cliente(dni, nombre_cliente, nombre_perro, raza):
        perro = clases.Perro(nombre_perro, raza)
        cliente = clases.Cliente(nombre_cliente, dni, perro)
        
        lista_clientes.append(cliente)
        print("---Cliente dado de alta---")

def modificacion_cliente(cliente, nombre_cliente, nombre_perro, raza):
    cliente.nombre = nombre_cliente
    cliente.perro.nombre = nombre_perro
    cliente.perro.raza = raza
    print("---Cliente modificado---")
    
def baja_cliente(cliente):
    lista_clientes.remove(cliente)
    print("---Cliente borrado---")

def informacion_cliente(cliente):
    tabla = [[cliente.nombre, cliente.dni, cliente.perro.nombre, cliente.perro.raza]]
    tabla_con_formato = tabulate(tabla, ["Cliente", "DNI", "Perro", "Raza"])
    return tabla_con_formato

def informacion_clientes():
    tabla = []
    for cliente in lista_clientes:
        fila = [cliente.nombre, cliente.dni, cliente.perro.nombre, cliente.perro.raza]
        tabla.append(fila)
    tabla_con_formato = tabulate(tabla, ["Cliente", "DNI", "Perro", "Raza"])
    return tabla_con_formato

def guardar():
    with open(fichero_clientes, 'wb') as f:
        pickle.dump(lista_clientes, f)
    print("---Información de cliente guardada---")




