class Maquina:
  def __init__(self, marca):
    self.marca = marca
  def encender(self):
    return f"La máquina de marca {self.marca} se ha encendido."
  
  
class Robot(Maquina):
  def __init__(self, marca, tipo):
    super().__init__(marca) # Llamada al constructor de la clase base
    self.tipo = tipo
    
    
def saludar(self):
  return f"Soy un robot de tipo {self.tipo}. ¡Hola, mundo!"

# Modo de Uso
mi_robot = Robot(marca="RoboTech", tipo="Android")
print(mi_robot.encender()) # Método heredado de Maquina
print(mi_robot.saludar()) # Método propio de Robot