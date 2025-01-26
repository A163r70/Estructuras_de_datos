"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 24 de enero de 2025
Descripción: Juego 4 en raya.
"""

tablero = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']]

def mostrar_tablero(tablero):
    print("-----------------------------")
    for fila in tablero:
        print("|", fila[0], "|", fila[1], "|", fila[2], "|", fila[3], "|", fila[4], "|", fila[5], "|", fila[6], "|")
        print("-----------------------------")

def juego(tablero):
    pass

if __name__ == '__main__':
    mostrar_tablero(tablero)