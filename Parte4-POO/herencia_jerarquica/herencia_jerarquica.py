class Robot:
  def __init__(self, nombre):
    self.nombre = nombre

  def saludar(self):
    return f"{self.nombre} dice hola."


class RobotExplorador(Robot):
  
  def explorar(self):
    return f"{self.nombre} está explorando el terreno."
  
  
class RobotCocinero(Robot):
  
  def cocinar(self):
    return f"{self.nombre} está preparando una deliciosa comida."


# Ejemplo de uso
robot1 = RobotExplorador(nombre="Rover")
robot2 = RobotCocinero(nombre="ChefBot")
# Usar los métodos heredados
print(robot1.saludar()) # Saludo del RobotExplorador
print(robot2.saludar()) # Saludo del RobotCocinero
# Usar métodos específicos de cada clase
print(robot1.explorar())
print(robot2.cocinar())