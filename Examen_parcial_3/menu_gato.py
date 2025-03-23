from time import sleep
from termcolor import colored
from colorama import init
from Gato import unovscpu, unovsuno

init()

def mostrar_letrero()->None:
    texto = "Bienvenido al juego del Gato, ¿crees poder ganar?."
    print()
    for letra in texto:
        print(colored(letra, 'green', attrs=['blink', 'bold', 'underline']), end=" ")
        sleep(.1)
    print()

def menu_gato()->int:
    mostrar_letrero()
    print("1.- 1 vs 1.")
    print("2.- Usuario vs CPU.")
    print("0.- Salir.")
    opcion = input("Escoja una opción: ")
    while not opcion.isnumeric():
        print("Opción no válida")
        opcion = input("Intenta nuevamente: ")
    opcion = int(opcion)
    print()
    return opcion

if __name__ == '__main__':
    tablero = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    opcion = menu_gato()
    while True:
        if opcion == 1:
            unovsuno(tablero)
        elif opcion == 2:
            unovscpu(tablero)
        elif opcion == 0:
            print("Vuelve pronto.")
            break
        else:
            print("Valor no válido.")