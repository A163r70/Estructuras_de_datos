'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 06 de diciembre de 2024
Descripción: Primer ejercicio sobre diccionarios.
'''

def menu():
    print("*** Ejercicio 1. La escalera. ***")
    escalones = int(input("Ingresa el número de escalones (positivo - ascendente y negativo - descendente) o ingresa un cero para salir: "))
    return escalones

def escalera():
    contador = 1
    while contador != 0:
        escalones = menu()
        if escalones > 0:
            print(" " * escalones + "  _")
            for f in range(0, escalones):
                base = "_"
                altura = "|"
                espacio = " " * (escalones - f)
                print(f"{espacio}{base}{altura}")
            print("-------------------------------------")
        elif escalones < 0:
            escalones = (escalones * -1)
            print("_")
            for l in range(0, escalones):
                base = "_"
                altura = "|"
                espacio = " " * (l + 1)
                print(f"{espacio}{altura}{base}")
            print("-----------------------------------")
        else:
            contador = 0

escalera()

