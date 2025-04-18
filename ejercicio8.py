"""
Escribe un programa que solicite tres lados de
un triangulo e indique si es equilatero, iscoceles o escaleno

"""


def comprobar_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        if lado1 == lado2 and lado2 == lado3:
            return f"El triangulo es equilatero"
        return f"El triangulo es iscoceles"
    return f"El triangulo es escaleno"


lado_1 = int(input("Ingresa el valor para el primer lado "))
lado_2 = int(input("Ingresa el valor para el segundo lado "))
lado_3 = int(input("Ingresa el valor para el tercer lado "))

print(comprobar_triangulo(lado_1, lado_2, lado_3))
