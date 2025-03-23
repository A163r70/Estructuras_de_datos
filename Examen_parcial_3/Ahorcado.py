"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 24 de enero de 2025
Descripción: Juego del Ahorcado.
"""
import random
from time import sleep
from termcolor import colored
from colorama import init

init()

def mostrar_letrero()->None:
    texto = "Bienvenido al juego del Ahorcado, adivina la palabra."
    print()
    for letra in texto:
        print(colored(letra, 'green', attrs=['bold']), end=" ")
        sleep(.1)
    print()

def ahorcado(palabras)->None:
    """
    Función que nos permite jugar el juego del ahorcado.
    :param palabras: Es la matriz que contiene las palabras para el juego.
    :return:
    """
    mostrar_letrero()
    palabra = random.choice(palabras)
    palabra = str(palabra)
    palabras_ocultas = ["_"] * len(palabra)
    malas = 6
    letras_adivinadas = set()
    while malas != 0:
        if "_" not in palabras_ocultas:
            print(f"Felicidades!, Adivinaste la palabra '{palabra}'.")
            break

        print(palabras_ocultas)
        print(f"Tienes {malas} oportunidades.")
        respuesta = input(f"Ingresa una letra de la a a la z: ").lower()
        print()

        while not respuesta.isalpha():
            print("Dato no válido.")
            print(f" {malas} oportunidades.")
            respuesta = input("Inténtelo de nuevo, ingresa una letra: ")
            print()

        if len(respuesta) > 1 and len(respuesta) < len(palabra):
            respuesta = input("Ingresa solo un caracter: ")
            print()

        if len(respuesta) == len(palabra) and respuesta == palabra:
            print(f"Felicidades!, Adivinaste la palabra '{palabra}'.")
            break

        if respuesta in letras_adivinadas:
            print("Ya has adivinado esta letra, intenta con otra.")
            print()

        letras_adivinadas.add(respuesta)

        if respuesta in palabra:
            for i, letra in enumerate(palabra):
                if respuesta == letra:
                    print(f"La letra {respuesta} si esta en la palabra.")
                    print()
                    palabras_ocultas[i] = respuesta
        else:
            print(f"La letra {respuesta} no se encuentra en la palabra.")
            print()
            malas -= 1
    if malas == 0:
        print("Lo siento, perdiste, suerte a la próxima.")
        print(f"La palabra era '{palabra}'.")


if __name__ == '__main__':
    palabras = ['palabra', 'animal', 'comida', 'clase', 'persona', 'avion', 'zapato', 'nombre', 'camisa',
                'taza', 'mesa', 'cama', 'mochila']
    ahorcado(palabras)