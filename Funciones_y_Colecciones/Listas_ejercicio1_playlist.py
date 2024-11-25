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
    print()
    return opcion

def ver_lista(videos_de_youtube, contador_videos):
    contador_videos = 1
    if len(videos_de_youtube) == 0:
        print("Aún no hay videos que mostrar.")
    else:
        for lista in videos_de_youtube:
            print(f"{contador_videos}.- {lista}")
            contador_videos +=1

def ordenAZ(videos_de_youtube):
    if len(videos_de_youtube) == 0:
        print("Aún no hay videos para acomodar.")
    else:
        videos_de_youtube.sort()
    return videos_de_youtube



def ordenZA(videos_de_youtube):
    if len(videos_de_youtube) == 0:
        print("Aún no hay videos para acomodar.")
    else:
        videos_de_youtube.sort(reverse=True)
    return videos_de_youtube

def agregar(videos_de_youtube):
    video_agregar = input("Ingresa el video a agregar: ")
    videos_de_youtube.append(video_agregar)
    print(f"El video ´{video_agregar}´ ah sido agregado correctamente.")
    print()
    return videos_de_youtube

def agregar_varios(videos_de_youtube, contador_videos):
    videos_agregar = int(input("Ingresa cuantos videos deseas agregar: "))
    for videos in range(videos_agregar):
        video = input("Ingresa el video: ")
        videos_de_youtube.append(video)
        contador_videos += 1
    print(f"{videos_agregar} videos han sido agregados correctamente.")
    print()
    return videos_de_youtube

def eliminar(videos_de_youtube, contador_videos):
    if len(videos_de_youtube) == 0:
        print("No hay videos para elimnar.")
    else:
        ver_lista(videos_de_youtube, contador_videos)
        eliminar = int(input("Ingresa el índice del video que desea eliminar: "))
        videos_de_youtube.pop(eliminar - 1)
        contador_videos -= 1
        print("El video ha sido eliminado correctamente.")
    print()
    return videos_de_youtube

final = 1
contador_videos = 0
while final != 0:
    opcion = menu()
    if opcion == 1:
        ver_lista(videos_de_youtube, contador_videos)
        print()
    elif opcion == 2:
        contador_videos = 0
        for lista in ordenAZ(videos_de_youtube):
            print(f"{contador_videos+1}.- {lista}")
            contador_videos +=1
        print()
    elif opcion == 3:
        contador_videos = 0
        for lista in ordenZA(videos_de_youtube):
            print(f"{contador_videos+1}.- {lista}")
            contador_videos +=1
        print()
    elif opcion == 4:
        agregar(videos_de_youtube)
        contador_videos +=1
    elif opcion == 5:
        agregar_varios(videos_de_youtube, contador_videos)
    elif opcion == 6:
        eliminar(videos_de_youtube, contador_videos)
    elif opcion == 0:
        final = 0
    else:
        print("Valor no válido.")