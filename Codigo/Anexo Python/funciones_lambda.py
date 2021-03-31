def escalar(numero):
    return lambda multiplicador : multiplicador * numero

doblar = escalar(2)
triplicar = escalar(3)

numero = int(input("Escriba un número: "))

numero_doblado = doblar(numero)
numero_triplicado = triplicar(numero)

print("El doble de "+str(numero)+ " es "+str(numero_doblado))
print("El triple de "+str(numero)+ " es "+str(numero_triplicado))
