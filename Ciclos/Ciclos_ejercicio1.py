'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 28 de Octubre de 2024
Descripción: Ciclo while.
'''


print("** Programa que calcula la suma acumulativa **")
numero_final = int(input("Ingresa hasta que número quiere sumar: "))
contador = 0
suma =0
while contador < numero_final:
    contador+=1
    suma += contador

print(f"La suma del 0 hasta el número {numero_final} es: {suma}")
