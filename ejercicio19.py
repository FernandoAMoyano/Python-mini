"""
Crea una lista de numeros que cuente el numero de veces que aprece
el numero ingresado por el usuario

"""

from itertools import count


lista_numeros = []



while len(lista_numeros) < 10:
    numero_usuario = int(input("Ingresa una lista de 10 numeros del 1 al 10"))
    lista_numeros.append(numero_usuario)
    
print(lista_numeros)


for numero in set(lista_numeros):
    repeticiones = lista_numeros.count(numero)
    print(f"El número {numero} aparece {repeticiones} veces.")


