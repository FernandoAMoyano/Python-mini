"""
Escribe un programa que convierta una temperatura dad en
grados Celsius a grados Farhenheit

"""


def convertir_grados(gradosCelsius):
    gradosFahrenheit = float(gradosCelsius * (9 / 5) + 32)
    return gradosFahrenheit


temperatura = float(input("ingresa la temperatura en grados Celsius"))
gradosConvertidos = convertir_grados(temperatura)
print(f"{temperatura}°C son {gradosConvertidos:.2f}°F")
