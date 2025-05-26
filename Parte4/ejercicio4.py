"""
En base a lo mencionado anteriormente, intenta crear una jerarquia
de asociacion en python que ilustre el ejemplo de Productos,
Categoria, y Proveedor.
"""


class Product:

    def __init__(self, nombre, precio, proveedor):
        self.__nombre = nombre
        self.__precio = precio
        self.__proveedor = proveedor

    def __str__(self):
        return f"Nombre: {self.__nombre} Precio: {self.__precio} Proveedor: {self.__proveedor}"


class Categoria:

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__productos = []

    def agregar_producto(self, producto):
        self.__productos.append(producto)

    def mostrar_productos(self):
        for p in self.__productos:
            print(p)

    def __str__(self):
        return f"Categoria : {self.__nombre}"


class Proveedor:

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__listado_de_productos = []

    def agregar_producto(self, producto):
        self.__listado_de_productos.append(producto)
        producto.proveedor = self

    def mostrar_productos(self):
        for item in self.__listado_de_productos:
            print(item)

    def __str__(self):
        return f"Proveedor: {self.__nombre}"


proveedor1 = Proveedor("La Serenisima")
producto1 = Product("Leche", 3000, proveedor1)
print(producto1)

categoria1=Categoria("Lacteos")
categoria1.agregar_producto(producto1)
categoria1.mostrar_productos()