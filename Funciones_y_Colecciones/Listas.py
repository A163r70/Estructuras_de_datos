'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 11 de noviembre de 2024
Descripción: Listas.
'''
from turtledemo.sorting_animate import ssort

#Crear lista, ejemplo
#Fila, en Python sería FIFO (First input - First output)
#Pila, queue, LIFO: el último el entrar es el primero en salir

alumnos = [ ]

alumnos.append("Hector")
alumnos.append("Addi")
alumnos.append("Alberto")
alumnos.append("Juan")
print(alumnos)
#para insertar valores en un índice específico:
alumnos.insert(1, "Tania")
#mostrando todos los alumnos con un for.
for alumno in alumnos:
    print(alumno, end=" ")

#para eliminar en base al valor que pongamos.
alumnos.remove("Hector")
print()
print(alumnos)
#Eliminar por su índice.
alumnos.pop(2)
print(alumnos)
del alumnos[2]
print(alumnos)

#lista declarada
alumnos2 = ["Rosalinda", "Juan", "Lourdes", "Tania", "Bryan", "Rebeca", "Jennifer", "Héctor", "Galilea", "Patricia", "Jesús", "Addi",]
print(alumnos2)
print("len")
caracteres = len(alumnos2)
print(caracteres)
#Ordenar por orden alfabético.
alumnos2.sort()
print("sort")
print(alumnos2)
#Voltear la lista.
print("sort2")
alumnos2.sort(reverse=True)
print(alumnos2)

print(alumnos2[-1])

