'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 29 de Octubre de 2024
Descripción:
'''

print("** bienvenido al Banco Azteca **")
dinero = 0.00
opcion = 1
while opcion != 0:
    print("0.- Salir")
    print("1.- Consultar Saldo")
    print("2.- Ingresar dinero")
    print("3.- Retirar dinero")
    opcion = int(input("Elige una opción: "))
    print()
    if opcion == 1:
        print(f"Usted tiene ${(dinero):.2f} en su cuenta.")
        print()
    elif opcion == 2:
        dinero += float(input("¿Cuánto dinero desea depositar en su cuenta?: "))
        print()
    elif opcion == 3:
        retiro = float(input("¿Cuánto desea retirar?: "))
        if retiro > dinero:
            print("Fondos insuficientes.")
            print()
        else:
            dinero -= retiro
            print(f"Su nuevo saldo es de: ${(dinero):.2f}")
        print()
    elif opcion == 0:
        opcion = 0
    else:
        print("Opción no válida.")
        print()

"""
En este programa hacemos un ejemplo de una cuenta de Banco Azteca. Primero le mostramos al usuario un pequeño menú donde puede consultar su saldo, depositar
o retirar dinero de su cuenta, después de que elija una opción la ejecutamos en el While, en u inicio el usuario no tiene nada en su cuenta, por lo que
tiene que depósitar, y hacer movimientos a partir de ahí, también le incluí el caso cuando quiere retirar más de lo que tiene en su cuneta. La función de paro 
es la misma que he usado en los otros códigos.
"""