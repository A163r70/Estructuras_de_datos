"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 24 de enero de 2025
Descripción: Menú de los juegos del examen parcial 3.
"""
from Ahorcado import ahorcado
from Gato import imprimir_tablero, ganador, empate, juego_gato


def menu()->int:
    print("*** Menú de juegos ***")
    print("1.- El ahorcado.")
    print("2.- Gato.")
    print("3.- 4 en raya.")
    print("0.- Salir.")
    opcion = input("Ingrese una opción: ")
    while not opcion.isnumeric():
        print("Opción no válida")
        opcion = input("Intenta nuevamente: ")
    opcion = int(opcion)
    print()
    return opcion

if __name__ == '__main__':
    palabras = ['palabra', 'animal', 'comida', 'clase', 'persona', 'avion', 'zapato']
    tablero = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    salir = 1
    while salir != 0:
        opciones = menu()
        if opciones == 1:
            ahorcado(palabras)
            print()
        elif opciones == 2:
            juego_gato(tablero)
            print()
        elif opciones == 3:
            print("en proceso")
            print()
        elif opciones == 0:
            salir = 0
        else:
            print("Opción no válida.")
