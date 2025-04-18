"""
Escribe un programa que genere un numero aleatorio entre 1 y 100
y permita al usuario adivinar el numero, El programa debe brindar
pistas (el numero secreto es mayor) y debe continuar pidiendo al usuario
que adivine hasta que acierte, al finalizar, debe mostrar el numero de intentos

"""

from random import randint

numero_aleatorio = randint(1, 100)
intentos_totales = 3

while intentos_totales >= 1:
    numero_usuario = int(
        input(
            "Ingresa un numero para intentar adivinar el numero secreto entre 1 y 100"
        )
    )
    if numero_usuario == numero_aleatorio:
        print(f"Adivinaste!! el numero era {numero_usuario}")
        break
      
    intentos_totales-=1
    
    if intentos_totales == 0:
      print("Te quedaste sin intentos, Perdiste!!!")
      print(f"El numero era {numero_aleatorio}")
      break
    
    if numero_usuario - numero_aleatorio > 0:
      print("El numero es mas chico")
    else:
      print("El numero es mas grande")
    print(f"Te quedan {intentos_totales} intentos")