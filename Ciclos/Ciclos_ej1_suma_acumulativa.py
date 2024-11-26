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
"""
En el programa primero le pedimos al usuario un número mayor a 0 que sera el fin de la suma acumulativa. Creamos una
variable llamada contador y la inicializamos en 0. En el While la función de paro es cuando la variable contador
sea igaul al número ingresado por el usuario. Dentro del While el contador aumenta de uno en uno, después creamos otra
variable llamada suma, la cual almacenara la suma del valor del contador. Finalmente solo imprimimos la suma
acumulativa hasta el número ingresado por el usuario.
"""