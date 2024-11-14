'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 11 de noviembre de 2024
Descripción: Segundo ejercicio sobre listas.
'''

alumnos = [ ]
esrtuctura_datos = [ ]
algebra = [ ]
contabilidad = [ ]
electronicaII = [ ]
derecho_legislacion = [ ]
ingles = [ ]

def menu():
    print("1.- Ver calificaciones de alumno")
    print("2.- Ver promedio de alumnos")
    print("3.- Añadir alumno")
    print("4.- Eliminar alumno")
    print("5.- Ver promedio grupal")
    print("0.- Salir")
    opcion = int(input("Elige una opción: "))
    print()
    return opcion

def ver_calificaciones(materias):
    numero_alumno = int(input("Ingrese el número del alumno que desea ver sus calificaciones: "))
    for i in materias:
        print(materias[1][numero_alumno])
    print()

def nuevo_alumno(alumnos):
    alumno = input("Ingresa al nuevo alumno: ")
    alumnos.append(alumno)
    calificacion_ed = int(input("Ingresa la calificación de la materia de Estrcutura de Datos: "))


contador = 1
contador_alumno = 0
while contador != 0:
    opciones = menu()
    if opciones == 1:
        ver_calificaciones(materias)
    elif opciones == 2:
        nuevo_alumno(alumnos)
        contador_alumno +=1
    elif opciones == 3:
        eliminar(nombre, cantidad, contador_productos)
    elif opciones == 0:
        contador = 0
    else:
        print("Valor no válido.")