"""
Escribe un programa que pida al usuario el radio de
un circulo y calcule el area

"""


def calcular_area(radio):
    PI = 3.14
    return PI * radio * radio


radio = float(input("Ingresa a continuacion el radio del circulo"))
area = calcular_area(radio)
print(f"El area del circulo es {area}")
