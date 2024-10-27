'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 15 de Octubre de 2024
Descripción: Ejemplos de los operadores de asignación compuesta.
'''

"""
Los operadores de asignación compuestos son una forma abreviada de realizar una operación aritmética y una asignación
en una sola línea de código. Combinan un operador aritmético (como suma, resta, multiplicación, división, etc.) 
con el operador de asignación (=).
"""

numero1, numero2 = int(input("Ingresa un número: ")), int(input("Ingresa otro número: "))
print(numero1, numero2)

numero1 +=3
print(numero1)
numero2 -=5
print(numero2)
numero1 *=2
print(numero1)
numero2 /=4
print(numero2)

numero3, numero4 = int(input("Ingresa un número: ")), int(input("Ingresa otro número: "))
print(numero3, numero4)
numero3+= numero4
print(numero3)
numero3 *= numero3
print(numero3)
numero3 -= numero4
print(numero3)
numero3 +=3
print(numero3)
numero3 /=2
print(numero3, numero4)
