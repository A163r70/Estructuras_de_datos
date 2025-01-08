'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 8 de enero de 2025
Descripción: Conversiones.
'''

def cadena_a_entero(cadena: str)-> int | None:
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-")
    if revisar_cadena.isnumeric() and no_guiones in (0,1):
        return int(cadena)
    else:
        return None

if opcion == 2:
    num_cadena = input("Ingrese el número a convertir: ")
    numero = cadena_a_entero(num_cadena)
    while numero is None:
        num_cadena = input("Opción no válida, intente nuevamente: ")
        numero = cadena_a_entero(num_cadena)

    print(f"El número {numero} es de tipo {type(numero)}")