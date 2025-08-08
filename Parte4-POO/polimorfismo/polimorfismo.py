import math

class Forma:
    def calcular_area(self):
        pass

# Clase concreta
class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

# Otra clase concreta
class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

# Función que utiliza polimorfismo
def calculate_total_area(formas):
    total = 0
    for forma in formas:
        total += forma.calcular_area()
    return total

# Uso del polimorfismo
formas = [
    Circulo(5),
    Rectangulo(3, 4),
    Circulo(2)
]
total_area = calculate_total_area(formas)
print(f"Total area: {total_area}")
