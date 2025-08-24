class Maquina:
    def encender(self):
        return "La máquina se ha encendido"


class SerVivo:
    def respirar(self):
        return "El ser vivo está respirando"


class Robot(Maquina, SerVivo):
    def trabajar(self):
        return "El robot está realizando una tarea"


# Ejemplo de Uso
mi_robot = Robot()
# Llamamos a métodos heredados
print(mi_robot.encender())  # Heredado de Maquina
print(mi_robot.respirar())  # Heredado de SerVivo
print(mi_robot.trabajar())  # Propio de Robot
