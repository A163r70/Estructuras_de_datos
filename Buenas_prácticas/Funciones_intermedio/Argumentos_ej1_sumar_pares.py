"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 29 - 01- 2025
Descripción: Primer ejercicio de argumentos variables.
"""

def cadena_a_entero(cadena: str)-> int | None:
    """
    Función que convierte una cadena a entero.
    :param cadena: Cadena a convertir en entero.
    :return: La cadena convertida.
    """
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-")
    if revisar_cadena.isnumeric() and no_guiones in (0,1) :
        return int(cadena)
    else:
        return None

def sumar_numeros(* vargs)->int:
    """
    Función que suma los números pares.
    :param vargs: La cadena de números variables a sumar.
    :return: La suma de los números.
    """
    suma = 0
    if len(vargs) != 0:
        for numero in vargs:
            if numero %2 == 0:
                suma += numero
    else:
        print("Intenta de nuevo.")

    return suma

def main()->None:
    """
    Función principal.
    :return:
    """
    numeros_sumar = []
    cantidad_numeros = input(f"Ingresa el número [{len(numeros_sumar)+1}] o presiona enter para sumar: ")
    while bool(cantidad_numeros):
        numero = cadena_a_entero(cadena= cantidad_numeros)
        if numero is None:
            print("Valor no válido, intenta de nuevo.")
        else:
            numeros_sumar.append(numero)
        cantidad_numeros = input(f"Ingresa el número [{len(numeros_sumar) + 1}] o presiona enter para sumar: ")

    suma = sumar_numeros(*numeros_sumar)
    print(f"La suma de los números pares es de: {suma}")

if __name__ == '__main__':
    main()