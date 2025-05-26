"""
Crea una clase base llamada instrumento con métodos
como tocar() y afinar().Luego crear subclases para representar
diferentes instrumentos como Guitarra, Piano, y Flauta. Implementa
métodos de manera diferente en cada subclase para simular la
ejecucion y la afinacion de cada instrumento

"""


class Instrumento:

    def tocar(self):
        pass

    def afinar(self):
        pass


class Guitarra(Instrumento):
    def __init__(self, tipo="clasica"):
        self.tipo = tipo

    def __str__(self):
        return f"Tipo de guitarra {self.tipo}"

    def tocar(self):
        return f"Tocando La GUITARRA de tipo {self.tipo}"

    def afinar(self):
        return f"Afinando la GUITARRA {self.tipo}"


class Piano(Instrumento):
    def __init__(self, tipo="De Cola"):
        self.tipo = tipo

    def __str__(self):
        return f"Tipo de piano: {self.tipo}"

    def tocar(self):
        return f"Tocando el PIANO de tipo {self.tipo}"

    def afinar(self):
        return f"Afinando el PIANO"


guitarra1 = Guitarra("electrica")
print(guitarra1.afinar())

piano1=Piano("Organo")
print(piano1.tocar())
