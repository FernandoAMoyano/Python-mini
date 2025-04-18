"""
Escribe un programa que pida al usuario el radio de
un circulo y calcule el area

"""


def calcularArea(radio):
    PI = 3.14
    return PI * radio * radio


radio = float(input("Ingresa a continuacion el radio del circulo"))
area = calcularArea(radio)
print(f"El area del circulo es {area}")
