"""
Registro de estudiantes.

Escribe un programa que permita registrar estudiantes en un arreglo/lista
cada estudiante debe tener:
- nombre
- edad
- lista de asignaturas en las que esta inscrito.

Implementa una clase Estudiante
con los atributos mencionados y metodos para agregar asignaturas, mostrar
la informacion del estudiante y calcular su promedio de calificaciones.


"""

from typing import Dict


class Estudiante:

    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad
        self.asignaturas = []

    def agregar_asignatura(self, nombre: str, calificaciones: list[int] = None) -> None:
        if calificaciones is None:
            calificaciones = []
            
        if not nombre:
            print("El nombre no puede estar vacío")
        elif nombre.isnumeric():
            print("La asignatura no puede contener solo números")
        else:
            self.asignaturas.append(
                {"nombre": nombre, "calificaciones": calificaciones}
            )
            print(f"Asignatura '{nombre}' agregada exitosamente")

    def __str__(self):
        return f"Estudiante: {self.nombre}, Edad: {self.edad}"

    def calcular_promedio(self, nombre_asignatura: str) -> str:
        for asignatura in self.asignaturas:
            if asignatura["nombre"] == nombre_asignatura:
                if len(asignatura["calificaciones"]) == 0:
                    return "Aún no tienes calificaciones para esta asignatura"
                else:
                    suma_total_notas = sum(asignatura["calificaciones"])
                    promedio = suma_total_notas / len(asignatura["calificaciones"])
                    return f"El promedio de {nombre_asignatura} es: {promedio:.2f}"
        return "Asignatura no encontrada"


def mostrar_menu():
    return input(
        "\nIngresa una opción a continuación:\n"
        "1. Agregar asignatura\n"
        "2. Calcular promedio\n"
        "3. Mostrar información del estudiante\n"
        "4. Salir\n"
        ">> "
    )


if __name__ == "__main__":
    nombre_estudiante = input("Ingresa el nombre del estudiante: ")
    edad_estudiante = int(input("Ingresa la edad del estudiante: "))
    
    estudiante = Estudiante(nombre_estudiante, edad_estudiante)
    
    # Agregar asignaturas iniciales (opcional)
    print("\n¿Quieres agregar asignaturas iniciales?")
    while True:
        continuar = input("¿Agregar asignatura? (s/n): ")
        if continuar.lower() != "s":
            break
        asignatura = input("Ingresa el nombre de la asignatura: ")
        estudiante.agregar_asignatura(asignatura)
    
    # Menú principal
    while True:
        seleccion_usuario = mostrar_menu()
        match seleccion_usuario:
            case "1":
                nombre = input("Ingresa el nombre de la asignatura: ")
                
                # Carga de calificaciones
                calificaciones = []
                print("Ingresa las calificaciones para esta asignatura:")
                while True:
                    try:
                        nota = int(input("Ingresa una calificación: "))
                        calificaciones.append(nota)
                        continuar = input("¿Quieres agregar otra calificación? (s/n): ")
                        if continuar.lower() != "s":
                            break
                    except ValueError:
                        print("Por favor, ingresa un número válido")
                
                estudiante.agregar_asignatura(nombre, calificaciones)
                
            case "2":
                if not estudiante.asignaturas:
                    print("No hay asignaturas registradas")
                    continue
                    
                print("Asignaturas disponibles:")
                for i, asig in enumerate(estudiante.asignaturas, 1):
                    print(f"{i}. {asig['nombre']}")
                
                nombre_asignatura = input("Ingresa el nombre de la asignatura para calcular el promedio: ")
                promedio = estudiante.calcular_promedio(nombre_asignatura)
                print(promedio)
                
            case "3":
                print(f"\n{estudiante}")
                if estudiante.asignaturas:
                    print("Asignaturas:")
                    for asig in estudiante.asignaturas:
                        print(f"  - {asig['nombre']}: {asig['calificaciones']}")
                else:
                    print("No tiene asignaturas registradas")
                    
            case "4":
                print("¡Hasta luego!")
                break
                
            case _:
                print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")