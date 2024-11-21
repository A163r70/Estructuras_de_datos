'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 19 de noviembre de 2024
Descripción: Tuplas.
'''

"""
Las tuplas sonuna colección ordenada e inmutable de elementos. 
Esto significa que:
- Ordenada: Los elementos se almacenan en un orden específico, y cada elemento tiene un índice asociado.
- Inmutable: Una vez creada, no se puede agregar, eliminar o cambiar elementos dentro de una tupla.
- Heterogénea: Una tupla puede contener elementos de diferentes tipos de datos.
- Los elementos se encierran entre paréntesis () y se separan por comas.
Aunque también el uso de los paréntesis es opcional.
"""

print("Ejemplo de tupla")
fechas_cumple = ('12-19', '12-27', '01-10', '10-18', '11-01', '09-30', '08-25', '01-06', '10-21', '04-11', '03-06')

print(f"Las fechas de cumpleaño son: {fechas_cumple}")
for fecha in fechas_cumple:
    print(f"Feliz cumple al: {fecha}", end=" ")

print(
    print("Serie de pi de Lebniz")
)

print("Serie de Leibniz")

pi_serie = (4, -4/3, 4/5, -4/7, 4/9, -4/11, 4/13, -4/15, 4/17, -4/19, 4/21, -4/23)
for pi in pi_serie:
    print(pi)
#Valor considerando tres elementos
#La fubción sum() suma los elementos del parámetro que recibe.
print(f"El número Pi considerando los primeros 3 elementos es: {(sum(pi_serie[0: 2])):.4f}")
print(f"El número Pi considerando los primeros 5 elementos es: {(sum(pi_serie[0: 4])):.4f}")
print(f"El número Pi considerando los primeros 7 elementos es: {(sum(pi_serie[0: 6])):.4f}")
print(f"El número Pi considerando los primeros 9 elementos es: {(sum(pi_serie[0: 8])):.4f}")
print(f"El número Pi considerando todos los elementos es: {(sum(pi_serie)):.4f}")


print()
print("Ejemplos con coordenadas")
punto1 = (1, 0)
punto2 = (5, 3)


print(f"Coordenadas en tuplas: {punto1} y {punto2}")
#Deseptaquetado de tuplas, asignamos los valores de las tuplas a variables
x1, y1 = punto1#el 1 se asigna a la varibale x1 y el 0 se asigna a y1
x2, y2 = punto2#Lo mismo sucede aquí

"""Expresión de la recta y= mx + b 
m = (y2 - y1)/(x2 - x1)
b = y1 - m*x1"""

m = (y2 - y1)/(x2 - x1)
b = y1 - m*x1

print(f"La expresión de la recta es y= {m}x + ({b})")