"""
Escribe un programa que solicite al usuario el precio y la cantidad
de un producto. Clasifique el producto como caro si el precio es
mayor de $100 o si la cantidad es menor que 10 y el precio es mayor a $50.
De lo contrario clasifiquelo como barato , incluye condiciones para manejar
valores falsos (0 o vacio)


"""

while True:
    precio = float(input("Ingresa el precio del producto"))
    cantidad = int(input("A continuacion ingresa la cantidad"))

    if not precio or not cantidad:
        print("No se permiten valores vacios")
    if precio <= 0 or cantidad <= 0:
        print("Debes ingresar un valor supeior a 0")
        continue
    if precio > 100 or (cantidad < 10 and precio > 50):
        print("El producto es caro")
    else:
      print("El producto es barato")
      break
