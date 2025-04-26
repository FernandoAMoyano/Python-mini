"""
Escribe un programa que cuente el numero de vocales
en una cadena de texto proporcionada por el usuario

"""

vocales = ["a", "e", "i", "o", "u"]
cadena_usuario = input("Ingresa a continuacion una cadena de texto")
numero_vocales = 0

for vocal in vocales:
    for letra in cadena_usuario:
        if vocal == letra:
            numero_vocales += 1

print(f"tu palabra tiene {numero_vocales} vocales")
