'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 29 de Octubre de 2024
Descripción: Calculadora básica.
'''


print("** Calculadora básica **")
opcion = 1
while opcion != 0:
    print("0) Salir")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicación")
    print("4) División")
    print("5) División entera")
    print("6) Exponenciación")
    opcion = int(input("Ingrese una opción para realizar con los número ingresados: "))
    if opcion ==1:
        numero_1 = float(input("Ingrese un número: "))
        numero_2 = float(input("Ingrese otro número: "))
        print(f"La suma del {numero_1} con el {numero_2} es igual a: {(numero_1+numero_2):.2f}")
    elif opcion ==2:
        numero_1 = float(input("Ingrese un número: "))
        numero_2 = float(input("Ingrese otro número: "))
        print(f"La resta del {numero_1} con el {numero_2} es igual a: {(numero_1-numero_2):.2f}")
    elif opcion == 3:
        numero_1 = float(input("Ingrese un número: "))
        numero_2 = float(input("Ingrese otro número: "))
        print(f"La multiplicación del {numero_1} con el {numero_2} es igual a: {(numero_1*numero_2):.2f}")
    elif opcion == 4:
        numero_1 = float(input("Ingrese un número: "))
        numero_2 = float(input("Ingrese otro número: "))
        print(f"La división del {numero_1} con el {numero_2} es igual a: {(numero_1/numero_2):.2f}")
    elif opcion == 5:
        numero_1 = float(input("Ingrese un número: "))
        numero_2 = float(input("Ingrese otro número: "))
        print(f"La división entera del {numero_1} con el {numero_2} es igual a: {(numero_1//numero_2):.2f}")
    elif opcion == 6:
        numero_1 = float(input("Ingrese un número: "))
        numero_2 = float(input("Ingrese otro número: "))
        print(f"El número {numero_1} elevado la {numero_2} es igual a: {(numero_1**numero_2):.2f}")
    elif opcion == 0:
        opcion = 0
    else:
        print("Opción no válida.")