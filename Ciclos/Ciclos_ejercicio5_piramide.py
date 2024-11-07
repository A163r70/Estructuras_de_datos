'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 29 de Octubre de 2024
Descripción:
'''

filas = int(input("Ingrese cuantas filas tendrá la piramide: "))
final = filas
for k in range(1, filas+1):
    for l in range(1, k+1):
        print("*", end=" ")
    print()

print("+++++++++++++++++++++++")

for k in range(1, filas+1):
    for l in range(final):
        print("*", end=" ")
    print()
    final -= 1
print("+++++++++++++++++++++++")


for k in range(0, filas):
    asterisco = "*" * filas
    espacio = " " * k
    print(f"{espacio}{asterisco}", end=" ")
    filas -= 1
    print()


print("+++++++++++++++++++++++")