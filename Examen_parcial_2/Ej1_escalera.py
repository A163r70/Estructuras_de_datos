'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 06 de diciembre de 2024
Descripción: Primer ejercicio del examen del segundo parcial. En este programa mostramos en pantalla una escalera con
el número de escalones que el usuario ingrese, ya sean positivos o negativos. Si el número ingresado es positivo
la escalera se mostrará de forma ascendente, y si el número es negativo la escalera se mostrará en forma
descendente.
'''

def menu():
    print("*** Ejercicio 1. La escalera. ***")
    escalones = int(input("Ingresa el número de escalones (positivo - ascendente y negativo - descendente) o ingresa un cero para salir: "))
    return escalones#Le pedimos al usuario el número de escalones que desea que tenga la escalera y retornamos la respuesta.

def escalera():
    contador = 1
    while contador != 0:
#En una variable llamada escalones furadamos la respuesta del usuario
        escalones = menu()
#Si el número es positivo ejecutamos lo siguiente.
        if escalones > 0:
#Imprimimos primero la base del escalón.
            print(" " * escalones + "  _")
#En el siguiente for ejecutamos la lógica para construir la escalera.
            for f in range(0, escalones):
#Declaramos dos varibale los cuales seran la base y la altura del escalón.
                base = "_"
                altura = "|"
#Calculamos el total de espacios que tendrá
                espacio = " " * (escalones - f)
#Imprimimos el espacio, la base y después la altura
                print(f"{espacio}{base}{altura}")
            print("-------------------------------------")
#Si el número es negativo ejecutamos lo siguiente.
        elif escalones < 0:
#Convertimos el número negativo en positivo y hacemos lo mismo que en el primer caso.
            escalones = (escalones * -1)
            print("_")
            for l in range(0, escalones):
                base = "_"
                altura = "|"
                espacio = " " * (l + 1)
                print(f"{espacio}{altura}{base}")
            print("-----------------------------------")
        else:
            contador = 0

escalera()

