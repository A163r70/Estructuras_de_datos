'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 06 de diciembre de 2024
Descripción: Primer ejercicio del examen del segundo parcial. En este programa mostramos en pantalla una escalera con
el número de escalones que el usuario ingrese, ya sean positivos o negativos. Si el número ingresado es positivo
la escalera se mostrará de forma ascendente, y si el número es negativo la escalera se mostrará en forma
descendente.
'''

def menu():
    print("*** Ejercicio 1. La escalera. ***")
    escalones = int(input("Ingresa el número de escalones (positivo - ascendente y negativo - descendente) o ingresa un cero para salir: "))
    return escalones#Le pedimos al usuario el número de escalones que desea que tenga la escalera y retornamos la respuesta.

def escalera():
    contador = 1
    while contador != 0:
        escalones = menu()
        if escalones > 0:
            print("_")
            for l in range(0, escalones+1):
                base = "_"
                altura = "|"
                espacio = " " * (l + 1)
                print(f"{espacio}{altura}{base}")
            print("-------------------------------------")
#Si el número es negativo ejecutamos lo siguiente.
        elif escalones < 0:
            escalones = (escalones * -1)
            print(" " * escalones + "  _")
            for f in range(0, escalones+1):
                base = "_"
                altura = "|"
                espacio = " " * (escalones - f)
                print(f"{espacio}{base}{altura}")
            print("-----------------------------------")
        else:
            contador = 0

escalera()