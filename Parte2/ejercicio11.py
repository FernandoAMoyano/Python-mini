"""
Piedra, papel y tijera

En cada ronda del juego del cachipun los dos competidores
deben elegir entre jugar tijera, papel, o piedra.

Las reglas para decidir quien gana la ronda son:
- Tijera le gana a papel
- Papel le gana a piedra
- Piedra le gana a tijera
- Todas las demas combinaciones son empates.

El ganador del juego es el primero que gane tres rondas.

Escriba un programa que pregunte a cada jugador cual es su jugada, muestre
cual es el marcador despues de cada ronda y termine cuando uno de ellos haya ganado tres
rondas.Los jugadores deben indicar su jugada escribiendo tijera papel o piedra.

"""

# Juego: Piedra, Papel o Tijera

rondas = 0
puntaje_competidor_1 = 0
puntaje_competidor_2 = 0

# El juego continúa hasta que uno de los jugadores gana 3 rondas
while puntaje_competidor_1 < 3 and puntaje_competidor_2 < 3:
    jugada_1 = (
        input("Jugador 1, ingresa tu jugada (piedra, papel o tijera): ").strip().lower()
    )
    jugada_2 = (
        input("Jugador 2, ingresa tu jugada (piedra, papel o tijera): ").strip().lower()
    )

    rondas += 1

    if jugada_1 == jugada_2:
        print(f"Ronda {rondas}: Empate")
    elif (
        (jugada_1 == "tijera" and jugada_2 == "papel")
        or (jugada_1 == "papel" and jugada_2 == "piedra")
        or (jugada_1 == "piedra" and jugada_2 == "tijera")
    ):
        puntaje_competidor_1 += 1
        print(f"Ronda {rondas}: Gana Jugador 1")
    elif (
        (jugada_2 == "tijera" and jugada_1 == "papel")
        or (jugada_2 == "papel" and jugada_1 == "piedra")
        or (jugada_2 == "piedra" and jugada_1 == "tijera")
    ):
        puntaje_competidor_2 += 1
        print(f"Ronda {rondas}: Gana Jugador 2")
    else:
        print("Entrada inválida. Asegúrate de escribir piedra, papel o tijera.")
        rondas -= 1  # No se cuenta la ronda si hay error
        continue

    print(
        f"Marcador => Jugador 1: {puntaje_competidor_1} | Jugador 2: {puntaje_competidor_2}\n"
    )

# Mostrar al ganador
if puntaje_competidor_1 == 3:
    print("¡Jugador 1 ha ganado el juego!")
else:
    print("¡Jugador 2 ha ganado el juego!")
