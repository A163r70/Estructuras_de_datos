'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 31 de Octubre de 2024
Descripción: Ejercico 4 del examen parcial.

Este programa es un juego en donde el usuario intente adivinar un número secreto.
Para ello:

a) El número a adivinar es un número aleatorio entre 1 y 100.
b) El jugador tendrá 5 intentos para encontrar el número.
c) Como pista, el juego indicará si el número a adivinar es menor o mayor al número ingresado, si el número no es el correcto.
d) Si el jugador adivina el número, el juego muestra un mensaje de felicitación y el número de intentos.
e) Si el jugador no adivina el número, el juego muestra un mensaje con el número.
'''
import random
from random import randint

intentos = 1
print("** Juego del adivinador **")
adivino = randint (1, 100)
while intentos <=5:
    numero = int(input(f"Número de intento: {intentos}. Ingresa un número (1/100): "))
    if numero < 1 or numero > 100:
        print("El número esta fuera del rango.")
    elif numero < adivino:
        print("El número a adivinar es mayor.")
        intentos += 1
    elif numero > adivino:
        print("El número a adivinar es menor.")
        intentos += 1
    else:
        print(f"¡Felicidades, adivinaste en {intentos} intentos.")
        break
    if intentos == 6:
        print(f"Perdiste. El número era: {adivino}")
        break

""""
Primero colocamos la libreria para el randint.
Creamos una variable que sera el contador de los intentos que hace el usuario.
Guardamos el número que sera el que adivinara el usuario creado aleatoriamente por el randint.
Pedimos un número al usuario y lo convertimos a un entero.
Hacemos las comparaciones y tomamos en cuenta que este dentro del rango solicitadon aumentando los intentos que hace
el usuario, y que culmina si hace más de 5 intentos.
"""