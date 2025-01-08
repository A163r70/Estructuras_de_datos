'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 06 de enero de 2025
Descripción: Conversiones.
'''

#TODO Implementar menú.
def menu():
    pass#no hacer nada, es para ponerlo en pendiente, mientras hacemos algo más

#TODO Implementar la conversión de.
def cadena_a_entero(cadena):
    ...

#se usa para que revise
#FIXME Revisar caso n=0

def cadena_a_flotante(cadena):
    raise NotImplementedError("Implementar función")

opcion = menu()
while opcion != 0:
    if opcion == 1:
        num_cadena = input("Ingrese el número a convertir: ")
        numero = cadena_a_entero(num_cadena)
        while numero is None:
            num_cadena = input("Opción no válida, intente nuevamente: ")
            numero = cadena_a_entero(num_cadena)

        print(f"El número {numero} es de tipo {type(numero)}")
    elif opcion == 2:
        num_cadena = input("Ingrese el número a convertir: ")
        numero = cadena_a_entero(num_cadena)
        while numero is None:
            num_cadena = input("Opción no válida, intente nuevamente: ")
            numero = cadena_a_entero(num_cadena)

        print(f"El número {numero} es de tipo {type(numero)}")
    else:
        print("Valor no válido.")


