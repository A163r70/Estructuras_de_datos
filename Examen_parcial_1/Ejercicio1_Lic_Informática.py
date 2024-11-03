'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 31 de Octubre de 2024
Descripción: Ejercico 1 del examen parcial.
Este programa imprime en consola los números, separados por comas, del 1 hasta un número ingresado por el usuario.

Sin embargo, se deben sustituir los siguientes valores:

3 o sus múltiplos por la palabra "Licenciatura".
5 y sus múltiplos por la palabra "Informática".
Múltiplos de 3 y 5 por la frase "Licenciatura en Informática" y se imprima un salto de línea en lugar de la coma.
'''

print("** Licenciatura en Informática **")
final = int(input("Ingrese el número final de la cuenta: "))#Le pedimos un número alususario y lo convertimos a entero.
Contador = 1#Iniciamos una variable llamado Contador en 1.
while Contador <= final:#Iniciamos el while con la condición de ejecutarse mientras sea menor o igual al número que el usuario ingresó.
    if Contador %3 == 0 and Contador %5 == 0:#Si el Contador es múltiplo del 3 y del 5 a la vez impimimios "Licenciatura en Informática".
        print("Licenciatura en Informática\n")
    elif Contador %3 == 0:#Si el Contador solo es múltiplo de 3 el programa imprime el mensaje "Licenciatura".
        print("Licenciatura,", end=" ")
    elif Contador %5 == 0:#Si el Contador es múltiplo de 5 el programa imprime el mensaje "Informática".
        print("Informática,", end=" ")
    else:
        print(f"{Contador},", end=" ")#Si el Contador no es múltiplo de 3 ni de 5, solo imprime en pantalla el número que sigue.
    Contador += 1#Aumentamos contador de 1 en 1.