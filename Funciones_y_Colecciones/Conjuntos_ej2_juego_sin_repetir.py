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
        palabra = palabra.lower( )
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



"""
Este programa permite ingresar varias palabras sbre un tema y termina cuando ingresan palabras que ya habían ingresado
previamente.
Primero  en una función mostramos las reglas del juego y empezamos pidiendo el tema para que empiezen a escribir 
palabras y retornamos el tema. Otra función recibe el conjunt vacío donde se guardaran las palabras ingresadas y 
recibe también el tema. Dentro de esta segunda función se desarrolla la lógica del juego. Declaramos primero
una variable que contará las palabras que se vayan ingresando, después empieza el while que termina hasta que la
variables contador sea igual a 0, pedimos la primera palabra y la guardamos en una variable cualquiera, después esa
palabra la convertimos a minúscula. Preguntamos con un if si la palabra ingresada ya esta dentro del conjunto, si esta
ya dentro finalizamos el programa mostrando la cantidad de palabras que se ingresarón así como las palabras
ingresadas, en caso opuesto, si la palabra ingresada aún no se encuentra en el conjunto se lo asignamos a este, 
después aumenamos el contador y así sucesivamente.
En el código a nivel módulo solo ,mandamos a llamar a nuestras dos funciones.  
"""