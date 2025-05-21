"""
1. Conversor de monedas. Crea una clase Moneda que
   permita la conversion entre monedas (ej. dolares a pesos)
-  Implementa los metodos __str__ y __add__ para mostrar la
   cantidad convertida y sumar cantidades en diferentes
   monedas.

2. Registro de Tareas. Crea una clase Tarea que almacene
   informacion sobre tareas pendientes.
-  Implementa los metodos
   __str__ y __len__ para mostrar detalles de la tarea y contar
   cuantas tareas hay en la lista.

3. Baraja de Cartas. Crea una clase Carta que represente una
   carta de la baraja.
-  Implementa los metodos __str__ y __getitem__
   para mostrar la carta y acceder a sus atributos (por ejemplo, palo y valor)

4. Agenda de contactos. Crea una clase Contacto que almacene informacion
   sobre personas en una agenda.
-  Implementa los metodos __str__ y __setitem__ para mostrar detalles
   del contacto y modificar sus atributos(por ejemplo, numero de telefono)

"""

""" 1 """


class Moneda:
    def __init__(self, cantidad, moneda="pesos"):
        self.cantidad = cantidad
        self.moneda = moneda.lower()

    def dolares_a_pesos(self):
        dolares = self.cantidad * 1200
        return dolares

    def pesos_a_dolares(self):
         pesos = self.cantidad / 1200
         return pesos
      
    def __str__(self):
        match self.moneda:
            case "usd":
                return f"{self.cantidad} dolares son {self.dolares_a_pesos()} pesos"
            case "pesos":
                return f"{self.cantidad} pesos son {self.pesos_a_dolares()} dolares"
            case _:
                return "Moneda no soportada"
    
    
   
       
if __name__ == "__main__":
    moneda = Moneda(100,"usd")
    print(moneda)
    moneda = Moneda(10000,"pesos")
    print(moneda)
