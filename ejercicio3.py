"""
Escribe un programa que pida al usuario los dos catetos de
un triangulo rectangulo y calcule la hipotenusa

"""

from math import sqrt


def calcularHipotenusa(catetA, catetoB):
    hipotenusa = float(sqrt(catetA ** 2 + catetoB ** 2))
    return hipotenusa


cateto1 = float(input("ingresa la medida para el primer cateto del triangulo"))
cateto2 = float(input("ingresa la medida para el segundo cateto del triangulo"))

hipotenusa = round(calcularHipotenusa(cateto1, cateto2), 2)
print(f"La hipotenusa es {hipotenusa}")
