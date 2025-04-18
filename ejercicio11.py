"""
Escribe un programa que solicite al usuario su nombre
edad y numero de telefono. Verifica que ninguno de estos datos esté
vacio o sea un valor falso (por ejemplo 0).

"""

nombre = input("Ingresa tu nombre")
edad = input("Ingresa tu edad")
numero = input("Ingresa tu numero")

mensaje = ""


def es_numero(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False


if not (nombre or nombre.isspace()):
    mensaje += "📢El nombre debe contener valores validos\n"
elif es_numero(nombre):
    mensaje += f"El nombre no puede ser un numero\n"
else:
    mensaje += f"Nombre : {nombre}\n"


#  comprobar la entrada para la edad
if not (edad or edad.isspace()):
    mensaje += f"📢La edad debe contener valores validos\n"
elif es_numero(edad):
    edad_num = int(edad)
    if edad_num == 0:
        mensaje += "La edad no puede ser 0\n"
    else:
        mensaje += f"Edad : {edad_num}"
else:
    mensaje += f"📢La edad debe ser un numero\n"


#  comprobar la entrada para el numero Telfónico
if not (numero or numero.isspace()):
    mensaje += f"📢El numero debe contener valores validos\n"
elif es_numero(numero):
    numero_num = int(numero)
    if numero_num == 0:
        mensaje += "El numero no puede ser 0"
    else:
        mensaje += f"Numero : {numero_num}"
else:
    mensaje += f"📢El numero telefónico debe ser un numero"


print(mensaje)
