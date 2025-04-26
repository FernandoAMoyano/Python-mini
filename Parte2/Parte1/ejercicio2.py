"""

Escriba un programa que pregunte al usuario la hora
actual t del reloj y un numero entero de
horas h, que indique que hora marcara el reloj
dentro de h horas

"""

hora_actual = int(input("Ingresa la hora actual"))
cantidad_horas = int(input("Ingresa una cantidad de horas"))

hora_futura = (hora_actual + cantidad_horas) % 24


if hora_futura == 0:
    hora_a_mostrar = 12
    periodo = "AM"
elif hora_futura < 12:
    hora_a_mostrar = hora_futura
    periodo = "AM"
elif hora_futura == 12:
    hora_a_mostrar = 12
    periodo = "PM"
else:
    hora_a_mostrar = hora_futura - 12
    periodo = "PM"

print(f"La hora dentro de {cantidad_horas} horas será: {hora_a_mostrar} {periodo}")
