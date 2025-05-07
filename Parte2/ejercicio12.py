"""
Torneo de Tenis

Escriba un programa para simular un campeonato de tenis.

- Primero, debe pedir al usuario que ingrese los
  nombres de ocho tenistas.
- A continuacion debe pedir los resultados de los partidos
  juntando los jugadores de dos en dos.El ganador de cada partido
  avanza a la ronda siguiente.

- El programa debe continuar preguntando ganadores
  de partidos hasta que quede un unico jugador, que es
  el campeon del torneo.
"""

""" ronda1=[
        {
         "partido1":(competidores["jugador1"], competidores["jugador2"]) ,
         "ganador":competidores["jugador1"]
        },
        {
          "partido2":(competidores["jugador3"], competidores["jugador4"]),
          "ganador":competidores["jugador1"]
        },
        {
          "partido3":(competidores["jugador5"], competidores["jugador6"]),
          "ganador":competidores["jugador1"]
        },
        {
          "partido3":(competidores["jugador7"], competidores["jugador8"]),
          "ganador":competidores["jugador1"]
        }      
       ] """

competidores = [
    {"jugador1": "Nadal"},
    {"jugador2": "Mezler"},
    {"jugador3": "Murray"},
    {"jugador4": "Soderling"},
    {"jugador5": "Djokovic"},
    {"jugador6": "Federer"},
    {"jugador7": "Del Potro"},
    {"jugador8": "peptito"},
]

ronda1 = []

# Formacion de equipos de dos jugadores = 4 equipos
for i in range(0, len(competidores), 2):
    jugador1 = list(competidores[i].values())[0]
    jugador2 = list(competidores[i + 1].values())[0]

    partido = {
        "partido": i // 2 + 1,
        "jugadores": (jugador1, jugador2),
    }
    ronda1.append(partido)


def mostrar_partidos(listado: list):
    for partido in listado:
        jugador1, jugador2 = partido["jugadores"]

        print(f"Partido {partido['partido']} - {jugador1} vs {jugador2}")
        ganador = input("Quien fue el ganador?")


mostrar_partidos(ronda1)
