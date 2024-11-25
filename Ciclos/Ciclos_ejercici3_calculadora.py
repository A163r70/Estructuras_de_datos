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
    opcion = int(input("Ingrese una opción: "))
    print()
    if opcion ==1:
        numero_1 = float(input("Ingrese un número: "))
        numero_2 = float(input("Ingrese otro número: "))
        print(f"La suma del {numero_1} con el {numero_2} es igual a: {(numero_1+numero_2):.2f}")
        print()
    elif opcion ==2:
        numero_1 = float(input("Ingrese un número: "))
        numero_2 = float(input("Ingrese otro número: "))
        print(f"La resta del {numero_1} con el {numero_2} es igual a: {(numero_1-numero_2):.2f}")
        print()
    elif opcion == 3:
        numero_1 = float(input("Ingrese un número: "))
        numero_2 = float(input("Ingrese otro número: "))
        print(f"La multiplicación del {numero_1} con el {numero_2} es igual a: {(numero_1*numero_2):.2f}")
        print()
    elif opcion == 4:
        numero_1 = float(input("Ingrese un número: "))
        numero_2 = float(input("Ingrese otro número: "))
        print(f"La división del {numero_1} con el {numero_2} es igual a: {(numero_1/numero_2):.2f}")
        print()
    elif opcion == 5:
        numero_1 = float(input("Ingrese un número: "))
        numero_2 = float(input("Ingrese otro número: "))
        print(f"La división entera del {numero_1} con el {numero_2} es igual a: {(numero_1//numero_2):.2f}")
        print()
    elif opcion == 6:
        numero_1 = float(input("Ingrese un número: "))
        numero_2 = float(input("Ingrese otro número: "))
        print(f"El número {numero_1} elevado la {numero_2} es igual a: {(numero_1**numero_2):.2f}")
        print()
    elif opcion == 0:
        opcion = 0
    else:
        print("Opción no válida.")
        print()

"""
En este programa realizamos diferentes cálculos, primero mostramos un menú, donde el usuario elige que desea realizar, después de que eliga una opción del
menú se le pide que ingrese dos números con los que se realizaran las operaciones, en este caso los guardo como tipos float, por si el ususario ingresa decimales
y no enteros, una vez ingresados los números dependiendo de la opción elegida, se realizan los cálculos adecuados, mostrando finalmente el resultado de las operaciones.
La función de paro en el While se determina cuando la variable opción que tenía el valor de 1, lo cambiamos a 0.
"""