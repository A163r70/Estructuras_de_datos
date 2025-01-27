"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 24 de enero de 2025
Descripción: Programa que calcula el promedio de un alumno.
"""
from Buenas_prácticas.Especificar_datos_en_funciones import cadena_a_flotante
from time import sleep
from termcolor import colored
from colorama import init

init()


def datos(calificaciones)->None:
    """
    Función que nos permite calcular el promedio de un parcial de un alumno.
    :param calificaciones:
    :return:
    """
    nombre = input("Ingresa tu nombre: ").strip()
    while not nombre.replace(" ", "").isalpha():
        print("Valor no válido.")
        nombre = input("Intenta de nuevo: ").strip()
    calificaciones['Nombre'] = nombre
    for materia in calificaciones['Materias']:
        while True:
            calificacion = input(f"Ingrese la calificación de la materia {materia}: ")
            calificacion = cadena_a_flotante(calificacion)
            while calificacion is None:
                print("Valor no válido.")
                calificacion = input("Ingrese un número válido: ")
                calificacion = cadena_a_flotante(calificacion)

            if calificacion < 0 or calificacion > 10:
                print("La alificación esta fuera de rango.")
                calificacion = input("Intentalo de nuevo: ")
                calificacion = cadena_a_flotante(calificacion)
                while calificacion is None:
                    print("Valor no válido.")
                    calificacion = input("Ingrese un número válido: ")
                    calificacion = cadena_a_flotante(calificacion)
            else:
                calificaciones['Materias'][materia] = calificacion
                break
    print()
    print("*** Calificaciones ***")
    print(f"Alumno: {calificaciones['Nombre']}")
    for materia, calificacion in calificaciones['Materias'].items():
        print(f"{materia}: {calificacion}")
    promedio(calificaciones)

def promedio(calificaciones)->None:
    suma = 0
    materias = len(calificaciones['Materias'])
    for calificacion in calificaciones['Materias'].values():
        suma += calificacion
    print(f"Su promedio es: {suma/materias:.2f}")


if __name__ == '__main__':
    texto = "¿Quiéres conocer tu promedio?."
    print()
    for letra in texto:
        print(colored(letra, 'green', attrs=['bold']), end=" ")
        sleep(.1)
    print()

    calificaciones = {'Nombre': " ",
                      'Materias': {'Estructura de Datos': 0, 'Derecho y Legislación': 0, 'Electronica II': 0,
                                   'Contabilidad': 0, 'Algebra': 0, 'Ingles': 0}}
    datos(calificaciones)