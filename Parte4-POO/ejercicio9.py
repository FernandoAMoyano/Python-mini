"""

Crea una clase CuentaBancaria con los siguientes atributos
obligatorios: numero de cuenta , nombre y apellido. El saldo
debe comenzar con 100.000. Agrega e implemnta metodos para:

1) depositar(debe aceptar un valor entero y sumarlo al saldo
2) retirar(debe aceptar un valor entero y restarlo al saldo solo si hay dinero
   suficiente para retirar en la cuenta)
3) ver el saldo

Ademas, escribe una aplicacion de consola que permita al usuairo
depositar retirar o ver saldo hasta que decida detenerse.
Al finalizar debera mostrar los datos de la cuenta y el saldo.

"""

# -------------------------------------------------------------------------


class CuentaBancaria:
    saldo = 100000.00

    def __init__(self, numero: int, nombre: str, apellido: str):
        self.numero = numero
        self.nombre = nombre
        self.apellido = apellido

    def depositar(self, monto: int):
        if not isinstance(monto, int) or monto <= 0:
            print("El monto a depositar no es valido")
            return
        self.saldo += monto
        print("Montor depositado satisfactoriamente!")

    def retirar(self, monto: int):
        if not isinstance(int, monto) or monto <= 0:
            print("El monto a retirar no es valido")
        if monto > self.saldo:
            print("No tienes saldo suficiente")
        self.saldo -= monto
        print(f"ustes a retirado {monto} de su cuenta")

    def ver_saldo(self) -> float:
        return self.saldo

    def __str__(self) -> str:
        return f"Cuenta #{self.numero} | Titular: {self.nombre} {self.apellido} | Saldo: ${self.saldo:.2f}"


# -----------------------------------------------------------------------


def mostrar_opciones():
    print("-------#-------")
    print("1. Depositar dinero")
    print("2. Extraer dinero")
    print("3. Ver saldo")
    print("4. Salir")
    print("-------#-------")


# ------------------------------------------------------------------------
def main():
    cuenta_bancaria = CuentaBancaria(13123, "Fernando Moyano", "Moyano")
    while True:
        mostrar_opciones()
        seleccion_usuario: int = int(input("Elige una de las siguientes opciones"))
        match seleccion_usuario:
            case 1:
                monto_a_depositar = int(input("Ingresa el monto a depositar"))
                cuenta_bancaria.depositar(monto_a_depositar)
            case 2:
                monto_a_extraer = int(input("Ingresa el monto que deseas extrer"))
                cuenta_bancaria.retirar(monto_a_extraer)
            case 3:
                saldo_actual = cuenta_bancaria.ver_saldo()
                print(f"Tu saldo actual es : {saldo_actual}")
            case 4:
                print("Gracias por ser parte de nuesta familia! vuelve luego")
                break


# ------------------------------------------------------------------------

if __name__ == "__main__":
    main()
