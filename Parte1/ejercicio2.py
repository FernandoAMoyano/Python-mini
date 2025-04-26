"""
Escribe un programa que convierta una temperatura dad en
grados Celsius a grados Farhenheit

"""


def convertidorDeGrados(gradosCelsius):
    gradosFahrenheit = float(gradosCelsius * (9 / 5) + 32)
    return gradosFahrenheit


temperatura = float(input("ingresa la temperatura en grados Celsius"))
gradosConvertidos = convertidorDeGrados(temperatura)
print(f"{temperatura}°C son {gradosConvertidos:.2f}°F")
