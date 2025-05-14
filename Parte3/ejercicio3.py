"""
1 - Crear una funcion para caluclar el area de un triangulo.Si no se
    proporciona la altura asumimos que la altura es 1.

2 - Crea una funcion para saludar con un mensaje personalizado. Si no se
    proporciona el nombre asumimos "invitado".

3 - Crea una funcion para proporcionar un porcentaje de descuento.
    si no se proporciona el porcentaje, asumimos 10%.
"""



""" 1 """
def calcular_area(base, altura=1):
    """Calcula el área de un triángulo con base y altura dadas."""
    return base * altura / 2


try:
    base = float(input("Ingresa la base del triángulo: "))
    altura_input = input("Ingresa la altura del triángulo (deja vacío para usar 1): ")
    if altura_input.strip() == "":
        area_triangulo = calcular_area(base)
    else:
        altura = float(altura_input)
        area_triangulo = calcular_area(base, altura)
    print(f"El área del triángulo es {area_triangulo}")
except ValueError:
    print("Por favor, ingresa valores numéricos válidos para base y altura.")


""" 2 """
def saludar(nombre="invitado"):
    print(f"Hola como estás {nombre}")


nombre = input("Ingresa tu nombre").strip()

try:
    if nombre == "":
        saludar()
    else:
        saludar(nombre)
except:
    print("Ingresa un valor valido")


""" 3 """
def calcular_descuento(precio, porcentaje=10):
    return precio - precio * porcentaje / 100


precio_producto = int(input("Ingresa el precio del producto"))
porcentaje_descuento = input("Ingresa el porcentaje de descuento")

if porcentaje_descuento.strip() == "":
    precio_con_descuento = calcular_descuento(precio_producto)
else:
    precio_con_descuento = calcular_descuento(
        precio_producto, int(porcentaje_descuento)
    )

print(f"El nuevo precio es de ${precio_con_descuento}")
