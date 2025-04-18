"""
Escribe un programa que permita realizar la division
de dos numeros siempre y cuando el denominador sea 0

"""

from math import sqrt


def dividir_numero(numerador, denominador):
    resultado = numerador / denominador
    return round(resultado, 2)


while True:

    primer_numero = int(input("A Continuacion ingresa el primer numero"))
    segundo_numero = int(input("A continuacion ngresa el segundo numero"))
    if segundo_numero == 0:
        print("No puedes dividir por 0")
        continue
    numero_dividido = dividir_numero(primer_numero, segundo_numero)
    print(numero_dividido)
    break
  
"""
def dividir_numero(numerador, denominador):
    resultado = numerador / denominador
    return round(resultado, 2)

# Variable de control del bucle
division_valida = False

while not division_valida:
    primer_numero = int(input("A continuación, ingresa el primer número: "))
    segundo_numero = int(input("A continuación, ingresa el segundo número: "))

    if segundo_numero == 0:
        print("❌ No puedes dividir por 0. Intenta de nuevo.")
    else:
        numero_dividido = dividir_numero(primer_numero, segundo_numero)
        print(f"✅ El resultado es: {numero_dividido}")
        division_valida = True  # Se cambia la condición para salir del bucle

"""
    
