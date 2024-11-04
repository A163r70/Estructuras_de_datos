'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 31 de Octubre de 2024
Descripción: Ejercico 3 del examen parcial.

Este programa es el famoso juego de "piedra, papel o tijera", en donde el contrincante es la CPU.
La opción de la CPU se escogerá de forma aleatorio con la función randint().

El juego mostrará las victorias del jugador, los partidos empatados y las victorias del CPU.
Además, mostrará el siguiente menú:

1) Piedra.
2) Papel.
3) Tijera.
0) Salir.
Cualquier otro caso -> Mostrar un mensaje de "opción no válida".
'''
import random
from random import randint

contador = 1
victorias = 0
empates = 0
victorias_cpu = 0
print("** Juego de piedra papel o tijeras **")
while contador != 0:
    print(f"Victorias del jugador: {victorias}, empates: {empates}, victorias del CPU: {victorias_cpu}")
    print("Piedra.")
    print("Papel.")
    print("Tijeras..")
    print("Salir..")
    opcion = input("Escriba la opción que quiera: ")
    cpu = randint(1, 3)
    if cpu == 1:
        cpu_opcion = "Piedra"
    elif cpu == 2:
        cpu_opcion = "Papel"
    elif cpu == 3:
        cpu_opcion = "Tijeras"

    if opcion == cpu_opcion and opcion == cpu_opcion and opcion == cpu_opcion:
        print(f"Jugador: {opcion}, CPU: {cpu_opcion}. El resultado es empate.")
        empates += 1
    elif (opcion =="piedra" or opcion == "Piedra") and cpu == 2:
        print(f"Jugador: {opcion}, CPU: {cpu_opcion}. El ganador es el jugador.")
        victorias_cpu += 1
    elif (opcion =="piedra" or opcion == "Piedra") and cpu == 3:
        print(f"Jugador: {opcion}, CPU: {cpu_opcion}. El ganador es el CPU.")
        victorias += 1
    elif (opcion =="papel" or opcion == "Papel") and cpu == 1:
        print(f"Jugador: {opcion}, CPU: {cpu_opcion}. El ganador es el CPU.")
        victorias += 1
    elif (opcion =="papel" or opcion == "Papel") and cpu == 3:
        print(f"Jugador: {opcion}, CPU: {cpu_opcion}. El ganador es el jugador.")
        victorias_cpu += 1
    elif (opcion =="tijeras" or opcion == "Tijeras") and cpu == 1:
        print(f"Jugador: {opcion}, CPU: {cpu_opcion}. El ganador es el jugador.")
        victorias_cpu += 1
    elif (opcion =="tijeras" or opcion == "Tijeras") and cpu == 2:
        print(f"Jugador: {opcion}, CPU: {cpu_opcion}. El ganador es el CPU.")
        victorias += 1
    elif opcion == "salir" or opcion == "Salir":
        contador = 0
        print("Fin del juego")
        print(f"Victorias del jugador: {victorias}, empates: {empates}, victorias del CPU: {victorias_cpu}")
    else:
        print("Opción no válida.")