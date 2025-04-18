"""
Escribe un programa que solicite al usuario que ingrese
una contraseña y confirme la contraseña. El programa
debe verificar si ambas contraseñas coinciden y no están vacias

"""

intentos = 3


while intentos > 0:
    password = input("A continuación ingresa la contraseña")
    confirm_password = input("A continuacion confirma la contraseña")

    if password and confirm_password:
        if password == confirm_password:
            print("Bienvenido a la aplicacion!!!")
            break
        else:
            print("Las contraseñas no coinciden")
            intentos -= 1
            if intentos > 0:
                print(f"Te quedan {intentos} intentos por realizar.")
            else:
                print("Te bloqueamos la cuenta por prevención.")
    else:
        print(f"debes ingresar un valor para las contraseñas")
