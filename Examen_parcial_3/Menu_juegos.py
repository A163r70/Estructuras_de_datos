"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 24 de enero de 2025
Descripción: Menú de los juegos del examen parcial 3.
"""
from Ahorcado import ahorcado
from menu_gato import menu_gato
from time import sleep
from termcolor import colored
from colorama import init
init()
def menu()->int:
    """
    Función que nos muestra el menú de juegos.
    :return:
    """
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
    texto = "Bienvenido al menú de juegos, escoje el juego  y a jugar."
    print()
    for letra in texto:
        print(colored(letra, 'green', attrs=['bold']), end=" ")
        sleep(.1)
    print()

    palabras = ['palabra', 'animal', 'comida', 'clase', 'persona', 'avion', 'zapato', 'nombre', 'camisa',
                'taza', 'mesa', 'cama', 'mochila']
    tablero = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    salir = 1
    while salir != 0:
        opciones = menu()
        if opciones == 1:
            ahorcado(palabras)
            print()
        elif opciones == 2:
            menu_gato()
            print()
        elif opciones == 3:
            print("En proceso, aún no queda.")
            print()
        elif opciones == 0:
            salir = 0
        else:
            print("Opción no válida.")
