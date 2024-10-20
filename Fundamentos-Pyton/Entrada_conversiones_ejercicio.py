'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 19 de Octubre de 2024
Descripción:
 Pida los datos de los profesores utilizando nombres de variables adecuadas, la función input y el casting.
'''

Nombre = input("Ingrese su nombre: ")
No_de_cubiculo = int(input("Ingrese su número de cubículo: "))
Horas_clases_xsemana = float(input("Ingrese las horas que imparte clases por semana: "))
Años_unsij = input("¿Tiene más de 5 años en la UNSIJ?: ")
Años_unsij = Años_unsij.lower() == "si"
print()
print("Datos del profesor.")
print()
print(f"Nombre: {Nombre}")
print(f"Número de cubículo: {No_de_cubiculo}")
print(f"Horas que imparte clase a la semana: {(Horas_clases_xsemana):.3f}")
print(f"¿Tiene más de 5 años en la UNSIJ?: {Años_unsij}")