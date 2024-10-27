'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 26 de Octubre de 2024
Descripción: Este programa determinará la estación del año de acuerdo al número de mes ingresado por el usuario.
'''
mes = int(input("Ingresa el número del mes en el que se encuentra: "))
if mes == 3 or mes == 4 or mes == 5:
    print("La estación es: Primavera.")
elif mes == 6 or mes == 7 or mes == 8:
    print("La estación es: Verano.")
elif mes == 9 or mes == 10 or mes == 11:
    print("La estación es: Otoño.")
elif mes == 12 or mes == 1 or mes == 2:
    print("La estación es: Invierno.")
else:
    print("Mes no existente.")