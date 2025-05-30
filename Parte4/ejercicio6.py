"""
Crear una clase llamada Persona. Sus atributos son: nombre, edad
y DNI. Construye los siguientes metodos para la clase:

a) Un constructor donde los datos pueden estar vacioss
b) Los setters y getters para cada uno de los atributos.Hay que
   validar las entradas de datos.
c) mostrar(): Muestra los datos de la persona
d) es_mayor_de_edad(): Devuelve un valor lógico indicando si es
   mayor de edad

Ademas crea una aplicacion de consola que pernita al ausuario
crear un objeto Persona y evaluar si es mayor de edad.
"""


class Persona:

    def __init__(self, nombre: str = "", edad: int = 0, dni: str = 0):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        if not nombre.isalpha() and nombre != "":
            raise ValueError("El nombre solo debe tener letras")
        self.__nombre = nombre

    @property
    def edad(self) -> int:
        return self.__edad

    @edad.setter
    def edad(self, edad: int):
        if not isinstance(edad, int) or edad < 1:
            raise ValueError("La edad debe ser un numero entero positivo")
        self.__edad = edad

    @property
    def dni(self) -> str:
        return self.__dni

    @dni.setter
    def dni(self, dni: str):
        if dni and (not dni.isdigit() or len(dni) != 8):
            raise ValueError("El DNI debe tener 8 dígitos numéricos.")
        self.__dni = dni
    
    def mostrar_datos(self) -> str:
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}, Dni: {self.__dni}"

    def es_mayor_edad(self) -> bool:
        return self.__edad >= 18


if __name__ == "__main__":
    persona1 = Persona("Fernando", 33, 3423423)
    print(persona1.edad)

    print(persona1.mostrar_datos())
    print(persona1.es_mayor_edad())
