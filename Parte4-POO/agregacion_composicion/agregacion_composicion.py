class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def girar(self):
        return f"Girando motor de {self.potencia} vatios"


class BrazoRobótico:
    def __init__(self, longitud):
        self.longitud = longitud
        self.motor = Motor(100)  # Composición

    def mover(self):
        self.motor.girar()
        return f"Brazo robótico de {self.longitud} cm se mueve"


class Herramienta:
    def __init__(self, nombre):
        self.nombre = nombre

    def usar(self):
        return f"Usando {self.nombre}"


class Robot:
    def __init__(self, nombre):
        self.nombre = nombre
        self.brazo = BrazoRobótico(50)  # Composición
        self.herramientas = []  # Agregación

    def agregar_herramienta(self, herramienta):
        self.herramientas.append(herramienta)

    def trabajar(self):
        acciones = [f"{self.nombre} está trabajando"]
        acciones.append(self.brazo.mover())
        for herramienta in self.herramientas:
            acciones.append(herramienta.usar())
        return "\n".join(acciones)


# Modo de uso
# Crear herramientas
llave_inglesa = Herramienta("Llave inglesa")
soldador = Herramienta("Soldador")
# Crear robots y asignar herramientas
robot1 = Robot("Alpha")
robot1.agregar_herramienta(llave_inglesa)
robot1.agregar_herramienta(soldador)
robot2 = Robot("Beta")
robot2.agregar_herramienta(llave_inglesa)  # Compartiendo la misma llave inglesa
# Ejecutar robots
print("\nRobot Alpha:")
print(robot1.trabajar())
print("\nRobot Beta:")
print(robot2.trabajar())
