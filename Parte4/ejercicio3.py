"""
Escribe un programa basado en la programacion orientada
a objetos (POO) con herencia simple en base al video
juego Mario Bros.

1_ Crear una clase base llamada Personaje , esta clase
    contendra los atributos y metodos comunes a todos
    los personajes del juego. Por ejemplo los atributos
    podrian ser nombre, vidas y poder. Los metodos podrian
    ser mover, saltar, caer

2_ Crea clases derivadas para cada personaje especifico.
   estas clases heredaran de la clase "Personaje" y
   podrán tener atributos y metodos adicionales. Por ejemplo
   la clase Mario podria tener un metodo adicional lanzar_fuego()
   mientras que la clase Luigi podria tener un metodo adicional
   usar_hongo()

3_ Crea clases base para los enemigos. Esta Clase contendrá
  los atributos y metodos comunes a todos los enemigos. Por
  ejemplo los metodos comunes a todos los enemigos. Por ejemplo
  los atributos podrian ser tipo, daño y los metodos mover, atacar, etc

4_ Crear clases derivadas de la clase enemigo. Estas clases heredarán
   de la clase base "Enemigo" y podran tener atributos y metodos
   adicionales. Por ejemplo la clase "Koopa Troopa" podria tener un
   metodo adicional usar_casco(), mientras que la clase "Goomba" podria
   tener un metodo esconder().
"""


class Personaje:
    def __init__(self, nombre, vidas, poder):
        self.nombre = nombre
        self.vidas = vidas
        self.poder = poder

    def mover(self):
        print(f"{self.nombre} MOVIENDOSE")

    def saltar(self):
        print(f"{self.nombre} SALTANDO")

    def caer(self):
        print(f"{self.nombre} CAYENDO")


class Mario(Personaje):

    def __init__(self, nombre, vidas, poder):
        super().__init__(nombre, vidas, poder)

    def lanzar_fuego(self):
        print(f"{self.nombre} Lanzando fuego")


class Luigi(Personaje):

    def __init__(self, nombre, vidas, poder):
        super().__init__(nombre, vidas, poder)

    def usar_hongo(self):
        print(f"{self.nombre} Usando Hongo")


class Enemigo:
    def __init__(self, tipo, daño):
        self.tipo = tipo
        self.daño = daño

    def mover(self):
        print(f"Enemigo {self.tipo} MOVIENDOSE")

    def atacar(self):
        print(f"Enemigo {self.tipo} ATACANDO")


class Koopa_Troopa(Enemigo):
    def __init__(self, tipo, daño):
        super().__init__(tipo, daño)

    def usar_casco(self):
        print("KOOPA SE HA colocado el Casco ")


class Goomba(Enemigo):

    def __init__(self, tipo, daño):
        super().__init__(tipo, daño)

    def esconder(self):
        print("Goomba ESCONDIDO")


# Personajes principales
mario = Mario("Mario", 3, "Lanzar bolas de fuego")
mario.lanzar_fuego()
mario.mover()

luigi = Luigi("Luigi", 3, "Aplastar enemigos")
luigi.caer()

# Enemigos
goomba = Goomba("Basico", "sutil")
goomba.esconder()

koopa_tropa = Koopa_Troopa("intermedio", "fuerte")
koopa_tropa.usar_casco()
