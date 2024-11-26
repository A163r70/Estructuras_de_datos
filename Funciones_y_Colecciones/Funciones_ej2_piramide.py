'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 21 de noviembre de 2024
Descripción: Ejrcicio sobre las pirámides, pero con funciones.
'''

def priamide1(filas):
    print("Forma 1")
    for k in range(1, filas+1):
        for l in range(1, k+1):
            print("*", end=" ")
        print()

    print("+++++++++++++++++++++++")
    print()

def piramide2(filas):
    print("Forma 2")
    final = filas
    for k in range(1, filas+1):
        for l in range(final):
            print("*", end=" ")
        print()
        final -= 1
    print("+++++++++++++++++++++++")
    print()

def piramide3(filas):
    print("Forma 3")
    limite = filas
    for k in range(0, limite):
        asterisco = "*" * limite
        espacio = " " * k
        print(f"{espacio}{asterisco}", end=" ")
        limite -= 1
        print()
    print("+++++++++++++++++++++++")
    print()

def piramide4(filas):
    print("Forma 4")
    for k in range(0, filas):
        asteriscos = "*" * (2 * k + 1)
        espacios = " " * (filas - k - 1)
        print(f"{espacios}{asteriscos}")
    print("+++++++++++++++++++++++")
    print()

def piramide5(filas):
    print("Forma 5")
    for k in range(0, filas):
        asteriscos = "*" * (2 * k + 1)
        espacios = " " * (filas - k - 1)
        print(f"{espacios}{asteriscos}")

filas = int(input("Ingrese cuantas filas tendrá la piramide: "))
priamide1(filas)
piramide2(filas)
piramide3(filas)
piramide4(filas)
piramide5(filas)

"""
En este programa se realizaron los mismos ejercios sobre las pirámides, pero en este caso utilizando funciones.
En este casó también se le pide al usuario el número de filas que tendrán las pirámides, lo cual se le envía
a las funciones para que trabajen con esas filas, imprimiendo en cada función el resultado de como se ve 
la pirámide.
"""