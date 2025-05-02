"""
Este problema aparecio en el certamen recuperativo
1 del segundo semestre de 2011 en el campus Vitacura

Una maquina de alimentos tiene productos de tres tipos
A,B,C, que valen respectivamente $270. $340 y $390
La maquina acepta y da de vuelto monedas de $10, $50 y $100

Escriba un programa que pida al usuario elegir el producto
y luego le pida ingresar las monedas hasta alcanzar el
monto a pagar. Si el monto ingresado es mayor que el
precio del producto,el programa debe entregar las monedas
de vuelto, una por una.

"""

monto_pagado = 0
precio_a_pagar = 0
moneda_de_vuelto = ""
lista_monedas_vuelto = []

vuelto = 0

producto_seleccionado = input("Ingresa el producto que quieres comprar")
if producto_seleccionado == "A":
    precio_a_pagar = 270
elif producto_seleccionado == "B":
    precio_a_pagar = 340
else:
    precio_a_pagar = 390
print(f"Eligiste el producto {producto_seleccionado} precio: {precio_a_pagar}")


monto_pagado = int(input("Ingresa una moneda para pagar (10 - 50 - 100)"))

while monto_pagado < precio_a_pagar:            
    precio_a_pagar = precio_a_pagar - monto_pagado
    print(f"te quedan por pagar {precio_a_pagar}")
    monto_pagado = int(input("Ingresa una moneda para pagar (10 - 50 - 100)"))

vuelto = monto_pagado - precio_a_pagar
      
while vuelto > 0:
           
    if vuelto >= 100:
        vuelto = vuelto - 100
       
        lista_monedas_vuelto.append(100)

    elif vuelto >= 50:
        vuelto = vuelto - 50
        
        lista_monedas_vuelto.append(50)

    else:
        vuelto >= 10
        vuelto = vuelto - 10
     
        lista_monedas_vuelto.append(10)
                
print(f"Te entregamos las siguientes monedas como vuelto{lista_monedas_vuelto}")
print(f"Ya puedes retirar el producto {producto_seleccionado}")
