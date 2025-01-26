"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 24 de enero de 2025
Descripción: Juego del Ahorcado.
"""
import random

def ahorcado(palabras):
    palabra = random.choice(palabras)
    palabra = str(palabra)
    palabras_ocultas = ["_"] * len(palabra)
    malas = 0
    letras_adivinadas = set()
    print("Bievenido al juego del Ahorcado. Adivina la palabra.")
    while malas != 9:
        if "_" not in palabras_ocultas:
            print(f"Felicidades!, Adivinaste la palabra '{palabra}'.")
            break

        print(palabras_ocultas)
        respuesta = input("Ingresa una letra de la a a la z: ").lower()

        while not respuesta.isalpha():
            print("Dato no válido.")
            respuesta = input("Inténtelo de nuevo: ")

        if len(respuesta) > 1 and len(respuesta) < len(palabra):
            respuesta = input("Ingresa solo un caracter: ")

        if len(respuesta) == len(palabra) and respuesta == palabra:
            print(f"Felicidades!, Adivinaste la palabra '{palabra}'.")
            break

        if respuesta in letras_adivinadas:
            print("Ya has adivinado esta letra, intenta con otra.")

        letras_adivinadas.add(respuesta)

        if respuesta in palabra:
            for i, letra in enumerate(palabra):
                if respuesta == letra:
                    print(f"La letra {respuesta} si esta en la palabra.")
                    palabras_ocultas[i] = respuesta
        else:
            print(f"La letra {respuesta} no se encuentra en la palabra.")
            malas += 1
    if malas == 9:
        print("Lo siento, perdiste, suerte a la próxima.")


if __name__ == '__main__':
    palabras = ['palabra', 'animal', 'comida', 'clase', 'persona', 'avion', 'zapato']
    ahorcado(palabras)