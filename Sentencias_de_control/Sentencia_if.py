'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 23 de Octubre de 2024
Descripción: Operador lógico IF.
'''
"""
La sentencia de control if es una estructura de control fundamental que permite ejecutar diferentes bloques de código
 dependiendo de si una condición se cumple o no.

Sintaxis:

if condición:
    # Código a ejecutar si la condición es verdadera. Notar que hay que dejar un espacio de tabulador.

# Código que se continúa ejecutando. Notar que ya no hay espacio y está a la misma altura que el if.
"""

print("Programa para determinar si el ususario es mayor de edad")

edad = int(input("Escribe tu edad actual: "))
if edad >= 18:
    print("Eres mayor de edad")

print(f"tu edad es de {edad}")
# Probar qué pasa con espacios simples, no dejando una línea entre ambas funciones print()
# y que ambos print() se encuentren a la misma altura.

"""
Sí no dejamos una línea de espacio entre los if, y con un espacio normal en el segundo print como en el suguiente caso:
if condición:
    print()
 print()
Nos marca como error.
Si ponemos ambos print a la misma altura ambos se toman como parte del if.
"""



