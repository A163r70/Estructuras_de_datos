'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 23 de noviembre de 2024
Descripción: .
'''

equipos = [ ]
def menu():
    print("1.- Ver equipos.")
    print("2.- Agregar equipo.")
    print("3.- Dterminar rol de juegos.")
    print("4.- Eliminar equipo.")
    print("0.- Salir.")
    opcion = int(input("Ingrese una opción: "))
    print()
    return opcion

def ver_equipos(equipos):
    if len(equipos) == 0:
        print("Aún no hay equipos.")
    else:
        contador = 1
        print("Los equipos participantes son:")
        for equipo in equipos:
            print(f"Equipo {contador}: {equipo}")
            contador += 1
    print()

def agregar_equipo(equipos):
    equipo = input("Ingresa el nombre del equipo: ")
    equipos.append(equipo)
    print(f"Equipo '{equipo}' agregado correctamente.")
    print()
    return equipos

def rol_juego(equipos, contador_equipos):
    if len(equipos) == 0:
        print("No hay equipos.")
    elif len(equipos) < 2:
        print("Se necesitan al menos dos equipos.")
    else:
        partidos = [ ]
        for i in range(len(equipos)):
            for j in range(i+1,len(equipos)):
                partidos.append((equipos[i], equipos[j]))
        print("El rol de partidos queda de la siguiente manera:")
        contador_equipos = 1
        for i in range(len(equipos)):
            for j in range(i+1,len(equipos)):
                print(f"Partido {contador_equipos}: {equipos[i]} vs {equipos[j]}")
                contador_equipos += 1
    print()

def eliminar(equipos, contador_equipos):
    if len(equipos) == 0:
        print("No hay equipos para eliminar.")
    else:
        ver_equipos(equipos)
        eliminar = int(input("Ingrese el índice del equipo que quiere eliminar: "))
        del equipos[eliminar-1]
        contador_equipos -= 1
    print()
    return equipos


contador = 1
contador_equipos = 0
while contador != 0:
    opciones = menu()
    if opciones == 1:#Ver equipos
        ver_equipos(equipos)
    elif opciones == 2:#Agregar nuevo equipo
        agregar_equipo(equipos)
        contador_equipos += 1
    elif opciones == 3:#Rol de juegos
        rol_juego(equipos, contador_equipos)
    elif opciones == 4:#Eliminar equipo
        eliminar(equipos, contador_equipos)
    elif opciones == 0:#Salir
        contador = 0
    else:
        print("Valor no válido.")
