'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 9 de enero de 2025
Descripción: Conversiones.
'''

def menu()->int:
    '''
    Muestra el menú del programa.
    :return: {Devuelve una opción elegida por el usuario a realizar}
    '''
    print("** Conversiones **")
    print("1.- Convertir cadena a entero.")
    print("2.- Convertir cadena a flotante.")
    print("0.- Salir.")
    opcion = input("Ingresa una opción: ")
    while not opcion.isnumeric():
        print("Opción no válida")
        opcion = input("Intenta nuevamente: ")
    opcion = int(opcion)
    print()
    return opcion

def cadena_a_entero(cadena: str)-> int | None:
    '''
    Función que convierte una cadena a un número entero con validación.
    :param cadena: {Es la cadena a convertir a un número entero}
    :return:
    '''
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-")
    if revisar_cadena.isnumeric() and no_guiones in (0,1):
        return int(cadena)
    else:
        return None

def cadena_a_flotante(cadena: str)-> float | None:
    '''
    Función que convierte una cadena a un número flotante con validación.
    :param cadena: {Es la cadena a convertir a flotante}
    :return:
    '''
    no_puntos = cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-").replace(".", "0")
    if revisar_cadena.isnumeric() and no_puntos in (0,1) and no_guiones in (0,1):
        return float(cadena)
    else:
        return None

salir = 1
while salir != 0:
    opcion = menu()
    if opcion == 1:
        num_cadena = input("Ingrese el número a convertir: ")
        numero = cadena_a_entero(num_cadena)
        while numero is None:
            num_cadena = input("Opción no válida. Intente nuevamente: ")
            numero = cadena_a_entero(num_cadena)

        print(f"El número {numero} es de tipo {type(numero)}")
        print()
    elif opcion == 2:
        num_cadena = input("Ingresa el número a convertir: ")
        numero = cadena_a_flotante(num_cadena)
        while numero is None:
            num_cadena = input("Opción no válida. Intente nuevamente: ")
            numero = cadena_a_flotante(num_cadena)
        print(f"El número {numero} es de tipo {type(numero)}")
        print()
    elif opcion == 0:
        salir = 0
    else:
        print("Opción no válida.")