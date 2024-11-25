'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 25 de noviembre de 2024
Descripción: Ejemplos de conjuntos.
'''

"""
Un conjunto es desordenado y mutables 
Sintáxis:
conjuntos y dirccionarios
{} diccionario vacío
"""
print("** Ejmemplos de uso de los conjuntos **")
#Conjunto vacío
conjunto_nombres = set( )
print(f"Conjunto vacío: {conjunto_nombres}")
print("********************************************")
print()
#Se añade valores al conjunto
conjunto_nombres.add("Rebeca")
conjunto_nombres.add("Juan")
conjunto_nombres.add("Bryan")
conjunto_nombres.add("Lourdes")
conjunto_nombres.add("Héctor")
conjunto_nombres.add("Tania")
conjunto_nombres.add("Marlene")
conjunto_nombres.add("Rosalinda")
conjunto_nombres.add("Galilea")
conjunto_nombres.add("Patricia")
conjunto_nombres.add("Addi")
conjunto_nombres.add("Alberto")
print(f"Conjunto 303: {conjunto_nombres}")

print("********************************************")
print()
#Añadiendo elementos repetidos
conjunto_nombres.add("Rebeca")
conjunto_nombres.add("Bryan")
conjunto_nombres.add("Lourdes")
conjunto_nombres.add("Héctor")
conjunto_nombres.add("Tania")
conjunto_nombres.add("Marlene")
conjunto_nombres.add("Alberto")
conjunto_nombres.add("Alberto")
conjunto_nombres.add("Galilea")
conjunto_nombres.add("Patricia")
conjunto_nombres.add("Addi")
conjunto_nombres.add("Alberto")
print(f"Conjunto 303: {conjunto_nombres}")
print("********************************************")
print()
#Eliminar un elementos de un conjunto
conjunto_nombres.remove("Juan")
print(conjunto_nombres)
print("********************************************")
print()
#Imprimir todos en un for
for nombre in conjunto_nombres:
    print(f"Hola {nombre}", end=" ")
print("********************************************")
print()
#Verificar si un elemento existente pertenece a un conjunto
print(f"El elemento Alberto pertenece al conjunto?: {"Alberto" in conjunto_nombres}")
#Verificar si un elemento no existente pertenece a un conjunto
print(f"El elemento Alberto pertenece al conjunto?: {"Juan" in conjunto_nombres}")
print("********************************************")
print()
numeros = {12.3, 4.2, 8.9, 0.5}
#Funciones básicas
#Tamaño del conjunto
len(numeros)
#Suma de todos los elementos
sum(numeros)

