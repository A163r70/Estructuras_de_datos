'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 22 de noviembre de 2024
Descripción: Ejemplo del uso de una tupla dentro de una función.
'''

numeros = [ ]

def menu():
    print("1.- Ver lista de números")
    print("2.- Añadir número a la lista")
    print("3.- Determinar el valor máximo y mínimo de la lista de números.")
    print("0.- Salir")
    opcion = int(input("Ingrese una opción: "))
    print()
    return opcion


def ver_lista(numeros):
    if len(numeros) == 0:
        print("No hay números.")
    else:
        print(numeros)
    print()

def agregar_numero(numeros):
    numero_nuevo = float(input("Ingresa el número nuevo: "))
    numeros.append(numero_nuevo)
    print()

def maximo_minimo(numeros):
    if len(numeros) == 0:
        return ()

    mayor = numeros[0]
    menor = numeros[0]
    for numero in numeros:
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
    print()
    return (mayor, menor)

def mostrar(numeros):
    resultado = maximo_minimo(numeros)
    if len(resultado) == 0:
        print("No hay números")
    else:
        print(f"El número máximo de la lista es: {resultado[0]}")
        print(f"El número mínimo de la lista es: {resultado[1]}")
    print()

contador = 1
while contador != 0:
    opciones = menu()
    if opciones == 1: #Ver lista de números
        ver_lista(numeros)
    elif opciones == 2:#Añadir números
        agregar_numero(numeros)
    elif opciones == 3:#Determinar máximo y mínimo
        mostrar(numeros)
    elif opciones == 0:
        contador = 0
    else:
        print("Valor no válido")

"""
En este programa determinamos el número más grande y el número más pequeño de una lista de números que el usuario nos
proporciona, para devolver en una tupla los números máximo y mínimo. Si la lista no tiene nada, retornamos una tupla 
vacía, pero si contiene algo, devolvemos los números mayor y menor, el cual almacenamos en una tupla que mostramos.
"""