'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 11 de noviembre de 2024
Descripción: Segundo ejercicio sobre listas.
'''

productos = [ ]

def menu():
    print("1.- Ver lista")
    print("2.- Añadir producto a la lista")
    print("3.- Eliminar producto de la lista")
    print("0.- Salir")
    opcion = int(input("Elige una opción: "))
    print()
    return opcion
#prodtuco = (nombre, cantidad)
#lista_prpductos.append(producto)
def ver_lista(productos, contador_productos):
    contador_productos = 1
    if len(productos) == 0:
        print("Aún no hay productos.")
    else:
        print("Productos y Cantidades")
        for nombre, cantidad in productos:
            print(f"{contador_productos}.- {nombre}... {cantidad}")
            contador_productos += 1
    print()

def agregar(productos):
    nombre = input("Ingresa el producto que desea agrear: ")
    cantidad = int(input("Ingresa la cantidad del producto que desea agruegar: "))
    productos.append((nombre, cantidad))
    print()
    return productos

def eliminar(productos, contador_productos):
    if len(productos) == 0:
        print("Aún no hay productos.")
    else:
        ver_lista(productos, contador_productos)
        eliminar = int(input("Ingresa el índice del producto que desea eliminar: "))
        productos.pop(eliminar-1)
        contador_productos -=1
        print(f"Producto eliminado correctamente.")
    print()

contador = 1
contador_productos = 0
while contador != 0:
    opciones = menu()
    if opciones == 1:
        ver_lista(productos, contador_productos)
    elif opciones == 2:
        agregar(productos)
        contador_productos +=1
    elif opciones == 3:
        eliminar(productos, contador_productos)
    elif opciones == 0:
        contador = 0
    else:
        print("Valor no válido.")
