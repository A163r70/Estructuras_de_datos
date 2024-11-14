'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 11 de noviembre de 2024
Descripción: Segundo ejercicio sobre listas.
'''

alumnos = [ ]
estructura_datos = [ ]
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

def ver_calificaciones(estructura_datos, algebra, contabilidad, electronicaII, derecho_legislacion, ingles):
    numero_alumno = int(input("Ingrese el número del alumno que desea ver sus calificaciones: "))
    print()
    print(f"Alumno: {alumnos[numero_alumno]}")
    print(f"Estrucutura de Datos: {estructura_datos[numero_alumno]}")
    print(f"Álgebra: {algebra[numero_alumno]}")
    print(f"Contabilidad: {contabilidad[numero_alumno]}")
    print(f"Electrónica II: {electronicaII[numero_alumno]}")
    print(f"Derecho y Legislación: {derecho_legislacion[numero_alumno]}")
    print(f"Inglés: {ingles[numero_alumno]}")
    print()

def promedio_alumno(alumnos, estructura_datos, algebra, contabilidad, electronicaII, derecho_legislacion, ingles):
    promedios = [ ]
    for i in estructura_datos:
        promedios[i] = estructura_datos[i]+algebra[i]+contabilidad[i]+electronicaII[i]+derecho_legislacion[i]+ingles[i]
    for j in alumnos:
        print(f"Alumo {j}: {promedios}")


def nuevo_alumno(alumnos):
    alumno = input("Ingresa al nuevo alumno: ")
    alumnos.append(alumno)
    calificacion_ed = float(input("Ingresa la calificación de la materia de Estrcutura de Datos: "))
    calificacion_al = float(input("Ingresa la calificación de la materia de Álgebra: "))
    calificacion_conta = float(input("Ingresa la calificación de la materia de Contabilidad: "))
    calificacion_elec = float(input("Ingresa la calificación de la materia de Electrónica II: "))
    calificacion_derecho = float(input("Ingresa la calificación de la materia de Derecho y Legislación: "))
    calificacion_ingles = float(input("Ingresa la calificación de la materia de Inglés: "))
    estructura_datos.append(calificacion_ed)
    algebra.append(calificacion_al)
    contabilidad.append(calificacion_conta)
    electronicaII.append(calificacion_elec)
    derecho_legislacion.append(calificacion_derecho)
    ingles.append(calificacion_ingles)

contador = 1
contador_alumno = 0
while contador != 0:
    opciones = menu()
    if opciones == 1:#Ver calififcaiones
        ver_calificaciones(estructura_datos, algebra, contabilidad, electronicaII, derecho_legislacion, ingles)
    elif opciones == 2:#Ver promedio de alumnos
        promedio_alumno(alumnos, estructura_datos, algebra, contabilidad, electronicaII, derecho_legislacion, ingles)
    elif opciones == 3:#Agregar nuevo alumno
        nuevo_alumno(alumnos)
        contador_alumno += 1
    elif opciones == 4:#Eliminar un alumno
        print("En proceso")
    elif opciones == 3:#Promedio grupal
        print("En proceso")
    elif opciones == 0:#
        contador = 0
    else:
        print("Valor no válido.")