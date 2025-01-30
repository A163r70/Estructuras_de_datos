"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 29 - 01- 2025
Descripción: Segundo ejercicio de argumentos variables.
"""

def cadena_a_flotante(cadena: str)-> float | None:
    no_puntos = cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-").replace(".", "")
    if revisar_cadena.isnumeric() and no_puntos in (0,1) and no_guiones in (0,1):
        return float(cadena)
    else:
        return None

def maximo_minimo(*vargs):
    maximo = vargs[0]
    minimo = vargs[0]
    if len(vargs) != 0:
        for numero in vargs:
            if numero > maximo:
                maximo = numero
            elif numero < minimo:
                minimo = numero
    return maximo, minimo



def main()->None:
    maximominimo = []
    numeros = input(f"Ingresa el número [{len(maximominimo)+1}] o presiona enter para calcular: ")
    while bool(numeros):
        numero = cadena_a_flotante(cadena=numeros)
        if numero is None:
            print("Valor no válido.")
        else:
            maximominimo.append(numero)
        numeros = input(f"Ingresa el número [{len(maximominimo) + 1}] o presiona enter para calcular: ")

    maximo, minimo = maximo_minimo(*maximominimo)
    print(f"El número máximo de la lista es el: {maximo}.")
    print(f"El número mínimo de la lista es el: {minimo}")

if __name__ == '__main__':
    main()