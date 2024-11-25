'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 28 de Octubre de 2024
Descripción: Ciclo while.
'''

print("** Programa que calcula la suma acmulativa entre 2 números **")
numero1 = int(input("Ingresa el núnmero inicial de la cuenta: "))
numero2 = int(input("Ingresa el número final de la cuenta: "))

suma = 0
while numero1 < numero2:
    numero1 += 1
    suma += numero1

print(f"La suma del número {numero1} hasta el número {numero2} es: {suma}")
"""
Este programa es parecido al anterior, con la diferencia de que en este solicitamos aparte del número en el que 
terminará la suma acumulativa, también pedimos desde que número quiere iniciar, así, empezamos a aumentar
solo la variable que guarda desde donde quiere iniciar, y el programa termina cuando el número de inicio sea igual al
número final.
"""