'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 23 de Octubre de 2024
Descripción: Operador lógico if else.
'''
"""
La sentencia if-else es una estructura de control fundamental que permite tomar decisiones en el código.
Dependiendo de si se cumple una determinada condición, el programa tomará un camino u otro.

Sintaxis:

if condición:
    # Código a ejecutar si la condición es verdadera.

else:
    # Código a ejecutar si la condición es falsa.

# Código que se ejecuta sin importar la condición.
"""
print("*** Calcular si un número es par o impar ***")
numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")