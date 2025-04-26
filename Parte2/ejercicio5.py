def es_bisiesto(año):
    """
    Determina si un año es bisiesto según las reglas históricas.
    - Calendario Juliano (antes de 1582): años divisibles por 4 son bisiestos
    - Calendario Gregoriano (desde 1582): años divisibles por 4 son bisiestos,
      excepto los divisibles por 100 que no sean divisibles por 400
    """
    # Determinar el calendario vigente
    if año < 1582:
        # Calendario Juliano: bisiesto si es divisible por 4
        return año % 4 == 0
    else:
        # Calendario Gregoriano
        if año % 400 == 0:
            return True
        elif año % 100 == 0:
            return False
        else:
            return año % 4 == 0

# Solicitar el año al usuario
try:
    año = int(input("Ingrese un año: "))
    
    if es_bisiesto(año):
        print(f"{año} es un año bisiesto.")
    else:
        print(f"{año} no es un año bisiesto.")
except ValueError:
    print("Error: Por favor ingrese un año válido (número entero).")