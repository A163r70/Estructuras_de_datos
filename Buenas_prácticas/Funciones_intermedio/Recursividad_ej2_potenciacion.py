"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 29 - 01- 2025
Descripción: Segundo ejercicio de recursividad.
"""

def es_numero_valido(cadena1: str, cadena2:str) -> bool:
    """
    Función que determina si el número ingresado se encuentra entre 0 y un entero positivo.
    :param cadena1: Cadena a validar.
    :param cadena2: Segunda cadena a validar.
    :return: Si la cadena cumple con el formato
    """
    if cadena1.isnumeric() and cadena2.isnumeric():
        return True

    else:
        return False

def potencia(base:int, exponente:int)->int | None:
    if base == 0 and exponente == 0:
        return 0
    else:
        return base*(base **(exponente-1))


def main()->None:
    base = input("Ingresa la base a: ")
    exponente = input("Ingrese el exponente b: ")
    if es_numero_valido(base, exponente):
        base, exponente = int(base), int(exponente)
        if base ==0 and exponente == 0:
            print(f"{base} ^ {exponente}: Indeterminado.")
        else:
            potencia_numero = potencia(base, exponente)
            if potencia_numero == 0:
                print("indeterminado")
            else:
                print(f"{base} ^ {exponente}: {potencia_numero}")
    else:
        print("Valor no válido.")

if __name__ == '__main__':
    main()