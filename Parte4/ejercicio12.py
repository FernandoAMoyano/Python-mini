"""
Expocoches.

Escribe un programa de consola para gestionar la venta
de entradas(no numeradas) de Expocoches que tiene 3 zonas:
1_ La sala principal con 1000 entradas disponibles,
2_ La zona de compra-venta con 200 entradas disponibles.
3_ La zona vip con 25 entradas disponibles.

Hay que contralar que existen entradas anted de venderlas.

Define la clase Zona con sus atributos y metodos correspondientes
y crea un programa de consola que permita vender las entradas.

"""

from enum import Enum

# -------------------------------------------------


class tipoZona(Enum):
    SALA_PRINCIPAL = "Sala principal"
    COMPRA_VENTA = "Compra-venta"
    VIP = "Vip"


class entradasPorZona(Enum):
    SALA_PRINCIPAL = 1000
    COMPRA_VENTA = 200
    VIP = 25


# -------------------------------------------------


class Zona:
    def __init__(self, tipo: tipoZona, entradas_disponibles: entradasPorZona):
        self.tipo = tipo
        self.entradas_disponibles = entradas_disponibles

    def vender(self, cantidad: int):
        if isinstance(cantidad, int) and cantidad > 0:
            if cantidad > self.entradas_disponibles:
                print("No hay entradas suficientes")
                print(f"Entradas disponibles: {self.entradas_disponibles}")
            else:
                self.entradas_disponibles -= cantidad
        else:
            print("Ingresa un valor valido")

    def mostrar_entradas_disponibles(self):
        print(f"Entradas disponibles: {self.entradas_disponibles}")


# -------------------------------------------------


def mostrar_zonas_disponibles():
    return input(
        "\n Selecciona la zona\n"
        "1. Sala principal\n"
        "2. Compra-venta\n"
        "3. Vip\n"
        ">> "
    )


# -------------------------------------------------


def mostrar_acciones_posibles():
    return input(
        "\n Ingresa una opcion a continuacion\n"
        "1. Comprar entradas\n"
        "2. Mostrar entradas disponibles\n"
        "3. Volver al menú de zonas\n"
        "4. Salir\n"
        ">> "
    )


# -------------------------------------------------

if __name__ == "__main__":

    zonas = {
        "1": Zona(tipoZona.SALA_PRINCIPAL.value, entradasPorZona.SALA_PRINCIPAL.value),
        "2": Zona(tipoZona.COMPRA_VENTA.value, entradasPorZona.COMPRA_VENTA.value),
        "3": Zona(tipoZona.VIP.value, entradasPorZona.VIP.value),
    }

    while True:
        seleccion_zona = mostrar_zonas_disponibles()
        zona = zonas.get(seleccion_zona)
        while True:
            accion = mostrar_acciones_posibles()
            match accion:
                # Comprar entradas
                case "1":
                    try:
                        cantidad_entradas = int(
                            input("Selecciona la cantidad de entradas a comprar")
                        )
                        zona.vender(cantidad_entradas)
                    except ValueError:
                        print("Ingresa un número válido.")
                # Mostrar entradas disponible
                case "2":
                    zona.mostrar_entradas_disponibles()
                # Volver al Menu de zonas
                case "3":
                    print("Menu de zonas")
                    break
                # Salir del sistema
                case "4":
                    print("Nos vemos pronto!!")
                    exit()
                case _:
                    print("Ingresa una opcion valida")
