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
    if opcion == 1:
        print(f"Usted tiene ${(dinero):.2f} en su cuenta.")
    elif opcion == 2:
        dinero += float(input("¿Cuánto dinero desea depositar en su cuenta?: "))
    elif opcion == 3:
        retiro = float(input("¿Cuánto desea retirar?: "))
        if retiro > dinero:
            print("Fondos insuficientes.")
        else:
            dinero -= retiro
    elif opcion == 0:
        opcion = 0
    else:
        print("Opción no válida.")