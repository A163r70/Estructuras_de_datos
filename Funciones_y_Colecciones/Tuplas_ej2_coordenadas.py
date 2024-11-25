'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 22 de noviembre de 2024
Descripción: Ejemplo del uso de una tupla dentro de una función.
'''

coordenadas = [ ]

def menu():
    print("1.-Ver coordenadas almacenadas.")
    print("2.-Agregar coordenadas (x,y).")
    print("3.-Calcular la pendiente y la ecuación de la recta entre dos coordenadas.")
    print("4.-Eliminar coordenada (x,y).")
    print("0.-Salir.")
    opcion = int(input("Ingrese una opción: "))
    print()
    return opcion

def ver_coordenada(coordenadas, contador_coordenadas):
    contador_coordenadas = 1
    if len(coordenadas) == 0:
        print("No hay coordenadas.")
    else:
        for x,y in coordenadas:
            print(f"Coordenada {contador_coordenadas}: ({x,y})")
            contador_coordenadas += 1
    print()

def agregar_coordenadas(coordenadas):
    x = float(input("Ingresa el valor de la coordenada X: "))
    y = float(input("Ingresa el valor para la coordenada Y: "))
    coordenadas.append((x,y))
    print()
    return coordenadas

def calculos(coordenadas, contador_coordenadas):
    if len(coordenadas) < 2:
        print("Se necesitan dos pares de cóordenadas.")
    else:
        ver_coordenada(coordenadas, contador_coordenadas)
        par1 = int(input("Elija el índice de la primera coordenada: "))
        par2 = int(input("Elija el índice de la segunda coordenada: "))
        par1 -= 1
        par2 -= 1
        if par1 >=0 and par2 >= 0 and par1 <= len(coordenadas) and par2 <= len(coordenadas):
            x1,y1 = coordenadas[par1]
            x2,y2 = coordenadas[par2]
            m = (y2 - y1) / (x2 - x1)
            b = y1 - m * x1
            print(f"La pendiente entre las coordenadas {coordenadas[par1]} y {coordenadas[par2]} es: {(m):.2f}")
            print(f"La ecuación de la recta es y= {m}x + ({b})")
        else:
            print("Índice no válido.")
    print()

def eliminar_coordenada(coordenadas,  contador_coordenadas):
    if len(coordenadas) == 0:
        print("No hay coordenada para eliminar.")
    else:
        ver_coordenada(coordenadas, contador_coordenadas)
        eliminar = int(input("Escoga el índice de la coordenada a eliminar: "))
        if eliminar >= 0 and eliminar <= len(coordenadas):
            coordenadas.pop(eliminar-1)
            contador_coordenadas -= 1
            print("La coordenada se eliminó exitosamente.")
    print()
#m = (y2 - y1) / (x2 - x1) pendiente
#b = y1 - m * x1 ecuación de la recta
contador = 1
contador_coordenadas = 0
while contador != 0:
    opciones = menu()
    if opciones == 1: #Ver coordenadas
        ver_coordenada(coordenadas, contador_coordenadas)
    elif opciones == 2:#Agregar coordenadas
        agregar_coordenadas(coordenadas)
        contador_coordenadas += 1
    elif opciones == 3:#Calcula pendiente y ecuación de la recta
        calculos(coordenadas, contador_coordenadas)
    elif opciones == 4:#Eliminar coordenada
        eliminar_coordenada(coordenadas, contador_coordenadas)
    elif opciones == 0:#Salir
        contador = 0
    else:
        print("Valor no válido")