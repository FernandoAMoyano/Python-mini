class Matematica:
  PI = 3.14159 # Variable de clase
  
  @staticmethod
  def suma(a, b):
    return a + b
  
  
  @staticmethod
  def resta(a, b):
    return a - b
  
  
  @staticmethod
  def multiplicacion(a, b):
    return a * b
  
  
  @staticmethod
  def division(a, b):
    if b != 0:
      return a / b
    else:
      raise ValueError("No se puede dividir por cero")
    
    
# Uso de la "clase estática"
print(Matematica.PI)
print(Matematica.suma(5, 3))
print(Matematica.resta(10, 4))
print(Matematica.multiplicacion(7, 2))
print(Matematica.division(9, 3))

try:
    print(Matematica.division(15, 0))
except ValueError as e:
  print(e)