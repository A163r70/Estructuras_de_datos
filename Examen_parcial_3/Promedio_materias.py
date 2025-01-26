"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 24 de enero de 2025
Descripción: Programa que calcula el promedio de un alumno.
"""
from dataclasses import replace
from Buenas_prácticas.Especificar_datos_en_funciones import cadena_a_flotante

calificaciones = {'Nombre': " ", 'Materias':{'Estructura de Datos': 0, 'Derecho y Legislación': 0, 'Electronica II': 0,
                    'Contabilidad': 0, 'Algebra': 0, 'Ingles': 0}}

def datos(calificaciones)->None:
    nombre = input("Ingresa tu nombre: ")
    nombre = nombre.replace(" ", "_")
    while not nombre.isalpha():
        print("Valor no válido.")
        nombre = input("Intenta de nuevo: ")
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
    datos(calificaciones)