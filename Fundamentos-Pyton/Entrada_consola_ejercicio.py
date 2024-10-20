'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 14 de Octubre de 2024
Descripción:
Con números pedidos al usuario realizamos las operaciones básicas.
'''

#Primero pedimos dos número y los convertimos a decimales.
numero_1 = float(input("Ingrese un número decimal: "))
numero_2 = float(input("Ingrese otro número decimal: "))
#Hacemos las operaciones básicas y las mostramos.
print(f"La suma del {numero_1} y el {numero_2} es: {numero_1 + numero_2}")
print(f"La resta del {numero_1} y el {numero_2} es: {numero_1 - numero_2}")
print(f"La multiplicación del {numero_1} y el {numero_2} es: {numero_1 * numero_2}")
print(f"La división del {numero_1} y el {numero_2} es: {(numero_1 / numero_2):.2f}")