'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 28 de Octubre de 2024
Descripción: Ciclo while.
'''

print("Programa que imprime todos los números pares **")
final = int(input("Ingresa hasta que número par quiere imprimir: "))
pares = 2
while pares <= final:
    print(pares, end=" ")
    pares+=2

print()
print("Final del ciclo")