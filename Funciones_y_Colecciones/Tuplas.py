'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 19 de noviembre de 2024
Descripción: Tuplas.
'''

"""
Las tuplas son:
- Ordenadas
- Inmutables
- Los elementos se encierran entre paréntesis
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
print(f"{(sum(pi_serie[0: 1])):.4f}")
print(sum(pi_serie[0: 2]))
print(sum(pi_serie[0: 4]))
print(sum(pi_serie[0: 7]))
print(sum(pi_serie[0: 9]))
print(sum(pi_serie[0: 12]))

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