'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 15 de Octubre de 2024
Descripción: Los operadores relacionales se utilizan para comparar dos valores

'''

numero1, numero2 = float(input("Ingresa un número decimal: ")), float(input("Ingresa otro número decimal: "))
print(numero1, numero2)

print(f"¿El primer número {(numero1):.2f} es mayor que {(numero2):.2f}? {numero1>numero2}")
print(f"¿El primer número {(numero1):.2f} es mayor o igual al número {(numero2):.2f}? {numero1 >= numero2}")
print(f"¿Los números {(numero1):.2f} y {(numero2):.2f} son iguales? {numero1 == numero2}")
print(f"¿El primer número {(numero1):.2f} es menor que el número {(numero2):.2f}? {numero1 < numero2}")
print(f"¿El primer número {(numero1):.2f} es menor o igual al número {(numero2):.2f}? {numero1 <= numero2}")
print(f"¿Los números {(numero1):.2f} y {(numero2):.2f} son diferentes? {numero1 != numero2}")