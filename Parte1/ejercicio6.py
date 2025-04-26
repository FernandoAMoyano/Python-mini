"""
Escribe un programa que a apartir de un numero positivo
muestre en pantalla si es primo o no

1_ Son mayores que 1.(El 1 no se considera primo.)

2_ Solo tienen dos divisores positivos distintos:
   El número 1 Y sí mismos

3_ No pueden dividirse exactamente por ningún otro
número aparte de 1 y ellos mismos
(es decir, dejan residuo con cualquier otro divisor).

4_ No son productos de otros números enteros
distintos de 1 y el propio número.

5_ El primer número primo es el 2, y es también el único número primo par.
"""


def comprobar_numero_primo(numero):
    if numero <= 1:
        return f"El numero {numero} NO ES PRIMO"
    for i in range(2, numero):
        if numero % i == 0:
            return f"El numero {numero} NO ES PRIMO "
    return f"El numero {numero} ES PRIMO"


mi_numero = int(input("A continuacion ingresa un numero"))
es_primo = comprobar_numero_primo(mi_numero)
print(es_primo)
