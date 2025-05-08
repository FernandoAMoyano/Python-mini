"""
Escribe una funcion que permita calcular el factorial
de un numero

"""


def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    print(factorial)

calcular_factorial(4)
