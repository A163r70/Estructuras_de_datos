def menu_gato()->int:

    print("1.- 1 vs 1.")
    print("2.- Usuario vs CPU.")
    print("0.- Salir.")
    opcion = input("Escoja una opción: ")
    while not opcion.isnumeric():
        print("Opción no válida")
        opcion = input("Intenta nuevamente: ")
    opcion = int(opcion)
    print()
    return opcion

if __name__ == '__main__':
    menu_gato()
