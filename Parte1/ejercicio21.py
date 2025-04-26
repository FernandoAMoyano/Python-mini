"""
Crea una tupla de numeros y verifica si el numero ingresado
por el usuario existe

"""

mis_numeros = (1, 3, 4, 2, 5, 2, 3, 4)
numero_usuario = int(input("Ingresa un numero del 1 al 10"))

if numero_usuario in mis_numeros:
    print(f"El numero {numero_usuario} esta dentro de la lista")
