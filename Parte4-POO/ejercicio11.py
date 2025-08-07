"""
Control de Volumen.

Crea una clase ControlVolumen que permita establecer
el volumen de un parlante (1 minimo volumen, 10 maximo volumen)
El constructor establecera el volumen en un nivel medio.Agrega metodos para:

1_ Ajustar el volumen permitiendo que el mismo sume o reste sin
   salirse de los limites
2_ Mostrar el nivel de volumen actual.
3_ Escriba una aplicación de consola que permita al usuario manipular
   y consultar el volumen hasta que decida salir.
4_ Al finalizar debera mostrar el nivel actual de volumen.
"""


class Volumen:
    def __init__(self, volumen: int = 5):
        self.__volumen = volumen

    def cambiar_volumen(self, nuevo_volumen: int) -> None:
        if isinstance(nuevo_volumen, int):
            if 1 <= nuevo_volumen <= 10:
                self.__volumen = nuevo_volumen
                print(f"volumen actualizado {self.__volumen}")
            else:
                print("El volumen debe estár entre 1 y 10")
        else:
            print("Ingresa un valor valido para le volumen")

    def mostrar_volumen_actual(self) -> int:
        return self.__volumen


def mostrar_menu_usuario():
    return input(
        "\n Ingresa una opcion a continuación:\n"
        "1. Cambiar Volumen\n"
        "2. Ver volumen actual\n"
        "3. Salir\n"
        ">> "
    )


if __name__ == "__main__":

    try:
        volumen_inicial = input("Ingresa el volumen inicial (1-10), o presiona Enter para usar el valor por defecto (5): ")
        volumen = Volumen(int(volumen_inicial)) if volumen_inicial.strip() else Volumen()
    except ValueError:
        print("Valor inválido, se usará el volumen por defecto.")
        volumen = Volumen()
        

while True:
    eleccion_usuario = mostrar_menu_usuario()
    match eleccion_usuario:
        case "1":
            try:
                nuevo_volumen = int(
                    input("Ingresa un nuevo volumen para tu dispositivo")
                )
                volumen.cambiar_volumen(nuevo_volumen)
            except:
                print(" Ingresa un número válido.")

        case "2":

            print(f" Volumen actual: {volumen.mostrar_volumen_actual()}")

        case "3":
            print("Adios!!")
            break
