"""
La secuencia de Collatz de un numero entero se construye
de la siguiente forma:
- Si es impar, se le multiplica tres y se le suma uno
-Si el numero es par se lo divide por dos
- La sucesion termina al llegar a uno
- Desarrolle un programa que entregue la secuencia de Collatz
de un numero entero

"""

try:
    numero_usuario = int(input("Ingresa un numero"))
    if numero_usuario <= 0:
        print("Ingresa un numero mayor a 0")
    else:
        collatz = f"{numero_usuario}"
    while numero_usuario != 1:
        if numero_usuario == 1:
            break
        elif numero_usuario % 2 == 0:
             numero_usuario = numero_usuario // 2
        else:
            numero_usuario = numero_usuario * 3 + 1
        collatz += f"->{str(numero_usuario)}"
    print(collatz)
except ValueError:
    print("Ingresa un numero valido")
