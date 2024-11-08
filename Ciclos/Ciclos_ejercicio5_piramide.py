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

limite = filas
for k in range(0, limite):
    asterisco = "*" * limite
    espacio = " " * k
    print(f"{espacio}{asterisco}", end=" ")
    limite -= 1
    print()


print("+++++++++++++++++++++++")

for k in range(0, filas):
    asteriscos = "*" * (2 * k + 1)
    espacios = " " * (filas - k - 1)
    print(f"{espacios}{asteriscos}")