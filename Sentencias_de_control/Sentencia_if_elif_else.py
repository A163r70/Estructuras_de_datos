'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 23 de Octubre de 2024
Descripción: Operador lógico if elsif else.
'''

#Depuramos

"""
La sentencia elif es una extensión del if-else y permite evaluar múltiples condiciones de forma secuencial. 
Es como tener varias opciones a elegir, ejecutándose el bloque de código correspondiente a la primera condición 
que sea verdadera.

Sintaxis:

if condicion_1:
    # Código a ejecutar si la condición_1 es verdadera.

elif condición_2:
    # Código a ejecutar si la condición_2 es verdadera.
  .
  .
  .
else:
    # Código que se ejecuta si todas las condiciones fueron falsas.
"""

print("Programa para determinar el grupo de edad del usuario")

grupo_edad = int(input("Ingresa tu edad: "))#marcar una línea se llama punto de ruptura
if grupo_edad <= 14:
    print(f"Perteneces al grupo de niños y adolescentes.")
elif grupo_edad >= 15 and grupo_edad <= 25:
    print(f"Perteneces al grupo de jóvenes.")
elif grupo_edad >=26 and grupo_edad <= 45:
    print(f"Perteneces al grupo de adultos jóvenes.")
elif grupo_edad >= 46 and grupo_edad <= 60:
    print(f"Perteneces al grupo de adultos maduros.")
else:
    print(f"Perteneces al grupo de adultos mayores.")

###############################################
"""
MODO DEPURACIÓN (DEBUG)

Utilizar ahora el modo depuración.
1) Crear un punto de ruptura en la variable edad. Marcar el número de línea y se pondrá un círculo color rojo.
2) Clic derecho y ejecutar el modo Debug.
3) Observar la nueva pantalla e ir ejecutando paso-a-paso (step over) F8.
4) Observar el comportamiento.
"""