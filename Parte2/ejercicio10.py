"""
Torre y Alfil

Un tablero de ajederez es una grilla de ocho filas y ocho columnas,
numeradas de 1 a 8 Dos de las piezas del juego de ajedrez son el alfil
y la torre, el alfil se desplaza en diagonal mientras que la torre
se desplaza horizontal o verticalmente.Una pieza pude ser capturada por
otra si está en una casilla a la cual la otra puede desplazarse.

Escriba un programa que reciba como entrada las posiciones en el tablero
de un alfil y de una torre, e indique cual pieza captura a la otra.
"""

# torre_captura
# si la fila de la torre == a ala fila del alfil
# or
# la columna de la torre == a la columna del alfil


# alfil_captura
# si la fila del alfil - la fila de la torre ==

# la columna de la alfil - la columna de la torre

import typing


def posicionar_pieza(fila: int, columna: int):
    posicion_pieza = (fila, columna)
    return posicion_pieza


def chequear_captura(posicion_torre: tuple, posicion_alfil: tuple):
    if posicion_torre[0] == posicion_alfil[0] or (
        posicion_torre[1] == posicion_alfil[1]
    ):
        print("La Torre captura al alfil")
    elif abs(posicion_torre[0] - posicion_alfil[0]) == abs(
        posicion_torre[1] - posicion_alfil[1]
    ):
        print("El Alfil captura a la torre")
    else:
        print("Ninguna pieza captura a la otra")


fila_alfil = int(input("ingresa la fila para el alfil"))
columna_alfil = int(input("Ingresa la columna para el alfil"))

posicion_alfil = posicionar_pieza(fila_alfil, columna_alfil)

fila_torre = int(input("Ingresa la fila para la torre"))
columna_torre = int(input("Ingresa la columna para la torre"))

posicion_torre = posicionar_pieza(fila_torre, columna_torre)


chequear_captura(posicion_torre, posicion_alfil)
