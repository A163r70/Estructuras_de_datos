'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 20 de noviembre de 2024
Descripción: Tuplas con funciones.
'''

print("** Clificaciones del parcial 1 **")
def calificacion(calificaciones):
    promedio_parcial = sum(calificaciones[0,2]/3 + calificaciones[3]/2)
    promedio_final =(promedio_parcial + calificaciones[0,2])/2
    tupla_promedios = (promedio_parcial, promedio_final)
    return tupla_promedios

parcial_1 = float(input("Ingresa la calificación del primer parcial: "))
parcial_2 = float(input("Ingresa la calificación del segundo parcial: "))
parcial_3 = float(input("Ingresa la calificación del tercer parcial: "))
ordinario = float(input("Ingresa la calificación del  ordinario: "))

calificaciones = (parcial_1, parcial_2, parcial_3, ordinario)
promedios = calificacion(calificaciones)
print(f"El promedio parcial es: {promedios[0]}", end=" ")
print(f"El promedio final es de: {promedios[1]}")