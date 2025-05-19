"""
1- Escribe una funcion que tome una cantidad variable de
cadenas y las concatene en una sola cadena. Ej: "Hola Mundo"

2- Escribe una funcion que muestre la cantidad de argumentos
con nombre enviados.

3- Escribe una funcion que calcule el promedio de una cantidad
variable de números.
"""


""" 1 """
def construir_string(*strings):
    nuevo_string = ""
    for s in strings:
        nuevo_string += s
    return nuevo_string

saludo = construir_string("hola", " ", "como estas?")
print(saludo)


""" 2 """
def mostrar_nombre_argumento(**params):
  print(len(params.keys()))
    

mostrar_nombre_argumento(nombre="jose", edad=32)


""" 3 """
def calcular_promedio(*numbers):
  return sum(numbers)/len(numbers)

promedio=calcular_promedio(9,8,8)
print(promedio)