class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def obtener_datos(self):
        return f"Nombre{self.get_nombre()} Edad: {self.get_edad()}"


if __name__ == "__main__":
    persona = Persona("Juan", 30)
    print(persona.obtener_datos())  # Imprime "Nombre:Juan" y "Edad:30"
    persona.set_nombre("Pedro")
    print(persona.get_nombre())  # Imprime "Nombre:Pedro y Edad:35"
