"""
Producto. Crea una clase Producto con los siguientes atributos: nombre, precio
y stock siendo obligatorios solo los atributos nombre y precio. El stock
debe comenzar con 0. Define metodos para actualizar el stock para calcular
el total del inventario y para ver los datos. Además escribe una aplicacion
de consola que permita al usuario:

1)actualizar el stock
2)Calcular el inventario hasta que decida detenerse

Al finalizar debera mostrar los datos del producto, stock e
inventario final.

"""

from typing import List


class Producto:
    def __init__(self, nombre: str, precio: int, stock: int = 0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad: int):
        if cantidad >= 0:
            self.stock = cantidad
        else:
            print("La cantidad no puede ser un valor negativo")

    def calcular_total_inventario(self) -> float:
        return self.precio * self.stock

    def __str__(self):
        return f"Nombre: {self.nombre} Precio: ${self.precio:.2f} Stock:{self.stock}"


def main():
    productos: List = []

    while True:
        print("\n--- Menú de opciones ---")
        print("1. Crear producto")
        print("2. Actualizar stock")
        print("3. Calcular inventario total")
        print("4. Ver productos")
        print("5. Salir")

        opcion_usuario = int(input("Elige una opcion"))

        match (opcion_usuario):
            case 1:
                nombre = input("Ingresa el nombre del producto")
                precio = int(input("Ingresa el precio del producto"))
                producto1 = Producto(nombre, precio)
                productos.append(producto1)
            case 2:
                for i, p in enumerate(productos):
                    print(f"{i+1}. {p.nombre}")
                try:
                    indice = (
                        int(input("Ingresa el numero del producto a actualizar")) - 1
                    )
                    nuevo_stock = int(input("Ingresa el stock"))
                    productos[indice].actualizar_stock(nuevo_stock)
                except:
                    print("seleccion invalida")
            case 3:
                total = sum(p.calcular_total_inventario() for p in productos)
                print(f"Total: ${total}")
            case 4:
              for p in productos:
                print(p)
            case 5:
              print("vuelve pronto!!")
              break
            
            
if __name__=="__main__":
  main()