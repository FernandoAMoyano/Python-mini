from typing import List

MAX_TRAMOS = 3  # Límite de tramos permitidos

def ingresar_tiempos() -> List[int]:
    """Permite al usuario ingresar los tiempos de los tramos."""
    tramos_de_viaje = []
    while len(tramos_de_viaje) < MAX_TRAMOS:
        try:
            tiempo = int(input("Ingresa el tiempo para el tramo (en minutos, 0 para terminar): "))
            if tiempo < 0:
                print("El tiempo no puede ser negativo. Intenta nuevamente.")
            elif tiempo == 0:
                break
            else:
                tramos_de_viaje.append(tiempo)
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")
    return tramos_de_viaje

def calcular_tiempo_total(tramos: List[int]) -> str:
    """Calcula el tiempo total en formato horas:minutos."""
    tiempo_total = sum(tramos)
    horas = tiempo_total // 60
    minutos = tiempo_total % 60
    return f"{horas} horas : {minutos} minutos"

def main():
    print("Bienvenido al calculador de tiempo de viaje.")
    tramos_de_viaje = ingresar_tiempos()
    if not tramos_de_viaje:
        print("No se ingresaron tramos de viaje.")
    else:
        tiempo_formateado = calcular_tiempo_total(tramos_de_viaje)
        print(f"El viaje duró: {tiempo_formateado}")

if __name__ == "__main__":
    main()