class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    def obtener_datos(self):
        return f"Nombre: {self.nombre} Edad:{self.edad}"

    # Ejemplo de uso


if __name__ == "__main__":
    persona = Persona("Juan", 30)
    print(persona.obtener_datos())  # Imprime "Nombre: Juan" y
    "Edad: 30"
    persona.nombre = "Pedro"
    persona.edad = 35
    print(persona.obtener_datos())  # Imprime "Nombre: Pedro" y
    "Edad: 35"
