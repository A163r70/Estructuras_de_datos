'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 29 de noviembre de 2024
Descripción: Primer ejercicio de conjuntos.
'''
import random
correos = set( )

def menu():
    print("*** Rifa de una computadora ***")
    print("1.- Ver correos de participantes.")
    print("2.- Agregar correo de participante.")
    print("3.- Eliminar correo de participante.")
    print("4.- Seleccionar ganador.")
    print("0.- Salir.")
    opcion = int(input("Eliga una opción: "))
    print()
    return opcion

def ver_correos(correos):
    if len(correos) == 0:
        print("No hay correos agregados.")
    else:
        for correo in correos:
            print(f"- {correo}")
    print()

def agregar(correos):
    correo = input("Ingrese el correo del participante: ")
    correos.add(correo)
    print(f"El correo '{correo}' ha sido agregado correctamente.")
    print()
    return correos

def eliminar_correo(correos):
    if len(correos) == 0:
        print("No hay correos para eliminar.")
    else:
        ver_correos(correos)
        eliminar = input("Ingrese el correo que desea eliminar: ")
        if eliminar in correos:
            correos.remove(eliminar)
            print(f"El correo '{eliminar}' ah sido eliminado.")
        else:
            print("El correo ingresado no existe, vuelva a intentarlo.")
    print()

def seleccionar_ganador(correos):
    if len(correos) == 0:
        print("No hay correos.")
    else:
        lista_correos = list(correos)
        ganador = random.choice(lista_correos)
        print(f"El correo ganador es '{ganador}'. Muchas felicidades!!.")
    print()

contador = 1
while contador != 0:
    opciones = menu()
    if opciones == 1:#Ver correos
        ver_correos(correos)
    elif opciones == 2:#Agregar correo
        agregar(correos)
    elif opciones == 3:#Eliminar
        eliminar_correo(correos)
    elif opciones == 4:#seleccionar ganador
        seleccionar_ganador(correos)
    elif opciones == 0:
        contador = 0
    else:
        print("Valor no válido.")