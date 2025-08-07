"""

Gestion de biblioteca.

Escribe un programa de consola que simula
la gestion de una biblioteca. Cada libro debe tener:
- titulo,
- autor
- un estado (prestado o disponible).

Crea una clase Libro con los atributos mencionados y metodos para prestar y devolver libros.
Implementa una clase Biblioteca que almacena una lista de libros
y permite buscar libros por titulo o autor, así como mostrar
el estado de un libro especifico.


"""


class Libro:
    def __init__(self, titulo: str, autor: str, estado="disponible"):
        self.titulo = titulo
        self.autor = autor
        self.estado = estado

    def prestar(self):
        if self.estado == "disponible":
            self.estado = "prestado"
            print(f'El libro "{self.titulo}" ha sido prestado.')
        else:
            print(f'El libro "{self.titulo}" ya está prestado.')

    def devolver(self):
        if self.estado == "prestado":
            self.estado = "disponible"
            print(f'El libro "{self.titulo}" ha sido devuelto.')
        else:
            print(f'El libro "{self.titulo}" ya está disponible.')


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro: Libro):
        self.libros.append(libro)
        print(f'Libro "{libro.titulo}" agregado a la biblioteca.')

    def buscar_libros(self, termino):
        resultados = [
            libro for libro in self.libros
            if termino.lower() in libro.titulo.lower() or termino.lower() in libro.autor.lower()
        ]
        return resultados

    def mostrar_estado_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                print(f'Estado del libro "{libro.titulo}": {libro.estado}')
                return
        print("Libro no encontrado.")


def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n===== Gestión de Biblioteca =====")
        print("1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Buscar libro")
        print("5. Mostrar estado de un libro")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            libro = Libro(titulo, autor)
            biblioteca.agregar_libro(libro)

        elif opcion == "2":
            titulo = input("Ingrese el título del libro a prestar: ")
            encontrados = biblioteca.buscar_libros(titulo)
            if encontrados:
                encontrados[0].prestar()
            else:
                print("Libro no encontrado.")

        elif opcion == "3":
            titulo = input("Ingrese el título del libro a devolver: ")
            encontrados = biblioteca.buscar_libros(titulo)
            if encontrados:
                encontrados[0].devolver()
            else:
                print("Libro no encontrado.")

        elif opcion == "4":
            termino = input("Ingrese título o autor para buscar: ")
            resultados = biblioteca.buscar_libros(termino)
            if resultados:
                print("Resultados de la búsqueda:")
                for libro in resultados:
                    print(f'- "{libro.titulo}" de {libro.autor} ({libro.estado})')
            else:
                print("No se encontraron libros.")

        elif opcion == "5":
            titulo = input("Ingrese el título del libro: ")
            biblioteca.mostrar_estado_libro(titulo)

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


# Ejecutar la aplicación
if __name__ == "__main__":
    menu()
