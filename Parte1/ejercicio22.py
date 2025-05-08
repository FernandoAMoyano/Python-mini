"""
Escribe un programa que administre el inventario de una
tienda , el programa debe permitir:
1_ agregar nuevos productos
2_ actualizar las cantidades de los productos existentes
3_ mostrar el inventario actual

"""

lista_productos = [
    {"id": 1, "nombre": "Mouse", "precio": 25, "cantidad" "stock": 30},
    {"id": 2, "nombre": "Teclado", "precio": 45, "stock": 20},
]

producto1 = {"nombre": "Laptop", "precio": 1200, "stock": 5}


def agregar_producto(nuevoProducto):
    lista_productos.append(nuevoProducto)


def actualizar_producto(id, nuevasCaracteristicas):
    for i in range(len(lista_productos)):
        if lista_productos[i]["id"] == id:
            if "nombre" in nuevasCaracteristicas:
                lista_productos[i]["nombre"] = nuevasCaracteristicas["nombre"]
            if "precio" in nuevasCaracteristicas:
                lista_productos[i]["precio"] = nuevasCaracteristicas["precio"]
            if "cantidad" in nuevasCaracteristicas:
                lista_productos[i]["cantidad"] = nuevasCaracteristicas["cantidad"]
            if "stock" in nuevasCaracteristicas:
                lista_productos[i]["stock"] = nuevasCaracteristicas["stock"]
            print(f"Producto con ID {id} actualizado parcialmente.")
            return
        print(f"No se encontro el producto con ID{id}")


def mostrar_productos():
    mensaje = "Productos en el carrito: \n"
    for producto in lista_productos:
        mensaje += f"{producto["nombre"]} ${producto["precio"]}\n"
    print(mensaje)


mostrar_productos()
actualizar_producto(1, {"nombre": "Leche", "precio": 43, "stock": 54})
mostrar_productos()
agregar_producto(producto1)
mostrar_productos()
