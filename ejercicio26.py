"""
Escriba una funcion que reciba una lista de
numeros y devuelva el promedio

"""

from typing import List


def calcularPromedio(numeros: List[int]):
    suma = 0
    for numero in numeros:
        suma += numero
    promedio=suma / len(numeros)
    return print(f"El promedio de los numeros ingresados es {promedio}")


calcularPromedio([5, 2, 3, 4, 5])
