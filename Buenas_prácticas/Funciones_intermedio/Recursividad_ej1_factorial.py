"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 29 - 01- 2025
Descripción: Primer ejercicio de recursividad.
"""

def cadena_a_entero(cadena: str)-> int | None:
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-")
    if revisar_cadena.isnumeric() and no_guiones in (0,1) :
        return int(cadena)
    else:
        return None

def es_numero_valido(cadena: str) -> bool:
    """
    Función que determina si el número ingresado se encuentra entre 0 y un entero positivo.
    :param cadena: Cadena a validar.
    :return: Si la cadena cumple con el formato
    """
    if cadena.isnumeric():
        return True

    else:
        return False

def factorial(numero:int)->int:
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)


def main()->None:
    numero = input("Ingresa un número entre 0 y un entero positivo: ")
    if es_numero_valido(numero):
        numero = int(numero)
        numero_factorial = factorial(numero)
        print(f"El factorial del número {numero} es: {numero_factorial}")
    else:
        print("Valor no válido.")

if __name__ == '__main__':
    main()


