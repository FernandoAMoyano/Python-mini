"""
Escribe un programa que a partir de un numero entero
positivo muestre por pantalla si es par o impar

"""


def chequear_numero_par(numero):
    if numero % 2 == 0:
        return f"el numero {numero} ingresado es PAR"
    else:
        return f"El numero {numero} es IMPAR"


numeroIngresado = int(input("A continuacion ingresa un numero"))
es_par = chequear_numero_par(numeroIngresado)
print(es_par)
