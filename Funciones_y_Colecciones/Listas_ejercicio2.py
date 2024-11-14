'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 11 de noviembre de 2024
Descripción: Segundo ejercicio sobre listas.
'''

nombre = [ ]
cantidad = [ ]

def menu():
    print("1.- Ver lista")
    print("2.- Añadir producto a la lista")
    print("3.- Eliminar producto de la lista")
    print("0.- Salir")
    opcion = int(input("Elige una opción: "))
    print()
    return opcion

def ver_lista(nombre, cantidad):
    for lista in nombre:
        print(lista, end=" ")
    print()
    for lista2 in cantidad:
        print(lista2, end=" ")
    print()

def agregar(nombre, cantidad):
    producto = input("Ingresa el producto que desea agrear: ")
    tanto = input("Ingresa la cantidad del producto que desea agruegar: ")
    nombre.append(producto)
    cantidad.append(tanto)
    print()
    return nombre, cantidad

def eliminar(nombre, cantidad, contador_productos):
    eliminar = int(input("Ingresa el índice del producto que desea eliminar: "))
    nombre.pop(eliminar-1)
    cantidad.pop(eliminar-1)
    contador_productos -=1

contador = 1
contador_productos = 0
while contador != 0:
    opciones = menu()
    if opciones == 1:
        ver_lista(nombre, cantidad)
    elif opciones == 2:
        agregar(nombre, cantidad)
        contador_productos +=1
    elif opciones == 3:
        eliminar(nombre, cantidad, contador_productos)
    elif opciones == 0:
        contador = 0
    else:
        print("Valor no válido.")