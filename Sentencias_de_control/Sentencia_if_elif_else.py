'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 23 de Octubre de 2024
Descripción: Operador lógico if elsif else

'''
# elif evalua una segunda condición.
#Depuramos

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
elif grupo_edad >60:
    print(f"Perteneces al grupo de adultos mayores.")
