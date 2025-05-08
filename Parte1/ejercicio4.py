"""
Escribe un programa que pida al usuario su año de nacimniento
calcule su edad y genere un mensaje de saludo personalizado
que incluya su nombre y la edad calculada

"""

from datetime import datetime


def calcaular_edad(fechaNacimiento):
    fecha_actual = datetime.now().year
    edad = fechaNacimiento - fecha_actual
    return edad


fecha_nacimiento = print("A continuacion Ingresa tu año de nacimiento")
tuEdad = calcaular_edad(fecha_nacimiento)
print(f"Tu edad es {tuEdad}")
