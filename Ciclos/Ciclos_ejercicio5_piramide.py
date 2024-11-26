'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 29 de Octubre de 2024
Descripción: Ejercicios con for.
'''

filas = int(input("Ingrese cuantas filas tendrá la piramide: "))
final = filas
print("Forma 1")
for k in range(1, filas+1):
    for l in range(1, k+1):
        print("*", end=" ")
    print()

print("+++++++++++++++++++++++")

print()
print("Forma 2")
for k in range(1, filas+1):
    for l in range(final):
        print("*", end=" ")
    print()
    final -= 1
print("+++++++++++++++++++++++")

print()
print("Forma 3")
limite = filas
for k in range(0, limite):
    asterisco = "*" * limite
    espacio = " " * k
    print(f"{espacio}{asterisco}", end=" ")
    limite -= 1
    print()


print("+++++++++++++++++++++++")

print()
print("Forma 4")
for k in range(0, filas):
    asteriscos = "*" * (2 * k + 1)
    espacios = " " * (filas - k - 1)
    print(f"{espacios}{asteriscos}")

"""
En este programa se ralizó el uso del for para imprimir una serie de asteríscos en distintas formas. Solo le pedimos al
usuario el número de filas que tendrán las pirámides.
"""