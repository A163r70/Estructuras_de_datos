'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 26 de Octubre de 2024
Descripción: Este programa determinará cuál de dos números ingresados por el usuario es menor o si son iguales.
'''

decimal_1 = float(input("Ingresa un número decimal: "))
decimal_2 = float(input("Ingresa otro número decimal: "))
#Utilizamos la sentencia if-elif-else
if decimal_1 > decimal_2:
    print(f"El número {decimal_1} es mayor que el número {decimal_2}.")
elif decimal_1 < decimal_2:
    print(f"El número {decimal_2} es mayor que el número {decimal_1}.")
else:
    print(f"Los números {decimal_1} y {decimal_2} son iguales.")