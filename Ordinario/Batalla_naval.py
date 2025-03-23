import random

def menu()->int:
    """
    Menú donde eliges si jugar contra otro amigo o contra la CPU.
    :return:
    """
    print("*** Batalla Naval ***")
    print("1.- Uno vs Uno.")
    print("2.- Uno vs CPU.")
    print("0.- Salir.")
    opcion = input("Elige una opción: ")
    while not opcion.isnumeric():
        print("Opción no válida")
        opcion = input("Intenta nuevamente: ")
    opcion = int(opcion)
    print()
    return opcion

def imprimir_tablero(tablero_jugador, tablero_ataque)->None:
    """
    Función que muestra los tableros de juego.
    :param tablero_jugador: El tablero donde estan los barcos del jugador.
    :param tablero_ataque: Tablero donde registra los ataques hacia el enemigo.
    :return:
    """
    print("Tablero del jugador.")
    print("    1   2   3   4   5   6   7   8   9   10")
    for fila in tablero_jugador:
        print(fila[0], "|", fila[1], "|", fila[2], "|", fila[3], "|", fila[4], "|", fila[5], "|", fila[6], "|",
              fila[7], "|", fila[8], "|", fila[9], "|")
        print("  -----------------------------------------")

    print("Tablero de ataque.")
    print("    1   2   3   4   5   6   7   8   9   10")
    for fila in tablero_ataque:
        print(fila[0], "|", fila[1], "|", fila[2], "|", fila[3], "|", fila[4], "|", fila[5], "|", fila[6], "|",
              fila[7], "|", fila[8], "|", fila[9], "|")
        print("  -----------------------------------------")

def colocar_barcos(tablero_jugador,cantidad_barcos, ataques)->None:
    """
    Función que pide la posición en donde estarán los barcos.
    :param tablero_jugador: Tbalero del jugador o del oponente.
    :param cantidad_barcos: La cantidad de barcos con los que jugaran.
    :param ataques: El tablero de ataques.
    :return:
    """
    letra_a_numero = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}
    for i in range(1,cantidad_barcos+1):
        while True:
            fila = input(f"Ingresa la fila donde colocará el barco {i} (A-J): ")
            while not fila in letra_a_numero:
                fila = input("Fila no válida. Ingresa una letra de A a J: ").lower()
            fila_numero = letra_a_numero[fila]

            columna = input(f"Ingresa la columna donde colocará el barco {i} (0-9): ")
            while not columna.isnumeric():
                columna = input("Ingresa números: ")
            columna = int(columna)

            orientacion = input(f"El barco {i} será horizontal (H) o vertical (V): ")
            orientacion = orientacion.lower()
            while orientacion != 'h' and orientacion != 'v':
                    orientacion = input("Valor no válido. Intenta nuevamente: ").lower()
            if verificar_colocacion(tablero_jugador,fila_numero,columna,orientacion,i):
                posicionar_barco(tablero_jugador,fila_numero,columna,orientacion,i)
                imprimir_tablero(tablero_jugador,ataques)
                break
            else:
                print("La posición esta ocupada o fuera de rango.")

def colocar_barcos_cpu(tablero_cpu, cantidad_barcos,ataques)->None:
    """
    Función que verifica donde pondra la CPU sus barcos.
    :param tablero_cpu: Tablero de la cpu.
    :param cantidad_barcos: Cantidad de barcos con los que jugaran.
    :param ataques: Tablero de ataques.
    :return:
    """
    for i in range(1,cantidad_barcos+1):
        while True:
            fila = random.randint(0, 9)
            columna = random.randint(0,9)
            orientacion = random.randint(0,1)
            if orientacion == 0:
                orientacion = 'h'
            else:
                orientacion = 'v'

            if verificar_colocacion(tablero_cpu,fila,columna,orientacion,i):
                posicionar_barco(tablero_cpu,fila,columna,orientacion,i)
                imprimir_tablero(tablero_cpu,ataques)
                break
            else:
                print("La posición esta ocupada o fuera de rango.")

def verificar_colocacion(tablero,x:int,y:int,orientacion:str,size:int)->bool:
    """
    Función que verifica si el barco esta dentro del rango del tablero.
    :param tablero: Tablero de juego.
    :param x: Filas del tablero.
    :param y: Columnas del tablero.
    :param orientacion: La orientación del barco (horizontal o vertical).
    :param size: Tamaño de los barcos.
    :return:
    """
    if not(0<=x<10 and 0<=y<10):
        return False

    if orientacion == 'h':
        if y + size > 10:
            return False
        for i in range(size):
            if tablero[x][y+i] != ' ':
                return False
    elif orientacion == 'v':
        if x + size > 10:
            return False
        for i in range(size):
            if tablero[x+i][y] != ' ':
                return False
    return True

def posicionar_barco(tablero,x:int,y:int,orientacion:str,size:int)->None:
    """
    Función que posiciona los barcos.
    :param tablero: Tablero de juego.
    :param x: Filas del tablero.
    :param y: Columnas del tablero.
    :param orientacion: La orientación del barco (horizontal o vertical).
    :param size: Tamaños de los barcos.
    :return:
    """
    if orientacion == 'h':
        for i in range(size):
            tablero[x][y+i] = 'B'
    elif orientacion == 'v':
        for i in range(size):
            tablero[x+i][y] = 'B'

def ganador(tablero)->bool:
    """
    Función que verifica si aún hay algun barco en el tablero para ddeterminar al ganador.
    :param tablero: Tablero de juego.
    :return:
    """
    for fila in tablero:
        for casilla in fila:
            if casilla == 'B':
                return False
    return True

def cadena_a_entero(cadena: str)-> int | None:
    no_puntos = cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-").replace(".", "")
    if revisar_cadena.isnumeric() and no_puntos in (0,1) and no_guiones in (0,1):
        return int(cadena)
    else:
        return None


def unocontrauno(tablero_jugador,tablero_oponente,ataques_jugador,ataques_oponente)->None:
    """
    Función de juego jugador 1 contra jugador 2.
    :param tablero_jugador: Tablero del ugador 1.
    :param tablero_oponente: Tablero del jugador 2.
    :param ataques_jugador: Tablero que muestra los ataques del jugador 1.
    :param ataques_oponente: Tablero que muestra los ataques del jugador 2.
    :return:
    """
    letra_a_numero = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}

    cantidad_barcos = input("¿Con cuántos barcos jugarán?: ")
    while not cantidad_barcos.isnumeric():
        print("Valor no válido.")
        cantidad_barcos = input("Intenta nuevamente: ")
    cantidad_barcos = int(cantidad_barcos)

    print("    1   2   3   4   5   6   7   8   9   10")
    for fila in tablero_jugador:
        print(fila[0], "|", fila[1], "|", fila[2], "|", fila[3], "|", fila[4], "|", fila[5], "|", fila[6], "|",
              fila[7],"|", fila[8], "|", fila[9], "|")
        print("  -----------------------------------------")
    print(f"Tendrán {cantidad_barcos} barcos de diferentes tamaños, desde 1 hasta {cantidad_barcos} casillas de longitud.")

    print("Jugador 1")
    colocar_barcos(tablero_jugador, cantidad_barcos,ataques_jugador)
    print("Jugador 2")
    colocar_barcos(tablero_oponente, cantidad_barcos, ataques_oponente)

    while True:
        print()
        while True:
            print("Turno jugagador 1")
            imprimir_tablero(tablero_jugador,ataques_jugador)
            fila = input("Ingresa una fila para atacar (A-J): ").lower()
            while not fila in letra_a_numero:
                fila = input("Fila no válida. Ingresa una letra de A a J: ").lower()
            x1 = letra_a_numero[fila]

            y1 = input("Ingresa una columna para atacar (0-9): ")
            y1 = cadena_a_entero(y1)
            while y1 is None:
                y1 = input("Valor no válido.Intenta nuevamente: ")
                y1 = cadena_a_entero(y1)

            if tablero_oponente[x1][y1] == 'B':
                print("Tocado")
                tablero_oponente[x1][y1] = 'X'
                ataques_jugador[x1][y1] = 'X'
                if ganador(tablero_oponente):
                    print("Felicidades, ganó el jugador 1.")
                    imprimir_tablero(tablero_oponente, ataques_oponente)
                    return
            else:
                print("Agua")
                tablero_oponente[x1][y1] = 'O'
                ataques_jugador[x1][y1] = 'O'
                break

        print()
        while True:
            print("Turno jugagador 2")
            imprimir_tablero(tablero_oponente, ataques_oponente)
            fila = input("Ingresa una fila para atacar (A-J): ").lower()
            while not fila in letra_a_numero:
                fila = input("Fila no válida. Ingresa una letra de A a J: ").lower()
            x2 = letra_a_numero[fila]

            y2 = input("Ingresa una columna para atacar (0-9): ")
            y2 = cadena_a_entero(y2)
            while y2 is None:
                y2 = input("Valor no válido.Intenta nuevamente: ")
                y2 = cadena_a_entero(y2)

            if tablero_jugador[x2][y2] == 'B':
                print("Tocado")
                tablero_jugador[x2][y2] = 'X'
                ataques_oponente[x2][y2] = 'X'
                if ganador(tablero_jugador):
                    print("Felicidades, ganó el jugador 2.")
                    imprimir_tablero(tablero_jugador, ataques_jugador)
                    return
            else:
                print("Agua")
                tablero_jugador[x2][y2] = 'O'
                ataques_oponente[x2][y2] = 'O'

def unocontracpu(tablero_jugador,tablero_oponente,ataques_jugador,ataques_oponente)->None:
    """
    Fucnión de juego jugador contra CPU.
    :param tablero_jugador: Tablero del jugador 1.
    :param tablero_oponente: Tablero de la CPU.
    :param ataques_jugador: Tablero que muestra los ataques del jugador 1.
    :param ataques_oponente: Tablero que muestra los ataques de la CPU.
    :return:
    """
    letra_a_numero = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}

    cantidad_barcos = input("¿Con cuántos barcos jugarán?: ")
    while not cantidad_barcos.isnumeric():
        print("Valor no válido.")
        cantidad_barcos = input("Intenta nuevamente: ")
    cantidad_barcos = int(cantidad_barcos)

    print("    1   2   3   4   5   6   7   8   9   10")
    for fila in tablero_jugador:
        print(fila[0], "|", fila[1], "|", fila[2], "|", fila[3], "|", fila[4], "|", fila[5], "|", fila[6], "|",
              fila[7], "|", fila[8], "|", fila[9], "|", fila[10], "|")
        print("  -----------------------------------------")
    print(f"Tendrán {cantidad_barcos} barcos de diferentes tamaños, desde 1 hasta {cantidad_barcos} casillas de longitud.")

    print("Jugador 1")
    colocar_barcos(tablero_jugador, cantidad_barcos,ataques_jugador)
    print("Jugador 2")
    colocar_barcos_cpu(tablero_oponente,cantidad_barcos,ataques_oponente)

    while True:
        print()
        while True:
            print("Turno jugagador 1")
            imprimir_tablero(tablero_jugador,ataques_jugador)
            fila = input("Ingresa una fila para atacar (A-J): ").lower()
            while not fila in letra_a_numero:
                fila = input("Fila no válida. Ingresa una letra de A a J: ").lower()
            x1 = letra_a_numero[fila]

            y1 = input("Ingresa una columna para atacar (0-9): ")
            y1 = cadena_a_entero(y1)
            while y1 is None:
                y1 = input("Valor no válido.Intenta nuevamente: ")
                y1 = cadena_a_entero(y1)

            if tablero_oponente[x1][y1] == 'B':
                print("Tocado")
                tablero_oponente[x1][y1] = 'X'
                ataques_jugador[x1][y1] = 'X'
                if ganador(tablero_oponente):
                    print("Felicidades, ganó el jugador 1.")
                    imprimir_tablero(tablero_oponente, ataques_oponente)
                    return
            else:
                print("Agua")
                tablero_oponente[x1][y1] = 'O'
                ataques_jugador[x1][y1] = 'O'
                break

        while True:
            print("Turno de la CPU")
            x2 = random.randint(0,9)
            y2 = random.randint(0,9)

            if tablero_jugador[x2][y2] == 'B':
                print("Tocado")
                tablero_jugador[x2][y2] = 'X'
                ataques_oponente[x2][y2] = 'X'
                if ganador(tablero_jugador):
                    print("Felicidades, ganó el jugador 2.")
                    imprimir_tablero(tablero_jugador, ataques_jugador)
                    return
            else:
                print("Agua")
                tablero_jugador[x2][y2] = 'O'
                ataques_oponente[x2][y2] = 'O'
                break




def funcion_princial_battalla_naval():
    tablero_jugador = [['A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],['B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
                       ['C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],['D', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
                       ['E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],['F', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
                       ['G', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],['H', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
                       ['I', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],['J', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ']]

    tablero_oponente = [['A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],['B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
                       ['C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],['D', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
                       ['E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],['F', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
                       ['G', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],['H', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
                       ['I', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],['J', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ']]

    ataques_jugador = [['A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],['B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
                       ['C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],['D', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
                       ['E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],['F', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
                       ['G', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],['H', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
                       ['I', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],['J', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ']]

    ataques_oponente = [['A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],['B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
                       ['C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],['D', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
                       ['E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],['F', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
                       ['G', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],['H', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
                       ['I', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],['J', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ']]

    while True:
        opcion = menu()
        if opcion == 1:
            unocontrauno(tablero_jugador, tablero_oponente, ataques_jugador, ataques_oponente)
            print()
        elif opcion == 2:
            unocontracpu(tablero_jugador, tablero_oponente, ataques_jugador, ataques_oponente)
        elif opcion == 0:
            print("Vuelve pronto.")
            print("Saliendo...")
            break
        else:
            print("Valor no válido.")

if __name__ == '__main__':
    funcion_princial_battalla_naval()