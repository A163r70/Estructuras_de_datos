'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 15 de Octubre de 2024
Descripción: Ejemplos del uso de los operadores de asignación.
'''

"""
En programación, las operaciones de asignación se utilizan para almacenar un valor en una variable. 
Es decir, se establece una relación entre un nombre (la variable) y un valor en la memoria de la computadora.
"""

# Asignación múltiple.
print("   ***   Asignación múltiple   ***")
nombre, primer_apellido, segundo_apellido = "alberto", "Martínez", "Barbosa"
print(f"Asignación múltiple de cadenas: {nombre} {primer_apellido} {segundo_apellido}")

entero1, entero2 = 1, 2
print(f"Asignación múltiple de enteros: {entero1} y {entero2}")
decimal1, decimal2, decimal3, decimal4 = 3.14, 3.1416, 3.14159, 3.141592
print(f"Asignación múltiple de decimales: {decimal1}, {decimal2}, {decimal3} y {decimal4}")
nombre, entero1, decimal4 = "Alberto", 12, 3.1415926            # Es posible combinar tipos de datos.
print(f"Asignación múltiple: {nombre}, {entero1} y {decimal4}")
suma, resta = entero1 + entero2, decimal1 - decimal2            # Es posible asignar distintas operaciones.
print(f"Asignaciones de operaciones: suma {suma} y resta {resta:.4f}")


# Asignación encadenada.
print()
print("   ***   Asignación encadenada   ***")
entero3 = entero4 = entero5 = 10    # Se les asigna el mismo valor a todas las variables.
print(f"Asignación encadenada de: {entero3} = {entero4} = {entero5} = 10")


# Intercambio de variables.
print()
print("   ***   Intercambio de variables   ***")
entero5, entero6 = 5, 6
print(f"Valores asignados: entero5 = {entero5} y entero6 = {entero6}")
entero6, entero5 = entero5, entero6
print(f"Valores intercambiados: entero5 = {entero5} y entero6 = {entero6}")

variable_prueba1, variable_prueba2 = 100, "Hola mundo"
variable_prueba1, variable_prueba2 = variable_prueba2, variable_prueba1 # Es posible porque las variables son dinámicas.
print(f"Valores asignados: variable_prueba1 = {variable_prueba1} y variable_prueba2 = {variable_prueba2}")
print(f"Valores intercambiados: variable_prueba1 = {variable_prueba1} y variable_prueba2 = {variable_prueba2}")