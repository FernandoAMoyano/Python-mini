"""
Escribe una funcion que convierta un numero entero
a binario y otra que realice el calculo inverso

Consideraciones:

- Las funciones deben tener una sola responsabilidad clara.
- Se debe usar nombres descriptivos para las funciones variables
  y parametros.
- Se debe manejar los casos de error posibles( por ejemplo
  numeros negativos)

"""


def transformarABinario(numero):
    binario = ""
    denominador = 2
    while True:
        cociente = numero // denominador
        residuo = numero % denominador
        numero = cociente

        binario = str(residuo) + binario
        if cociente == 0:
            break
    print(binario)


transformarABinario(6)
