"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 24 de enero de 2025
Descripción: Juego 4 en raya.
"""
from time import sleep
from termcolor import colored
from colorama import init

init()

tablero = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ']]

def mostrar_tablero(tablero):
    print("-----------------")
    for fila in tablero:
        print("|", fila[0], "|", fila[1], "|", fila[2], "|", fila[3], "|")
        print("-----------------")

def hay_espacio(tablero, columna:int)->bool:
    for i in range():
        if tablero[columna][3-i] == ' ':
            return True
        else:
            print("No hay espacio.")


def juego(tablero):

    while True:
        mostrar_tablero(tablero)
        valido = False
        while not valido:
            columna = input("Escoje una columna: ")
            if not(columna.isnumeric()):
                print("Opción no válida. Ingresa números.")
            else:
                columna = int(columna)

                if columna < 0 or columna > 4:
                    print("Opción fuera de rango. Inténtalo de nuevo.")
                elif hay_espacio(tablero, columna) == True:


if __name__ == '__main__':
    texto = "Bienvenido al juego 4 en Raya."
    print()
    for letra in texto:
        print(colored(letra, 'green', attrs=['bold']), end=" ")
        sleep(.1)
    print()

    mostrar_tablero(tablero)