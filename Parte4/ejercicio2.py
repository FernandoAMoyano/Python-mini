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


""" 2 """


class Tarea:

    tareas_pendientes = []

    def __init__(self, tarea, estado="pendiente"):
        self.tarea = tarea
        self.estado = estado
        self.chequear_estado()

    def chequear_estado(self):
        if self.estado == "pendiente":
            if self.tarea not in Tarea.tareas_pendientes:
                Tarea.tareas_pendientes.append(self.tarea)
        else:
            if self.tarea in Tarea.tareas_pendientes:
                Tarea.tareas_pendientes.remove(self.tarea)

    def __str__(self):
        return f"Tarea: {self.tarea}, Estado: {self.estado}"

    def __len__(self):
        return len(Tarea.tareas_pendientes)


""" 3 """


class Carta:
    def __init__(self, numero, palo):
        self.numero = numero
        self.palo = palo

    def __str__(self):
        return f"Carta numero {self.numero} de {self.palo}"

    def __getitem__(self, clave):
        atributos = {"numero": self.numero, "palo": self.palo}

        if clave in atributos:
            return atributos[clave]
        else:
            raise KeyError(f"Atributo {clave} no valido")


class Contacto:
    lista_de_contactos = []

    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        Contacto.lista_de_contactos.append(self)

    def __setitem__(self, clave, valor):
        if hasattr(self, clave):
            setattr(self, clave, valor)
        else:
            raise KeyError(f"Atributo {clave} no valido")

    def __str__(self):
        return f"Contacto: {self.nombre} telefono: {self.telefono} "


if __name__ == "__main__":
    # 1- Conversor de monedas
    moneda = Moneda(100, "usd")
    print(moneda)
    moneda = Moneda(10000, "pesos")
    print(moneda)

    # 2- Registro de Tareas
    tarea1 = Tarea("estudiar", "completada")
    print(tarea1)
    tarea2 = Tarea("Programar", "pendiente")
    print(tarea1)
    tarea3 = Tarea("Hacer compras", "pendiente")
    print(tarea3)
    print(f"Cantidad de tareas pendientes: {len(tarea3)}")

    # 3- Cartas
    carta1 = Carta(7, "bastos")
    print(carta1["numero"])
    print(carta1)

    # Contacto
    contacto1 = Contacto("Fernando", 341234)
    print(contacto1)
    contacto1["nombre"] = "Claudio"
    print(contacto1)
    
    contacto2=Contacto("Hernesto",2342342)
    

    for c in contacto1.lista_de_contactos:
        print(c)
