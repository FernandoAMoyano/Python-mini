class Maquina:
  def __init__(self, marca):
    self.marca = marca
    
    
def encender(self):
  return f"La máquina de marca {self.marca} se ha encendido."


class Robot(Maquina):
  def __init__(self, marca, tipo):
    super().__init__(marca)
    self.tipo = tipo
    
    
def saludar(self):
  return f"Soy un robot de tipo {self.tipo}. ¡Hola, mundo!"


class RobotInteligente(Robot):
  def __init__(self, marca, tipo, nivel_inteligencia):
    super().__init__(marca, tipo)
    self.nivel_inteligencia = nivel_inteligencia
    
    
def tomar_decision(self):
  return f"Tomando una decisión de nivel{self.nivel_inteligencia}."


# Ejemplo de uso
mi_robot_inteligente = RobotInteligente(marca="AI Tech",
tipo="Android", nivel_inteligencia=5)
print(mi_robot_inteligente.encender()) # Método heredado de
Maquina
print(mi_robot_inteligente.saludar()) # Método heredado de Robot
print(mi_robot_inteligente.tomar_decision()) # Método propio de
RobotInteligente