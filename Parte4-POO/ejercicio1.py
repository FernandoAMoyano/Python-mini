""" 
Intenta crear una clase Dado que cumpla los siguientes requerimientos

- El dado debe tener un numero de caras(por defecto 6)
- Debe ser capaz de lanzarse y devolver un numero aleatorio
  entre 1 y el numero de caras

"""

import random

class Dado:
  def __init__(self, caras=6):
    self.caras = caras
  
  def lanzarse(self):
     numero_aleatorio = random.randint(1, self.caras)
     print(numero_aleatorio)
  

if __name__=="__main__":
  dado=Dado()
  dado.lanzarse()