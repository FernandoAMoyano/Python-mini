"""
Anagrama:

Escribe una funcion que reciba dos palabras y retorne
verdadero o falso segun sean o no anagramas
- Un Anagrama consiste en formar una palabra reordenando.
  Todas las letras de otra palabra inicial.
- No hace falta comprobar que ambas palabras existen.
- Dos palabras exactamente iguales no son anagramas.
- Ambas palabras tienen la misma cantidad de letras.
- Las letras que forman parte de la palabra son las mismas

"""

def es_anagrama(palabra1, palabra2):
    # Normalizamos a minúsculas
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    # Si son iguales o tienen diferente largo, no son anagramas
    if palabra1 == palabra2 or len(palabra1) != len(palabra2):
        return False

    # Contamos las letras de ambas palabras
    contador1 = {}
    contador2 = {}

    for letra in palabra1:
        if letra in contador1:
            contador1[letra] += 1
        else:
            contador1[letra] = 1

    for letra in palabra2:
        if letra in contador2:
            contador2[letra] += 1
        else:
            contador2[letra] = 1

    print(contador1)
    print(contador2)
    # Comparamos ambos diccionarios
    return contador1 == contador2

# Ejemplo de uso
p1 = input("Ingresa la primera palabra: ")
p2 = input("Ingresa la segunda palabra: ")

if es_anagrama(p1, p2):
    print("✅ Son anagramas")
else:
    print("❌ No son anagramas")




