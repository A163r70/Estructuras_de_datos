'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 15 de Octubre de 2024
Descripción: Este programa determinará si una persona forma parte de la comunidad de la UNSIJ.

'''

print("*** Comunidad de la UNSIJ ***")
print()
profe = input("¿Es profesor de la UNSIJ?: ")
profe = profe.lower() == "si"
estudiante = input("¿Es estudiante de la UNSIJ?: ")
estudiante = estudiante.lower() == "si"

print(f"Forma parte de la UNSIJ?: {profe or estudiante}")