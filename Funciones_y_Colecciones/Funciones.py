'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 11 de noviembre de 2024
Descripción: Funciones.
'''

"""
Una función en Python es un bloque de código reutilizable que se define una vez y se puede llamar múltiples veces a lo 
largo de tu programa.

¿Por qué usar funciones?
- Reutilización de código: Evita repetir el mismo código una y otra vez.
- Modularidad: Divide un programa grande en partes más pequeñas y manejables.
- Abstracción: Oculta la complejidad de ciertas tareas, enfocándose en el nivel más alto del programa.
- Legibilidad: Hace que el código sea más fácil de leer y entender.

Sintaxis para crear una función:

# Se utiliza la palabra reservada def, el nombre y los parámetros que recibe (opcionales)
def nombre_funcion(parametro1, parametro2, ...):       
    # Código que realiza la función.

    return variable # Variable que retorna la función (opcional).

# Código a nivel de módulo -> que es lo que conocemos como código principal. 
"""

def menu():
    print("0) Salir")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicación")
    print("4) División")
    print("5) División entera")
    print("6) Exponenciación")

def calculadora(opcion, numero1, numero2):
    if opcion == 1:
        resultado = numero1 + numero2
    elif opcion == 2:
        resultado = numero1 - numero2
    elif opcion == 3:
        resultado = numero1 * numero2
    elif opcion == 4:
        resultado = numero1 / numero2
    elif opcion == 5:
        resultado = numero1 // numero2
    elif opcion == 6:
        resultado = numero1 ** numero2
    return resultado

def hola(nombre):
    print(f"Hola {nombre}")

nombre = input("Ingresa tu nombre: ")
menu()
opcion = int(input("Escoga una opción: "))
numero1 = float(input("Ingrese un número: "))
numero2 = float(input("Ingrese otro número: "))
resultado = calculadora(opcion, numero1, numero2)
print(f"El resultado de la operación es: {(resultado):.3f}")
hola(nombre)
print("Adiós.")

""" Función que imprime el mensaje de "Hola mundo" """
# No recibe ni devuelve ningún valor.
def hola_mundo():
    print("Hola Mundo mediante una función.")


""" Función que imprime el mensaje de "Hola mundo" """
# Recibe el nombre que se imprime en consola y no devuelve ningún valor.
def hola(nombre):
    print(f"Hola {nombre} mediante una función.")


""" Función que regresa la suma de dos números  """
# Recibe los dos números que va a sumar y devuelve el resultado.
def suma(numero1, numero2):
    suma = numero1 + numero2
    return suma


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
# Primer ejemplo: no se utilizan parámetros, ni valores de retorno.
# Se imprime el mensaje de "Hola mundo" de la forma que se había manejado y mediante la función.
print("  ***  Primer ejemplo de uso de función  ***")
print("Hola mundo en el código a nivel de módulo.")
hola_mundo()    # Se llama a la función utilizando su nombre, en donde no tiene ningún parámetro a mandar.


# Segundo ejemplo: Se utiliza un parámetro, pero no hay valores de retorno.
# Se imprime un mensaje utilizando las dos formas:
print()
print("  ***  Segundo ejemplo de uso de función  ***")
nombre = input("Ingresa tu nombre: ").strip()   # strip() elimina espacios en blanco al inicio y final de una cadena.

print(f"Hola {nombre} en el código a nivel de módulo.")
hola(nombre)    # Ahora manda el parámetro del nombre a la función.


# Tercer ejemplo: Se utilizan dos parámetros y hay un valor de retorno.
# Se utiliza una operación matemática.
print()
print("  ***  Tercer ejemplo de uso de función  ***")
numero1 = float(input("Ingresa un número: ").strip())
numero2 = float(input("Ingresa otro número: ").strip())

print(f"La suma en el código a nivel de módulo es: {numero1 + numero2}")

suma = suma(numero1, numero2)   # El resultado de los dos parámetros se asigna a la variable 'suma'.
print(f"La suma mediante una función es: {suma}")


"""
   ***  MODO DEPURACIÓN  ****
Utilizar el modo depuración para observar el comportamiento de una función.
- Crear un punto de ruptura al imprimir el primer mensaje de "Hola" Mundo".
- Entrar al modo depuración.
- Observar la diferencia entre "Step over" y "Step into" en el menú de depuración.   
"""
