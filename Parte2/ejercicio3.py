"""
Escribir un programa que pida al usuario un numero entero
y muestre por pantalla si es un numero primo o no

numeros Primos:

- Divisible por si mismo y por 1
-
"""

numero_usuario = input("A continuacion ingresa un numero")


for i in range(2, numero_usuario):
    if numero_usuario % 2 == 0:
        print(f"El numero {numero_usuario} no es primo")
    else:
        print(f"El numero {numero_usuario} es primo")
