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



# Formacion de equipos de dos jugadores = 4 equipos
def formar_equipos(jugadores):
    partidos = []
    for i in range(0, len(jugadores), 2):
        jugador1 = jugadores[i]
        jugador2 = jugadores[i + 1]

        partidos.append(
            {
                "partido": i // 2 + 1,
                "jugadores": (jugador1, jugador2),
            }
        )
    return partidos


def solicitar_ganadores(partidos: list):
    ganadores = []
    for partido in partidos:
      
        jugador1, jugador2 = partido["jugadores"]
        print(f"Partido {partido['partido']} - {jugador1} vs {jugador2}\n")

        while True:
            ganador = input("Quien fue el ganador?").strip()
            if ganador in (jugador1, jugador2):
                ganadores.append(ganador)
                break
            else:
                print("El nombre no coincide con los jugadores")
    return ganadores


def ejecutar_torneo(jugadores):
    ronda = 1
    while len(jugadores) > 1:
        print(f"\n🏆 RONDA {ronda} - Jugadores: {jugadores}")
        partidos = formar_equipos(jugadores)
        jugadores = solicitar_ganadores(partidos)
        ronda += 1

    print(f"\n🎉 El campeón del torneo es: {jugadores[0]} 🏆")


    """
    j.values()          # devuelve: dict_values(['Nadal'])
    list(j.values())    # convierte eso en: ['Nadal']
    list(j.values())[0] # accede al primer (y único) valor: 'Nadal'
    """

if __name__=="__main__":
  
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

  nombres_jugadores = [list(j.values())[0] for j in listado_competidores]
  ejecutar_torneo(nombres_jugadores)
