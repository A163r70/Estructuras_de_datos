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
adivino1 = randint (1, 50)
adivino2 = randint(1, 100)
adivino3 = randint(1, 110)

print("[F]- 10 intentos y números de 1-50.")
print("[M]- 5 intentos y números de 1-100.")
print("[D]- 4 intentos y números de 1-110.")
dificultad = input("Ingrese la dificultad: ")
while intentos != 0:
    if dificultad == "f" or dificultad == "F":
        numero = int(input(f"Número de intento: {intentos}. Ingresa un número (1/50): "))
        if numero < 1 or numero > 50:
            print("El número esta fuera del rango.")
        elif numero < adivino1:
            print("El número a adivinar es mayor.")
            intentos += 1
        elif numero > adivino1:
            print("El número a adivinar es menor.")
            intentos += 1
        else:
            print(f"¡Felicidades, adivinaste en {intentos} intentos.")
            break
        if intentos == 11:
            print(f"Perdiste. El número era: {adivino1}")
            break
    elif dificultad == "m" or dificultad == "M":
        numero = int(input(f"Número de intento: {intentos}. Ingresa un número (1/100): "))
        if numero < 1 or numero > 100:
            print("El número esta fuera del rango.")
        elif numero < adivino2:
            print("El número a adivinar es mayor.")
            intentos += 1
        elif numero > adivino2:
            print("El número a adivinar es menor.")
            intentos += 1
        else:
            print(f"¡Felicidades, adivinaste en {intentos} intentos.")
            break
        if intentos == 6:
            print(f"Perdiste. El número era: {adivino2}")
            break
    elif dificultad == "d" or dificultad == "D":
        numero = int(input(f"Número de intento: {intentos}. Ingresa un número (1/110): "))
        if numero < 1 or numero > 110:
            print("El número esta fuera del rango.")
        elif numero < adivino3:
            print("El número a adivinar es mayor.")
            intentos += 1
        elif numero > adivino3:
            print("El número a adivinar es menor.")
            intentos += 1
        else:
            print(f"¡Felicidades, adivinaste en {intentos} intentos.")
            break
        if intentos == 5:
            print(f"Perdiste. El número era: {adivino3}")
            break
    else:
        print("Valor inválido.")
