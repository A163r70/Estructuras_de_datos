'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 15 de Octubre de 2024
Descripción: Los operadores relacionales se utilizan para comparar dos valores

'''

cantidad_compra= int(input("¿De cuánto fué su compra?: "))
meses_sin_intereses = input("¿Su compra fue a meses sin intereses?: ")
meses_sin_intereses = meses_sin_intereses.lower() == "si"
print(f"¿Aplica para bonificación?: {cantidad_compra >= 5000 and meses_sin_intereses}")