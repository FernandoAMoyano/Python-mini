"""
Escribe un programa que cuente los caracteres de una cadena
de texto proporcionada por el usuario utilizando el for

"""

cadena_usuario=input("Ingresa una cadena de texto")

# Opcion 1
for letra in cadena_usuario:
  print(letra)
  
# Opcion 2
caracteres=list(cadena_usuario)
print(caracteres)