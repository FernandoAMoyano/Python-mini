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

listado_competidores = [
    {"jugador-1": "Nadal"},
    {"jugador-2": "Mezler"},
    {"jugador-3": "Murray"},
    {"jugador-4": "Soderling"},
    {"jugador-5": "Djokovic"},
    {"jugador-6": "Federer"},
    {"jugador-7": "Del Potro"},
    {"jugador-8": "peptito"},
]

ronda1 = []

# Formacion de equipos de dos jugadores = 4 equipos
def formar_equipos(competidores):
    for i in range(0, len(competidores), 2):
        jugador1 = list(competidores[i].values())[0]
        jugador2 = list(competidores[i + 1].values())[0]

        contrincantes = {
            "partido": i // 2 + 1,
            "jugadores": (jugador1, jugador2),
        }
        ronda1.append(contrincantes)


formar_equipos(listado_competidores)
print(ronda1)


def solicitar_ganadores(partidos: list):
    ganadores = []
    for partido in partidos:
        jugador1, jugador2 = partido["jugadores"]

        print(f"Partido {partido['partido']} - {jugador1} vs {jugador2}\n")
        ganadores= input("Quien fue el ganador?")
        ganadores.append({ganadores})
    return ganadores


ganadores_ronda_1 = solicitar_ganadores(ronda1)
print(ganadores_ronda_1)