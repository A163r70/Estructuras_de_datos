'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 15 de Octubre de 2024
Descripción: Realizamos las operaciones aritméticas básicas con dos números.

'''

"""
Los operadores aritméticos en Python son los siguientes:
- Suma (+).
- Resta (-).
- Multiplicación (*).
- División (/).
- División entera (//).
- Módulo (%).
- Exponenciación (**).
"""

#Se le solicitan dos número al usuario.
numero_1 = int(input("Ingresa un número: "))
numero_2 = int(input("Ingresa otro núnero: "))

#Realizamos las operaciones aritméticas.
print(f"La suma del {numero_1} y el {numero_2} es: {numero_1 + numero_2}")
print(f"La resta del {numero_1} y el {numero_2} es: {numero_1 - numero_2}")
print(f"La multiplicación del {numero_1} con el {numero_2} es: {numero_1 * numero_2}")
print(f"La división del {numero_1} con el {numero_2} es: {(numero_1 / numero_2):.2f}")
print(f"La división entera del {numero_1} con el {numero_2} es: {numero_1 // numero_2}")
print(f"La exponenciación del {numero_1} con el {numero_2} es: {numero_1 ** numero_2}")
print(f"El módulo del {numero_1} con el {numero_2} es: {numero_1 % numero_2}")
#los ** eleva el primer número a la potencia del segundo número.