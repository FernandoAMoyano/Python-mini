"""
1 - Crea una funcion anónmima(lambda) que calcule el promedio de
  un arreglo de numeros enteros
2 - Escribe una funcion anónima que calcule el factorial dado un numero
  entero
3 - Crea una funcion anónima que permita conocer si un numero es par.
4 - Dado un arreglo de numeros enteros, crea una funcion anónima que
  retorne una lista con los numeros pares.
5 - Utiliza una funcion lambda para elevar al cuadrado cada elemento
  de una lista de numeros
"""

""" 1 """
from functools import reduce

numeros_enteros = [9, 16, 32, 98, 89]

porcentaje = reduce(lambda x, y: x + y, numeros_enteros)
print(porcentaje / len(numeros_enteros))


""" 2 """
factorial = lambda x: reduce(lambda a, b: a * b, range(1, x + 1))
print(factorial(5))


""" 3 """
is_par = lambda x: x % 2 == 0


if is_par(9):
    print("es par")
else:
    print("no es par")


""" 4 """
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros_enteros))
print(numeros_pares)


""" 5 """
numeros_al_cuadrado=list(map(lambda x: x**2, numeros_pares))
print(numeros_al_cuadrado)