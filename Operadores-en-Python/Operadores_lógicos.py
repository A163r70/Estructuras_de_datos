'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 15 de Octubre de 2024
Descripción: Los operadores relacionales se utilizan para comparar dos valores

'''

"""
Los operadores lógicos permiten combinar expresiones booleanas (verdadero o falso) para crear condiciones más complejas.
Estos operadores nos permiten realizar operaciones lógicas como "y", "o" y "no", lo que nos da la capacidad de tomar 
decisiones más sofisticadas dentro de nuestros programas.
"""

# Solicitamos por consola que se ingresen dos valores (Si/No) para covnertirlas a expresiones booleanas.
expresion1, expresion2 = input("Ingresa (Si/No): "), input("Ingresa otro (Si/No): ")
#Las convertimos a expresiones booleanas.
expresion1 = expresion1.lower() == "si"
expresion2 = expresion2.lower() == "si"

print(expresion1)
print(expresion2)

#Imprimimos mensajes sobre las operaciones lógicas.
print(f"¿Ambos fueron sí?: {expresion1 and expresion2}")
print(f"¿Ambos fueron diferentes?: {expresion1 or expresion2}")
print(f"La primera respuesta negada es: {not expresion1}")
print(f"La segunda respuesta negada es: {not expresion2}")