"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 26 de Octubre de 2024
Descripción: Este programa mostrará los detalles del tour turístico Ecoturixtlán de acuerdo a las siguientes tarifas:

Precio de un adulto: $ 200.00
Precio de un niño: $ 100.00
Además, si la visita son los lunes, martes y jueves, se tiene un descuento del 10 %.
"""

print("*** Tour turístico Ecoturixtlán ***")
encargado = input("Ingrese el nombre del cliente: ")
adultos = int(input("Ingrese el total de adultos: "))
niños = int(input("Ingrese el total de niños: "))
dia_semana = input("Ingrese el día de la semana: ")

pago_niños = 100*niños
pago_adultos = 200*adultos
total = pago_niños+pago_adultos

if dia_semana == "lunes" or dia_semana == "martes" or dia_semana == "jueves":
    print(f"Gracias por tu visita {encargado} en este día {dia_semana}.")
    print(f"El costo toal es de ${(total)-(((total)*10)/100)}")
else:
    print(f"Gracias por tu visita {encargado} en este día {dia_semana}.")
    print(f"El costo total es de ${total}.")
