"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 24 de enero de 2025
Descripción: Clculadora de suma y multiplicación.
"""
from Buenas_prácticas.Especificar_datos_en_funciones import cadena_a_flotante
from time import sleep
from termcolor import colored
from colorama import init

init()

def menu()->int:
    """
    Función que nos muestra el menú para escojer que opción hacer.
    :return:
    """
    print("*** Calculadora ***")
    print("1.- Suma.")
    print("2.- Multiplicación.")
    print("0.- Salir.")
    opcion = input("Elija una opción: ")
    while not opcion.isnumeric():
        print("Valor no válido.")
        opcion = input("Ingrese la opción de nuevo: ")
    opcion = int(opcion)
    print()
    return opcion

def suma(numero1: float, numero2:float)->float:
    """
    Función suma los números.
    :param numero1: Primer número a sumar.
    :param numero2: Segundo número a sumar.
    :return:
    """
    return numero1 + numero2

def multiplicacion(numero1:float, numero2:float)->float:
    """
    Función que multiplica los números.
    :param numero1: Primer número a multiplicar.
    :param numero2: Segundo número a multiplicar.
    :return:
    """
    return numero1 * numero2

if __name__ == '__main__':
    texto = "¿Qué operación harás hoy?."
    print()
    for letra in texto:
        print(colored(letra, 'green', attrs=['bold']), end=" ")
        sleep(.1)
    print()

    salida = 1
    while salida != 0:
        opcion = menu()
        if opcion == 1:

            numero1 = input("Ingrese el primer número a sumar: ")
            numero1 = cadena_a_flotante(numero1)
            while numero1 is None:
                print("Valor no válido.")
                numero1 = input("Ingrese un número válido: ")
                numero1 = cadena_a_flotante(numero1)

            numero2 = input("Ingrese el segundo número a sumar: ")
            numero2 = cadena_a_flotante(numero2)
            while numero2 is None:
                print("Valor no válido.")
                numero2 = input("Ingrese un número válido: ")
                numero2 = cadena_a_flotante(numero2)

            resultado = suma(numero1, numero2)

            print(f"El resultado de la suma es: {resultado}")
            print()
        elif opcion == 2:
            numero1 = input("Ingrese el primer número a multiplicar: ")
            numero1 = cadena_a_flotante(numero1)
            while numero1 is None:
                print("Valor no válido.")
                numero1 = input("Ingrese un número válido: ")
                numero1 = cadena_a_flotante(numero1)

            numero2 = input("Ingrese el segundo número a multiplicar: ")
            numero2 = cadena_a_flotante(numero2)
            while numero2 is None:
                print("Valor no válido.")
                numero2 = input("Ingrese un número válido: ")
                numero2 = cadena_a_flotante(numero2)

            resultado = multiplicacion(numero1, numero2)
            print(f"El resultado de la multiplicación es: {resultado}")
            print()
        elif opcion == 0:
            print("Saliendo...")
            salida = 0
        else:
            print("Valor no válido.")