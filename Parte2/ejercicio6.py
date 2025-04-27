"""
Escribir un programa que pida al usuario
un numero entero y muestre por pantalla un
triangulo rectangulo como el de mas abajo con tantos
renglones como indique el usuario.

"""

try:
    x = int(input("Ingresa un número: "))
    j = int(input("Ingresa la cantidad de renglones: "))

    if x < 0 or j < 0:
        raise ValueError("No se permiten números negativos.")

    renglon = ""
    for i in range(j):
        renglon += str(x)
        print(renglon)

except ValueError as e:
    print(f"Error: {e}")
