FICHERO = "miFichero.txt"
empresa1 = {"nombre":"Empresa1", "direccion":"Suiza", "facturacion":1000}
empresa2 = {"nombre":"Empresa2", "direccion":"Irlanda", "facturacion":2000}
lista_empresas = [empresa1, empresa2]

def mostrar_datos_empresas(lista_empresas):
    for empresa in lista_empresas:
        for clave, valor in empresa.items():
            print(clave + ":" + str(valor))
        print("---")

print("Se procede a guardar los datos de las siguientes empresas")
mostrar_datos_empresas(lista_empresas)

with open(FICHERO, "w") as f:
    for empresa in lista_empresas:
        for clave, valor in empresa.items():
            f.write(clave + ":" + str(valor) + "#")
        f.write("\n")

lista_empresas_cargadas = []
f = open(FICHERO, "r")
for linea in f:
    empresa = {}
    lista_pares_clave_valor = linea.split("#")
    lista_pares_clave_valor.pop()
    for clave_valor in lista_pares_clave_valor:
        lista_clave_valor = clave_valor.split(":")
        clave = lista_clave_valor[0]
        valor = lista_clave_valor[1]
        empresa[clave] = valor
    lista_empresas_cargadas.append(empresa)

print("Se han leído los datos de la siguientes empresas")
mostrar_datos_empresas(lista_empresas_cargadas)




