"""
Teniendo en cuenta la programacion modular intenta resolver
Escribe un programa para llevar la gestion de usuarios de una
aplicacion. La misma debe permitir:
- Registrar usuarios
- Eliminar usuarios
- Buscar Usuario

Para ello:

- Define un modulo para manejar las operaciones relacionadas
  con los usuarios.
- Define otro modulo para el programa principal que presente
  un menu para seleccionar la operacion y manejar las entradas del usuario
- Utiliza Modulos.
"""

import GestionUsuarios
import Inicio
if __name__ == "__main__":

    lista_usuarios = []


while True:
     opcion_seleccionada=Inicio.iniciar_aplicacion()
     match opcion_seleccionada:
          case 1:
              GestionUsuarios.mostrar_usuarios(lista_usuarios)
          case 2:
              usuario_a_registrar = input(
                  "a continuacion ingresa el nombre del usuario que deseas registrar"
              )
              usuario_registrado = GestionUsuarios.registrar_usuario(lista_usuarios, usuario_a_registrar)
              print(usuario_registrado)
          case 3:
              usuario_a_eliminar = input(
                  "a continuacion ingresa el nombre del usuario que deseas eliminar"
              )
              usuario_eliminado = GestionUsuarios.eliminar_usuario(
                  lista_usuarios, usuario_a_eliminar
              )
              print(usuario_eliminado)
          case 4:
              usuario_a_buscar = input(
                  "a continuacion ingresa el nombre del usuario que deseas buscar"
              )
              usuario_encontrado = GestionUsuarios.buscar_usuario(usuario_a_buscar)
              print(usuario_encontrado)
          case 5:
            print("Te esperamos pronto!!")
            break
