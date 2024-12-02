'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 29 de noviembre de 2024
Descripción: Primer ejercicio de conjuntos.
'''

palabras = set( )

def menu():
    print("***  Juego 'sin repetir'  ***")
    print("Este es un juego que se puede jugar de manera grupal, en donde el objetivo es decir palabras de un tema en específico y los jugadores deben tratar de no repetir la misma palabra. ")
    tema = input("Ingrese el tema de juego: ")
    print()
    return tema

def juego(palabras, tema_juego):
    contador = 1
    while contador != 0:
        palabra = input(f"Ingresa la palabra {contador} del tema {tema_juego}: ")
        if palabra in palabras:
            print(f"El juego ha terminado, han dicho {contador} palabras.")
            print(f"Las palabras del tema {tema_juego} fueron: {palabras}")
            contador = 0
            return
        else:
            palabras.add(palabra)
        contador += 1

tema_juego = menu()
juego(palabras, tema_juego)