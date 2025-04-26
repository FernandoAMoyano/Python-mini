from typing import List

""" 
Tiempo de viaje:

Un viajero desea saber cuanto tiempo tomó un viaje que realizó.
él tiene la duracion en minutos de cada uno de los tramos del 
viaje.

- Desarrolle un programa que permita ingresar los tiempos de viaje
  de los tramos y entregue como resultado el tiempo total
  de viaje en formato hroas:minutos

El programa deja de pedir tiempo de viaje cuando se ingresa un 0

"""
tramos_de_viaje: List[int] = []
tiempo_total: int = 0
horas: int = 0
minutos: int = 0
while True:
    if len(tramos_de_viaje) > 3:
        break
    else:
        tiempo: int = int(input(f"A continuacion ingresa el tiempo para el tramo"))
        if tiempo == 0:
            print("El tramo debe tener un tiempo")
            continue
        else:
            tramos_de_viaje.append(tiempo)


for tramo in tramos_de_viaje:
    tiempo_total += tramo

if tiempo_total % 60 == 0:
    horas = tiempo_total // 60
elif tiempo_total < 60:
    horas = 00
    minutos = tiempo_total
else:
    horas = round(tiempo_total / 60)
    minutos = tiempo_total % 60
print(f"El viaje duró: {horas} horas :{minutos} minutos")
