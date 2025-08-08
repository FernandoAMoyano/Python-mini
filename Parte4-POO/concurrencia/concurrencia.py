import threading
import time


class Contador(threading.Thread):
  def __init__(self, nombre):
    super().__init__()
    self.nombre = nombre
    
    
  def run(self):
    for i in range(5):
      print(f"{self.nombre}: {i}")
      time.sleep(1)
      
      
# Ejemplo de uso
# Crear e iniciar dos hilos
hilo1 = Contador("Hilo 1")
hilo2 = Contador("Hilo 2")
hilo1.start()
hilo2.start()
# Esperar a que ambos hilos terminen
hilo1.join()
hilo2.join()
print("Ambos hilos han terminado")