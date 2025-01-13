'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 13 de enero de 2025
Descripción: Conversiones.
'''


def menu()-> int:
    print("** Suma y Resta **")
    print("1.- Suma")
    print("2.- Resta")
    print("0.- Salir")
    opcion = input("Ingrese una opción: ")
    while not opcion.isnumeric():
        print("Opción no válida")
        opcion = input("Intenta nuevamente: ")
    opcion = int(opcion)
    print()
    return opcion

def suma(numero1, numero2: float)-> float:
    suma = numero1 + numero2
    return suma

def resta(numero1, numero2: float)-> float:
    resta = numero1 - numero2
    return resta


if __name__ == '__main__':
    salir = 1
    while salir != 0:
        opcion = menu()
        if opcion == 1:
            numero1 = input("Ingrese el primer número a sumar: ")
            while not numero1.isnumeric():
                print("Opción no válida")
                numero1 = input("Intenta nuevamente: ")
            numero1 = float(numero1)
            numero2 = input("Ingrese el segundo número a sumar: ")
            while not numero2.isnumeric():
                print("Opción no válida")
                numero2 = input("Intenta nuevamente: ")
            numero2 = float(numero2)
            resultado = suma(numero1, numero2)
            print(f"El resultado de la suma es: {resultado}")
            print()
        elif opcion == 2:
            numero1 = input("Ingrese el primer número a restar: ")
            while not numero1.isnumeric():
                print("Opción no válida")
                numero1 = input("Intenta nuevamente: ")
            numero1 = float(numero1)
            numero2 = input("Ingrese el segundo número a restar: ")
            while not numero2.isnumeric():
                print("Opción no válida")
                numero2 = input("Intenta nuevamente: ")
            numero2 = float(numero2)
            resultado = resta(numero1, numero2)
            print(f"El resultado de la resta es: {resultado}")
            print()
        elif opcion == 0:
            print("Saliendo...")
            salir = 0
        else:
            print("Valor no válido.")
