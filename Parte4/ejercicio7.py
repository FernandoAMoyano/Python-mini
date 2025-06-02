"""
Area y Perimetro

Crea una clase Reactangulo que permita calcular su area
y su perimetro. Además, crea en una aplicacion de consola
que permita al usuario crear un objeto Perimetro y realizar los
calculos

"""


class Rectangulo:

    def __init__(self, base, altura):
        self.__base = float(base)
        self.__altura = float(altura)

    def calcular_perimetro(self):
      return  2 * (self.__base + self.__altura)
      
    def calcular_area(self):
      return  self.__base * self.__altura
      


if __name__ == "__main__":

    base = input("Ingresa la base del rectangulo en cm")
    altura = input("Ingresa la altura del rectangulo en cm")

    rectangulo1 = Rectangulo(base, altura)
    print(f"El area del reactangulo es {rectangulo1.calcular_area()} cm")
