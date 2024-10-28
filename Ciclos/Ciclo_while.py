'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 28 de Octubre de 2024
Descripción: Ciclo while.
'''
from operator import concat

print("** Programa que imprime un ejemplo de ciclo while **")
numero = int(input("Ingresa un número: "))
contador = 1
while contador < numero:
    print(f"{contador}")
    contador+= 1

print(f"Los número del 1 al {numero} son: {contador}")