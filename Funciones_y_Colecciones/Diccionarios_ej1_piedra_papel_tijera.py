'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 02 de diciembre de 2024
Descripción: Primer ejercicio sobre diccionarios.
'''
from random import choice

piedra_papel_tijeras = {('PIEDRA', 'TIJERAS'): "JUGADOR",
                        ('PIEDRA', 'PAPEL'): "CPU",
                        ('PAPEL', 'PIEDRA'): "JUGADOR",
                        ('PAPEL', 'TIJERAS'): "CPU",
                        ('TIJERAS', 'PAPEL'): "JUGADOR",
                        ('TIJERAS', 'PIEDRA'): "CPU"}

def menu():
    print("***  Juego de piedra, papel o tijeras  ***")
    print("1.- Piedra.")
    print("2.- Papel.")
    print("3.- Tijeras.")
    print("Salir.")
    opcion = input("Ingresa una opción: ")
    return opcion

def jugador(opcion):
    eleccion_jugador = " "
    if opcion == 1:
        eleccion_jugador = "PIEDRA"
    elif opcion == 2:
        eleccion_jugador = "PAPEL"
    elif opcion == 3:
        eleccion_jugador = "TIJERAS"
    else:
        print("Valor no valido.")
    eleccion_cpu = choice(["PIEDRA", "PAPEL", "TIJERAS"])

    return eleccion_jugador, eleccion_cpu


