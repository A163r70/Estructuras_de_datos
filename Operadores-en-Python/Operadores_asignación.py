'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 15 de Octubre de 2024
Descripción:

'''
print("Asignación múltiple")
variable_1,variable_2 = 5,10
variable_3, variable_4 = 9.14,"Compa Chay"
print(variable_1, variable_2, variable_3, variable_4)

variable_5, variable_6 = variable_1 + variable_2, variable_1 - variable_2
print(variable_5, variable_6)

print("Asignación encadenada")
variable_7=variable_8=variable_9=10
print(variable_7)

variable_10, variable_11="Alberto", "Geto"
print(variable_10, variable_11)
variable_11, variable_10=variable_10, variable_11
print(variable_10, variable_11)

nombre, apellido = input("Ingresa el nombre: "), input("Ingresa apellido: ")
print(nombre, apellido)