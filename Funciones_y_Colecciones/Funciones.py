'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 11 de noviembre de 2024
Descripción: Funciones.
'''

def menu():
    print("0) Salir")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicación")
    print("4) División")
    print("5) División entera")
    print("6) Exponenciación")

def calculadora(opcion, numero1, numero2):
    if opcion == 1:
        resultado = numero1 + numero2
    elif opcion == 2:
        resultado = numero1 - numero2
    elif opcion == 3:
        resultado = numero1 * numero2
    elif opcion == 4:
        resultado = numero1 / numero2
    elif opcion == 5:
        resultado = numero1 // numero2
    elif opcion == 6:
        resultado = numero1 ** numero2
    return resultado

def hola(nombre):
    print(f"Hola {nombre}")

nombre = input("Ingresa tu nombre: ")
menu()
opcion = int(input("Escoga una opción: "))
numero1 = float(input("Ingrese un número: "))
numero2 = float(input("Ingrese otro número: "))
resultado = calculadora(opcion, numero1, numero2)
print(f"El resultado de la operación es: {(resultado):.3f}")
hola(nombre)
print("Adiós.")
