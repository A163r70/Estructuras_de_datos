'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 21 de noviembre de 2024
Descripción: Ejercicio uno de una calculadora con funciones.
'''

def menu():
    print("0) Salir")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicación")
    print("4) División")
    print("5) División entera")
    print("6) Exponenciación")
    opcion = int(input("Escoga una opción: "))
    return opcion

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

contador = 1
while contador != 0:
    opcion = menu()
    if opcion == 1 or opcion==2 or opcion==3 or opcion==4 or opcion==5 or opcion==6:
        numero1 = float(input("Ingrese un número: "))
        numero2 = float(input("Ingrese otro número: "))
        resultado = calculadora(opcion, numero1, numero2)
        print(f"El resultado de la operación es: {(resultado):.3f}")
    elif opcion == 0:
        contador = 0
    else:
        print("Valor no válido.")
