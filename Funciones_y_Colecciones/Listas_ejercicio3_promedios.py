'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 11 de noviembre de 2024
Descripción: Segundo ejercicio sobre listas.
'''

alumnos = [ ]
calificaciones = [ ]
materias = ['Estructura de Datos','Álgebra','Contabilidad','Electrónca II','Derecho y Legislación','Inglés']
def menu():
    print("1.- Ver calificaciones de todos los alumnos")
    print("2.- Ver calificaciones detalladas de un alumno")
    print("3.- Ver promedio del Primer parcial de todos los alumnos")
    print("4.- Ver promedio grupal")
    print("5.- Añadir alumno")
    print("6.- Eliminar alumno")
    print("0.- Salir")
    opcion = int(input("Elige una opción: "))
    print()
    return opcion

def calificaciones_todos(alumnos, calificaciones, contador_alumno):
    contador_alumno = 0
    if len(alumnos) == 0:
        print("No hay alumnos.")
    else:
        for alumno in (alumnos):
            print(f"{alumno}: {calificaciones[contador_alumno]}")
            contador_alumno += 1
    print()

def calificaciones_detalladas(alumnos, calificaciones, contador_alumno, materias):
    contador_alumno = 1
    if len(alumnos) == 0:
        print("Aún no hay alumnos.")
        return
    for alumno in alumnos:
        print(f"{contador_alumno}.- {alumno}")
        contador_alumno += 1
    numero_alumno = int(input("Ingrese el número del alumno que desea ver sus calificaciones: "))
    if numero_alumno>= 1 and numero_alumno <= len(alumnos):
        posicion = numero_alumno - 1
        print(f"Alumno: {alumnos[posicion]}")
        print("Clificaciones: ")
        for materia, calificacion in zip(materias, calificaciones[posicion]):
            print(f"{materia}: {(calificacion):.2f}")
        print()
    else:
        print("El alumno no existe")
    print()

def promedio_alumnos(alumnos, calificaciones, contador_alumno):
    promedios = [ ]
    if len(alumnos) == 0:
        print("Aún no hay alumnos.")
    else:
        for alumno, calificacion in zip(alumnos,calificaciones):
            promedios = (sum(calificacion)) / (len(calificacion))
            print(f"{alumno}: {(promedios):.2f}")
    print()

def promedio_grupal(calificaciones):
    if len(calificaciones) == 0:
        print("Aún no hay alumnos")
    else:
        total_calificaciones = 0
        total_materias = 0
        for calificacion in calificaciones:
            total_calificaciones += sum(calificacion)
            total_materias += len(calificacion)
        promedio_total = total_calificaciones / total_materias
        print(f"El promedio grupal es de: {(promedio_total):.2f}")
    print()

def nuevo_alumno(alumnos, calificaciones):
    alumno = input("Ingresa al nuevo alumno: ")
    alumnos.append(alumno)
    estructura_datos = float(input("Ingresa la calificación de la materia de Estrcutura de Datos: "))
    algebra = float(input("Ingresa la calificación de la materia de Álgebra: "))
    contabilidad = float(input("Ingresa la calificación de la materia de Contabilidad: "))
    electronicaII = float(input("Ingresa la calificación de la materia de Electrónica II: "))
    derecho_legislacion = float(input("Ingresa la calificación de la materia de Derecho y Legislación: "))
    ingles = float(input("Ingresa la calificación de la materia de Inglés: "))
    calificaciones.append([estructura_datos, algebra, contabilidad, electronicaII, derecho_legislacion, ingles])
    print()
    return calificaciones

def eliminar_alumno(alumnos, calificaciones, contador_alumno):
    contador_alumno = 1
    if len(alumnos) == 0:
        print("No hay alumnos para eliminar")
    else:
        for alumno in alumnos:
            print(f"{contador_alumno}.- {alumno}")
            contador_alumno += 1
        eliminar = int(input("Ingrese el número del alumno que desea eliminar: "))
        del alumnos[eliminar-1]
        del calificaciones[eliminar-1]
        contador_alumno -= 1
        print("El alumno y sus calificaciones se borraron correctamente.")
    print()


contador = 1
contador_alumno = 0
while contador != 0:
    opciones = menu()
    if opciones == 1:#Calificaciones de todos los alumnos
        calificaciones_todos(alumnos, calificaciones, contador_alumno)
    elif opciones == 2:#Calificaciones detalladas de un alumno
        calificaciones_detalladas(alumnos, calificaciones, contador_alumno, materias)
    elif opciones == 3:#Ver promedio de todos los alumnos
        promedio_alumnos(alumnos, calificaciones, contador_alumno)
    elif opciones == 4:#Promedio grupal
        promedio_grupal(calificaciones)
    elif opciones == 5:#Añadir alumno
        nuevo_alumno(alumnos, calificaciones)
        contador_alumno += 1
    elif opciones == 6:#Eliminar alumno
        eliminar_alumno(alumnos, calificaciones, contador_alumno)
    elif opciones == 0:#
        contador = 0
    else:
        print("Valor no válido.")