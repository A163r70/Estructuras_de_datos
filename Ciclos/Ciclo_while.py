'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 28 de Octubre de 2024
Descripción: Ciclo while.
'''

"""
El ciclo while es una estructura de control fundamental en la programación que permite repetir un bloque de código 
mientras una determinada condición se evalúe como verdadera.

Sintaxis:

while condicion:
    # Código a ejecutar mientras la condición sea verdadera.

# Nota: No hay llaves, sino que se deja un espacio. 
"""

from operator import concat

print("** Programa que imprime un ejemplo de ciclo while **")
numero = int(input("Ingresa un número: "))
contador = 1
while contador < numero:
    print(f"{contador}")
    contador+= 1

print("Fin de la cuenta.")
print(f"Los número del 1 al {numero} son: {contador}")

"""
En el programa pedimos un número que será el final de los número que vamos a mostrar.
"""

# Otro ejemplo del ciclo while. Imprimir los números pares del 0 hasta el número ingresado pro consola.
print()
print("  ***  Otro ejemplo del ciclo while  ***")

numero = int(input("Ingresa otro número: "))

print()
print(f"Los números pares del 0 al {numero} son: ")

contador = 0
while contador <= numero:
    print(contador, end = " ")
    contador += 2

print("\nFin de la cuenta.")        # Notar la diferencia de este print() con el ejemplo anterior.

