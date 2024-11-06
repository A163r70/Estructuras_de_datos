'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 31 de Octubre de 2024
Descripción: Aprendemos a usar el ciclo for.
En Python ya no es necesario indicar de donde empezar y donde terminar.
'''


numero_caracteres = 0
cadena = input("Ingresa una cadena: ")
for caracter in cadena:
    numero_caracteres += 1
    print(caracter, end=" ""-")

print()
print(numero_caracteres)

alumnos = ["Rosalinda", "Juan", "Lourdes", "Tania", "Bryan", "Rebeca", "Jennifer", "Héctor", "Galilea", "Patricia", "Jesús", "Addi",]
for alumno in alumnos:
    print(f"Hola {alumno}.")

for i in range(1, 11):#para números ocupamos la función range(inicio, final -1)
    print(f"{i},", end="")