'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 06 de enero de 2025
Descripción: Piedra, Ppapel o Tijeras de la serie El juego del Calamar.
'''
import random
from random import choice

victorias = 0
empates = 0
victorias_cpu = 0
opcion = 1
cpu_opcion1 = "nada"
cpu_opcion2 = "nada2"
cpu = "nada3"
opcion1_jugador = "jugador"
opcion2_jugador = "jugado"
cpu_opciones = [ ]
opcionf_jugador = "valor"
print("** Juego de piedra papel o tijeras **")
while opcion != 0:
    print(f"Victorias del jugador: {victorias}, empates: {empates}, victorias del CPU: {victorias_cpu}")
    print("1) Piedra.")
    print("2) Papel.")
    print("3) Tijeras..")
    print("0) Salir..")
    opcion1 = int(input("Eliga una opcion: "))
    opcion2 = int(input("Eliga otra opcion: "))
    cpu1 = random.randint(1, 3)
    cpu2 = random.randint(1, 3)
    if cpu1 == 1:
        cpu_opciones.insert(0, "Piedra")
    elif cpu1 == 2:
        cpu_opciones.insert(0, "Papel")
    elif cpu1 == 3:
        cpu_opciones.insert(0, "Tijera")

    if cpu2 == 1:
        cpu_opciones.insert(1, "Piedra")
    elif cpu2 == 2:
        cpu_opciones.insert(1, "Piedra")
    elif cpu2 == 3:
        cpu_opciones.insert(1, "Piedra")

    if opcion1 == 1:
        opcion1_jugador = "Piedra"
    elif opcion1 == 2:
        opcion1_jugador = "Papel"
    elif opcion1 == 3:
        opcion1_jugador = "Tijera"

    if opcion2 == 1:
        opcion2_jugador = "Piedra"
    elif opcion2 == 2:
        opcion2_jugador = "Papel"
    elif opcion2 == 3:
        opcion2_jugador = "Tijera"

    print(f"Opciones de la CPU: {cpu_opciones[0]} y {cpu_opciones[1]}")
    opcion3 = int(input(f"Elija una de las dos opciones que eligió: 1.-{opcion1_jugador} ó 2.-{opcion2_jugador}: "))

    if opcion3 == 1:
        opcionf_jugador = opcion1_jugador
    else:
        opcionf_jugador = opcion2_jugador

    cpu_opcion = choice(cpu_opciones)
    print(f"Opcion final de la CPU es: {cpu_opcion}")

    if opcionf_jugador == cpu1:
        print(f"Jugador: {opcion1_jugador}, CPU: {cpu_opcion1}. El resultado es empate.")
        empates += 1
    elif opcionf_jugador ==1 and cpu1 == 2:
        print(f"Jugador: {opcion1_jugador}, CPU: {cpu_opcion1}. El ganador es el CPU.")
        victorias_cpu += 1
    elif opcionf_jugador ==1 and cpu1 == 3:
        print(f"Jugador: {opcion1_jugador}, CPU: {cpu_opcion1}. El ganador es el jugador.")
        victorias += 1
    elif opcionf_jugador ==2 and cpu1 == 1:
        print(f"Jugador: {opcion1_jugador}, CPU: {cpu_opcion1}. El ganador es el jugador.")
        victorias += 1
    elif opcionf_jugador ==2 and cpu1 == 3:
        print(f"Jugador: {opcion1_jugador}, CPU: {cpu_opcion1}. El ganador es el CPU.")
        victorias_cpu += 1
    elif opcionf_jugador ==3 and cpu1 == 1:
        print(f"Jugador: {opcion1_jugador}, CPU: {cpu_opcion1}. El ganador es el CPU.")
        victorias_cpu += 1
    elif opcionf_jugador ==3 and cpu1 == 2:
        print(f"Jugador: {opcion1_jugador}, CPU: {cpu_opcion1}. El ganador es el jugador.")
        victorias += 1
    elif opcionf_jugador == 0 and opcion2 == 0:
        opcion1 = 0
        print("Fin del juego")
        print(f"Victorias del jugador: {victorias}, empates: {empates}, victorias del CPU: {victorias_cpu}")
    else:
        print("Opción no válida.")