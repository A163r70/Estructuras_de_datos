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

victorias = 0
empates = 0
victorias_cpu = 0
opcion = 1
cpu_opcion = "nada"
opcion_jugador = "jugador"
print("** Juego de piedra papel o tijeras **")
while opcion != 0:
    print(f"Victorias del jugador: {victorias}, empates: {empates}, victorias del CPU: {victorias_cpu}")
    print("1) Piedra.")
    print("2) Papel.")
    print("3) Tijeras..")
    print("0) Salir..")
    opcion = int(input("Eliga una opcion: "))
    cpu = randint(1, 3)
    if cpu == 1:
        cpu_opcion = "Piedra"
    elif cpu == 2:
        cpu_opcion = "Papel"
    elif cpu == 3:
        cpu_opcion = "Tijera"\

    if opcion == 1:
        opcion_jugador = "Piedra"
    elif opcion == 2:
        opcion_jugador = "Papel"
    elif opcion == 3:
        opcion_jugador = "Tijera"

    if opcion == cpu:
        print(f"Jugador: {opcion_jugador}, CPU: {cpu_opcion}. El resultado es empate.")
        empates += 1
    elif opcion ==1 and cpu == 2:
        print(f"Jugador: {opcion_jugador}, CPU: {cpu_opcion}. El ganador es el CPU.")
        victorias_cpu += 1
    elif opcion ==1 and cpu == 3:
        print(f"Jugador: {opcion_jugador}, CPU: {cpu_opcion}. El ganador es el jugador.")
        victorias += 1
    elif opcion ==2 and cpu == 1:
        print(f"Jugador: {opcion_jugador}, CPU: {cpu_opcion}. El ganador es el jugador.")
        victorias += 1
    elif opcion ==2 and cpu == 3:
        print(f"Jugador: {opcion_jugador}, CPU: {cpu_opcion}. El ganador es el CPU.")
        victorias_cpu += 1
    elif opcion ==3 and cpu == 1:
        print(f"Jugador: {opcion_jugador}, CPU: {cpu_opcion}. El ganador es el CPU.")
        victorias_cpu += 1
    elif opcion ==3 and cpu == 2:
        print(f"Jugador: {opcion_jugador}, CPU: {cpu_opcion}. El ganador es el jugador.")
        victorias += 1
    elif opcion == 0:
        opcion = 0
        print("Fin del juego")
        print(f"Victorias del jugador: {victorias}, empates: {empates}, victorias del CPU: {victorias_cpu}")
    else:
        print("Opción no válida.")

"""
Comentarios sobre el programa.
Primero colocamos la libreria para poder usar el randint. Declaramos variables de tipo entero y cadena que ocuparemos
después. Iniciamos el while y mostramos el menú, donde el ususario elegirá una opción, y en otra variable guardamos
el número que generó el randint la cual es la opción del CPU. 

Dependiendo de la opción que eliga el ususario a una
variable declarada previamente le asignamos si es "piedra", "papel" o "tijeras", hacemos lo mismo para la opción que
genere el randint para la CPU.

Empezamos haciendo las comparaciones para ver quien gana o si quedan empatados, tomando en cuenta todas las 
convinaciones posibles, y a la misma vez aumentamos los contadores que las veces que gana el usuario o la CPU, victoiras
y empates que se irán mostrando confome vaya avanzando el juego.
"""