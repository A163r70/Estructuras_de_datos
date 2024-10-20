'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 19 de Octubre de 2024
Descripción:
Conversión de cadenas a int, float y boolean mediante la interacción con consola.
'''

# Comentar sobre las funciones anidadas.
#Le pedimos datos al usuario y los convertimos a sus respectivos tipoa de datos.
print("****   Datos de los alumnos    *****")
nombre = input("Ingresa el nombre: ")
semestre = int(input("Ingresa el no. de semestre: "))#De cadena a entero.
promedio = float(input("Ingresa el promedio: "))#De cadena decimal
es_mujer = input("¿Es mujer (Si/No)?: ")

# No es posible convertir directamente una cadena a un valor booleano.
# Por ello, utilizamos la misma variable, convertimos a  minúsculas con la función lower() y lo comparamos con la cadena "si".
es_mujer = es_mujer.lower() == "si"

# Se imprimen los datos del alumno.
# Comentar  qué es lo que realiza {promedio:.2f} probando con números diferentes.
#{promedio:.2f} hace que después del punto solo imprima dos dígitos.
print()
print(f"El alumno {nombre} cursa el {semestre} semestre con un promedio de {promedio:.2f}. Además, es mujer: {es_mujer}.")