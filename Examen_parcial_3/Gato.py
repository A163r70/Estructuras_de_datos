"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 24 de enero de 2025
Descripción: Juego del gato.
"""
from random import choice
import random

def imprimir_tablero(tablero):
    print("-------------")
    for fila in tablero:
        print("|", fila[0], "|", fila[1], "|", fila[2], "|")
        print("-------------")

def ganador(tablero, jugador):
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == jugador:
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == jugador:
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True
    return False

def empate(tablero):
    for fila in tablero:
        if ' ' in fila:
            return False
    return True

def juego_gato(tablero):
    print("Bienvenido al juego del Gato.")
    jugador = "x"
    cpu = "o"

    while True:
        imprimir_tablero(tablero)
        valido = False
        while not valido:
            fila = input("Escoge una fila (0,1,2): ")
            columna = input("Escoge una columna (0,1,2): ")
            if not (fila.isnumeric() and columna.isnumeric()):
                print("Opción no válida. Ingresa números.")
            else:
                fila, columna = int(fila), int(columna)

                if fila < 0 or fila > 2 or columna < 0 or columna > 2:
                    print("Opción fuera de rango. Inténtalo de nuevo.")

                if tablero[fila][columna] == " ":
                    tablero[fila][columna] = jugador
                    valido = True
                else:
                    print("Lugar ocupado.")

        if ganador(tablero, jugador):
            imprimir_tablero(tablero)
            print("Felicidades!, has ganado el juego.")
            break

        if empate(tablero):
            imprimir_tablero(tablero)
            print("Es un empate.")
            break

        valido = False
        while not valido:
            fila_cpu = random.randint(0, 2)
            columna_cpu = random.randint(0,2)

            if tablero[fila_cpu][columna_cpu] == " ":
                tablero[fila_cpu][columna_cpu] = cpu
                valido = True
        if ganador(tablero, cpu):
            imprimir_tablero(tablero)
            print("Gano la CPU, suerte a la próxima.")
            break

        if empate(tablero):
            imprimir_tablero(tablero)
            print("Es un empate.")
            break


if __name__ == '__main__':
    tablero = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    juego_gato(tablero)

