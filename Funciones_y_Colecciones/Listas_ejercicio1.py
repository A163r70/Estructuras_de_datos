'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 11 de noviembre de 2024
Descripción: Ejercicio sobre listas.
'''

videos_de_youtube = [ ]

def menu():
    print("1.- Ver lista de videos por añadir")
    print("2.- Ver lista de videos por orden A-Z")
    print("3.- Ver lista por orden por orden Z-A")
    print("4.- Añadir video")
    print("5.- Añadir varios videos")
    print("6.- Eliminar video")
    print("0.- Salir")
    opcion = int(input("Elige una opción: "))

def ver_lista(videos_de_youtube):
    for lista in videos_de_youtube:
        print(lista, end=" ")

def ordenAZ(videos_de_youtube):
    videos_de_youtube.sort()
    return videos_de_youtube

def ordenZA(videos_de_youtube):
    videos_de_youtube.sort(reverse=True)
    return videos_de_youtube

def agregar(videos_de_youtube):
    videos_de_youtube.insert()
    return videos_de_youtube

def agregar_varios(videos_de_youtube):

    contador = 0
    while contador != videos:
        if videos_de_youtube[contador] == " ":


