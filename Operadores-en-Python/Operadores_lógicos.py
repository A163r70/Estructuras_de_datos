'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 15 de Octubre de 2024
Descripción: Los operadores relacionales se utilizan para comparar dos valores

'''
expresion1, expresion2 = input("Ingresa (Si/No): "), input("Ingresa otro (Si/No): ")
expresion1 = expresion1.lower() == "si"
expresion2 = expresion2.lower() == "si"

print(expresion1)
print(expresion2)

print(f"¿Ambos fueron sí?: {expresion1 and expresion2}")
print(f"¿Ambos fueron diferentes?: {expresion1 or expresion2}")
print(f"La primera respuesta negada es: {not expresion1}")
print(f"La segunda respuesta negada es: {not expresion2}")