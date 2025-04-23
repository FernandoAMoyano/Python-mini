"""
Escriba un programa que pida al usuario un entero de
tres digitos y entregue el numero con los digitos en
orden inverso.

"""

while True:
    numero = input("Ingresa un numero de 3 digitos")
    try:
        if numero.isdigit():
            if len(numero) == 3:
                a = numero[0]
                b = numero[1]
                c = numero[2]
                print("Numero invertido: " + c + b + a)
                break
            print("El numero debe tener 3 digitos")
        print("El valor ingresado debe ser un numero")
    except:
        print("El numero no es valido")
