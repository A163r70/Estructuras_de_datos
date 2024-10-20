'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 14 de Octubre de 2024
Descripción:
Entrada de datos por consola para interacturar con el usuario con valores dinámicos.
'''

# Comentar sobre la función input.
# input la utilizamos para leer una entrada de texto desde la consola o terminal. Cuando la llamamos el programa se espera
# para que el usuario escriba algo, luego, el texto introducido la almacenamos en una variable y se devuelve como una cadena.
# Pedimos dos números al usuario por consola y las almacenamos en diferentes variables.
numero1_cadena = input("Introduce un número decimal: ") # Lo que introduzca el usuario se guradará como una cadena.
numero2_cadena = input("Introduce otro número decimal: ")
# La siguiente instrucción trata de sumar los número que el usuario ingreso, sin embargo como están guradadas como cadenas,
# no se puede realizar correctamente la operación.
resultado_cadena = numero1_cadena + numero2_cadena # Verificar qué es lo que realiza esta instrucción (ver el print).
print()
print(" ****  Recibir número sin un casting de varibles  ****")
# Al imprimir el resultado de la operación solo nos mostrará las cadenas concatenadas.
print(f"El resultado de {numero1_cadena} y {numero2_cadena} es: {resultado_cadena}")

nose_float = float(input("Ingresa un número: "))#Funciones anidadas

# Comentar por qué se realiza el casting de variables.
numero1_float = float(numero1_cadena)#El número ingresado por el usuario lo convertimos a decimal y lo almacenamos en otra variable.
numero2_float = float(numero2_cadena)
# Realizamos la operación deseada, y en este caso se puede realizar correctamente ya que ahora los número ya son decimales y no cadenas.
resultado_float = numero1_float + numero2_float # Verificar qué es lo que realiza de esta manera y compáralo.
print()
print(" ****  Casting de varibles  ****")
# Al imprimir, se imprimirá la suma de los números y no los concatenará.
print(f"El resultado de {numero1_float} y {numero2_float} es: {resultado_float}")
#lower = convertir toda la cadena a minúsculas


