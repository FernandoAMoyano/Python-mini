"""
Escribe un programa que permita llevar un registro de las
calificaciones de varios estudiantes. El programa debe
permitir:
1_ agregar estudiantes con sus calificaciones
2_ actualizar las calificaciones de un estudiante
    existente.
3_ mostrar el promedio
    de calificaciones de un estudiante especifico.
"""

lista_calificaciones = [
    {"nombre": "Ana", "calificaciones": {"1": 4, "2": 7, "3": 5, "4": 5}},
    {"nombre": "Luis", "calificaciones": {"1": 3, "2": 9, "3": 8, "4": 9}},
]


def actualizarCalificaciones(nombre, nuevasCalificaciones):
    alumno_encontrado = False
    for alumno in lista_calificaciones:
        if alumno["nombre"] == nombre:
            for materia, nuevaNota in nuevasCalificaciones.items():
                alumno["calificaciones"][materia] = nuevaNota
            print(f"Las calificaciones de {nombre} fueron actualizadas")
            alumno_encontrado = True
            break
    if not alumno_encontrado:
        print(f"No se encontro al alumno con nombre{nombre}")


def mostrarCalificaciones():
    for alumno in lista_calificaciones:
        print(f"Alumno: {alumno['nombre']}")
        for materia, nota in alumno["calificaciones"].items():
            print(f"  Materia {materia}: {nota}")


def calcularPromedio(nombre):
    for alumno in lista_calificaciones:
        if alumno["nombre"] == nombre:
            calificaciones = alumno["calificaciones"]
            suma = sum(map(int, calificaciones.values()))
            promedio = suma / len(calificaciones)
            return promedio
    return None


def agregarNuevaCalificacion(nombre, calificaciones):
    nuevo_alumno = {"nombre": nombre, "calificaciones": calificaciones}
    lista_calificaciones.append(nuevo_alumno)
    print(f"Se agregó a {nombre} con sus calificaciones.")


def solicitarCalificaciones():
    calificaciones = {}
    for i in range(1, 6):
        calificacion = input(f"Ingresa la calificacion para la materia {i}")
        calificaciones[i] = int(calificacion)
    return calificaciones


def solicitarNombreAlumno():
    return input("Ingresa el nombre del alumno")


def main():
    while True:
        print("\n--- Menú ---")
        print("1. Agregar estudiante")
        print("2. Actualizar calificaciones")
        print("3. Mostrar calificaciones")
        print("4. Calcular promedio")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = solicitarNombreAlumno()
            calificaciones = solicitarCalificaciones()
            agregarNuevaCalificacion(nombre, calificaciones)

        elif opcion == "2":
            nombre = solicitarNombreAlumno()
            nuevas = solicitarCalificaciones()
            actualizarCalificaciones(nombre, nuevas)

        elif opcion == "3":
            mostrarCalificaciones()

        elif opcion == "4":
            nombre = solicitarNombreAlumno()
            promedio = calcularPromedio(nombre)
            if promedio is not None:
                print(f"El promedio de {nombre} es {promedio:.2f}")
            else:
                print("Alumno no encontrado.")

        elif opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
