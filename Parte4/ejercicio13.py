"""

Compra de Productos.

Escribe un programa de consola para gestionar la
compra de productos.

Cada producto se define por :
- id(autoincremental)
- nombre
- caducidad/fecha de vencimiento
- precio que estará sujeto a la fecha de caducidad
como sigue:

- Si le quedan entre 3 y 5 dias, se reduce un 40%
- Si le quedan menos de 3 dias, se reduce un 70%
- No se podran vender productos vencidos


"""

from datetime import datetime

#-----------------------------------------------------------

class Producto:
    __id = 1

    def __init__(self, nombre: str, precio: int, fecha_vencimiento: str):
        self.__id = Producto.__id
        Producto.__id += 1
        self.nombre = nombre
        self.precio = precio
        self.fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%Y-%m-%d").date()

    def calcular_descuento(self, fecha_actual:datetime.date):
        dias_restantes = (self.fecha_vencimiento- fecha_actual).days
        if dias_restantes < 0:
            raise ValueError(
                f"El producto '{self.nombre}' está vencido y no puede ser vendido."
            )
        elif dias_restantes < 3:
            return round(self.precio * 0.30, 2)
        elif dias_restantes <= 5:
            return round(self.precio * 0.60, 2)
        else:
            return round(self.precio, 2)

    def __str__(self):
        return f"El producto: {self.nombre} vence: {self.fecha_vencimiento}"

#-----------------------------------------------------------

def cargar_productos():
    productos = []
    while True:
        nombre = input("Ingresa el nombre del producto")
        precio = int(input("Ingresa el precio del producto"))
        fecha = input("Ingresa la fecha de vencimiento (YYYY-MM-DD):")

        try:
            producto = Producto(nombre, precio, fecha)
            productos.append(producto)
        except ValueError:
            print("Fecha invalida, vuelve a ingresar la fecha")

        continuar = input("Quieres ingresar otro producto? (s/n)").strip().lower()
        if continuar != "s":
            break
    return productos

#-----------------------------------------------------------

def mostrar_precios(productos):
    fecha_actual = datetime.now().date()
    for producto in productos:
        precio_final = producto.calcular_descuento(fecha_actual)
        try:
          print(f"Precio final con descuento ${precio_final}")
        except ValueError as e:
          print(e,"\n")

#-----------------------------------------------------------
          
def main():
    productos = cargar_productos()
    mostrar_precios(productos)

#-----------------------------------------------------------

if __name__ == "__main__":
    main()