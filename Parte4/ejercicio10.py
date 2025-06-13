"""

Kilometraje Recorrido. Crea una clase vehiculo que permita llevar
el kilometraje recorrido.

Atributos para definir:
  color, marca modelo y patente del vehiculo

Metodos para:
  1_ Conducir el auto(debe aceptar la cantidad de Kilometros y sumarlo
     al kilometraje recorrido).
  2_ Metodo para mostrar en pantalla los datos del vehiculo y el correspondiente kilonmetraje
  3_ Escribe una aplicación de consola que permita al usuario:
      -Conducir varios kilometros
      -Mostrar el kilometrahe actual hasta que decida detenerse.
      -Al finalizar debera mostrar los datos del vehiculo y el kilometraje recorrido.

"""


class Vehiculo:

    def __init__(self, marca: str, modelo: int, patente: str, kilometraje: int):
        self.marca: str = marca
        self.modelo: str = modelo
        self.patente: str = patente
        self.kilometraje: int = kilometraje
        self.kilometros_recorridos: int = 0

    def conducir(self, kilometros_por_conducir: int):
        if kilometros_por_conducir > 0 and isinstance(kilometros_por_conducir, int):
            for i in range(0, kilometros_por_conducir + 1, 10):
                print(f"Kilometro {i}")
                detenerse = input(
                    "Presiona ENTER para continuar, o escribe 'ESC' para detenerse: "
                )
                if detenerse.strip().upper() == "ESC":
                    print(
                        f"Conducción finalizada. Kilómetros recorridos hasta ahora: {self.kilometros_recorridos} km."
                    )
                    break
                self.kilometros_recorridos += 10
            self.kilometraje += self.kilometros_recorridos

    def mostrar_kilometraje_recorrido(self):
        return f"Kilometraje recorrido: {self.kilometros_recorridos}Km"

    def mostrar_kilometraje_total(self):
        return f"Kilometraje total {self.kilometraje}"

    def __str__(self):
        return f"Marca: {self.marca} Modelo: {self.modelo} Patente: {self.patente} Kilometraje: {self.kilometraje}"


# --------------------------------------------------------------------


def comprar_auto():
    marca = input("Ingresa la marca del vehiculo")
    modelo = input("Ingresa el modelo del vehiculo")
    patente = input("Ingresa la patente del vehiculo")
    kilometraje = int(input("Ingresa el kilometraje del vehiculo"))

    return Vehiculo(marca, modelo, patente, kilometraje)


# --------------------------------------------------------------------


def elegir_opciones(vehiculo):
    while True:
        print("--------------")
        opcion_usuario = input(
            "Ingresa una opcion a continuacion:\n1. Conducir\n2. Mostrar kilometros recorridos\n3. Mostrar datos del vehiculo\n4. Mostrar Kilometraje total"
        )
        print("--------------")

        match opcion_usuario:
            case "1":
                kilometros = int(
                    int(input("Ingresa la cantidad de km que planeas conducir"))
                )
                vehiculo.conducir(kilometros)
            case "2":
                kilometros_recorridos = vehiculo.mostrar_kilometraje_recorrido()
                print(kilometros_recorridos)
            case "3":
                print(vehiculo)
            case "4":
                km_totales = vehiculo.mostrar_kilometraje_total()
                print(km_totales)


# ---------------------------------------------------------------

if __name__ == "__main__":
    mi_vehiculo = comprar_auto()
    elegir_opciones(mi_vehiculo)
