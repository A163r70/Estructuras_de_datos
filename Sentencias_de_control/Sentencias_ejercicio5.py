'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 26 de Octubre de 2024
Descripción: Este programa determinará el promedio de una materia e indicará si el alumno aprobó o no la materia.
'''

parcial_1 = float(input("Ingresa tu calificación del parcial 1: "))
parcial_2 = float(input("Ingresa tu calificación del parcial 2: "))
parcial_3 = float(input("Ingresa tu calificación del parcial 3: "))
ordinario = float(input("Ingresa tu calificación del ordinario: "))

calificacion_final = float(((parcial_1/6)+(parcial_2/6)+(parcial_3/6)+(ordinario/2)))
if calificacion_final >= 6.0:
    print(f"La calificación final es de {(calificacion_final):.1f}. ¡Felicidades! Aprobaste.")
else:
    print(f"La calificación final es de {(calificacion_final):.1f}. Lo siento, no aprobaste.")