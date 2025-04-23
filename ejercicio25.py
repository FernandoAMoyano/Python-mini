"""
Escribe una funcion que permita calcular el factorial
de un numero

"""


def calcularFactorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    print(factorial)

calcularFactorial(4)
