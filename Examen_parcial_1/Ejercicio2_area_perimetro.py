'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 31 de Octubre de 2024
Descripción: Ejercico 2 del examen parcial.
Este programa determina el área y el perímetro de un rectángulo o de un círculo.
Muestre el siguiente menú:

1) Calcular el área de un rectángulo.
2) Calcular el perímetro de un rectángulo.
3) Calcular el área de un círculo.
4) Calcular el perímetro de un círculo.
0) Salir.
Cualquier otro caso -> Mostrar un mensaje de "opción no válida".
'''
print("** Programa que calcula el área y el perímetro **")
opciones = 1#declaramos una variable donde guardaré las opciones del usuario.
Pi = 3.1416#Declaro una constante llamada "Pi", que ocuparé más adelante.
while opciones != 0:#Iniciamos el while con la condición de ejecutarse mientras sea menor o igual al número que el usuario ingrese.
    print("1) Calcular el área de un rectángulo.")#Mostramos un menú, y el usuario elegirá una opción.
    print("2) Calcular el perímetro de un rectángulo.")
    print("3) Calcular el área de un círculo.")
    print("4) Calcular el perímetro de un círculo.")
    print("0) Salir.")
    opciones = int(input("Ingrese una opción: "))#Guardamos la opción del ususario en la variable "opciones".
    if opciones == 1:#Si elige la opción 1, calcularemos el área del rectángulo.
        base = float(input("Ingrese la base: "))#Pedimos la base del rectángulo.
        altura = float(input("Ingrese la altura: "))#Pedimos la altura del rectángulo.
        print(f"\nEl área es de: {(base * altura):.3f}")#Cálculamos el área con la fórmula b*h, y mostramos en pantalla.
        print("---------------------------------------\n")
    elif opciones == 2:#Si elige la opción 2, calculamos el perímetro del rectángulo.
        base = float(input("Ingrese la base: "))#
        altura = float(input("Ingrese la altura: "))
        print(f"\nEl perímetro es de: {(2 * (base + altura)):.3f}")#Calculamos el perímetro con la fórmula: P=2*(b+h)
        print("---------------------------------------\n")
    elif opciones ==3:#Si elige la opción 3, calcularemos el área de un circulo.
        radio = float(input("Ingrese la el radio: "))#Le pedimos al ususario el radio del circulo.
        print(f"\nEl área es de: {(Pi * (radio**2)):.3f}")#Calculamos su área con la fórmula: π × r^2, y mostramos.
        print("---------------------------------------\n")
    elif opciones == 4:#Si elige la opción 4, calcularemos el perímetro de un circulo.
        radio = float(input("Ingrese la el radio: "))#Le pedimos al ususario el radio del circulo.
        print(f"\nEl perímetro es de: {(2 * Pi * radio):.3f}")#Clculamos el perímetro con la fórmula: 2 × π × r.
        print("---------------------------------------\n")
    elif opciones == 0:#Si elige la opción 0, salimos del programa.
        opciones = 0
        print("\nSaliendo...")
    else:#Si elige una opción ajena al menú, mostramos un mensaje de error.
        print("\nOpción no válida.")
        print("---------------------------------------\n")

""""

"""