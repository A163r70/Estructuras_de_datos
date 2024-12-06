'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 02 de diciembre de 2024
Descripción: Primer ejercicio sobre diccionarios.
'''
from random import choice

victorias = 0
empates = 0
victorias_cpu = 0

piedra_papel_tijeras = {('PIEDRA', 'TIJERAS'): "JUGADOR",
                        ('PIEDRA', 'PAPEL'): "CPU",
                        ('PAPEL', 'PIEDRA'): "JUGADOR",
                        ('PAPEL', 'TIJERAS'): "CPU",
                        ('TIJERAS', 'PAPEL'): "JUGADOR",
                        ('TIJERAS', 'PIEDRA'): "CPU"}

def menu(victorias, empates, victorias_cpu):
    print(f"Victorias del jugador: {victorias}, empates: {empates}, victorias del CPU: {victorias_cpu}")
    print("***  Juego de piedra, papel o tijeras  ***")
    print("1.- Piedra.")
    print("2.- Papel.")
    print("3.- Tijeras.")
    print("0.- Salir.")
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
    elif opcion == 0:
        return
    else:
        print("Valor no valido.")
    eleccion_cpu = choice(["PIEDRA", "PAPEL", "TIJERAS"])

    return eleccion_jugador, eleccion_cpu

def juego(eleccion_jugador, eleccion_cpu, piedra_papel_tijeras, victorias, victorias_cpu, empates):
    resultado = piedra_papel_tijeras.get((eleccion_jugador, eleccion_cpu), "EMPATE")
    if resultado == "JUGADOR":
        print(f"Jugador: {eleccion_jugador}. CPU: {eleccion_cpu}. El resultado es: {resultado}")
        victorias += 1
    elif resultado == "CPU":
        print(f"Jugador: {eleccion_jugador}. CPU: {eleccion_cpu}. El resultado es: {resultado}")
        victorias_cpu += 1
    else:
        print(f"Jugador: {eleccion_jugador}. CPU: {eleccion_cpu}. El resultado es: EMPATE")
        empates += 1
    print()
    return victorias, victorias_cpu, empates

opcion = menu(victorias, empates, victorias_cpu)
jugador(opcion)
juego(jugador(menu(victorias, empates, victorias_cpu)), piedra_papel_tijeras, victorias, victorias_cpu, empates)