'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 02 de diciembre de 2024
Descripción: Segundo ejercicio sobre diccionarios.
'''
from random import choice

victoria = 0
empate = 0
victoria_cpu = 0

piedra_papel_tijeras_lagarto_spock = {('PIEDRA', 'TIJERAS'): "JUGADOR",
                        ('PIEDRA', 'PAPEL'): "CPU",
                        ('PAPEL', 'PIEDRA'): "JUGADOR",
                        ('PAPEL', 'TIJERAS'): "CPU",
                        ('TIJERAS', 'PAPEL'): "JUGADOR",
                        ('TIJERAS', 'PIEDRA'): "CPU",
                        ('PIEDRA', 'LAGARTO'): "JUGADOR",
                        ('LAGARTO', 'PIEDRA'): "CPU",
                        ('LAGARTO', 'SPOCK'): "JUGADOR",
                        ('SPOCK', 'LAGARTO'): "CPU",
                        ('SPOCK', 'TIJERAS'): "JUGADOR",
                        ('TIJERAS', 'SPOCK'): "CPU",
                        ('TIJERAS', 'LAGARTO'): "JUGADOR",
                        ('LAGARTO', 'TIJERAS'): "CPU",
                        ('LAGARTO', 'PAPEL'): "JUGADOR",
                        ('PAPEL', 'LAGARTO'): "CPU",
                        ('PAPEL', 'SPOCK'): "JUGADOR",
                        ('SPOCK', 'PAPEL'): "CPU",
                        ('SPOCK', 'PIEDRA'): "JUGADOR",
                        ('PIEDRA', 'SPOCK'): "CPU"}

def menu(victoria, victoria_cpu, empate):
    print(f"Victorias del jugador: {victoria}, empates: {empate}, victorias del CPU: {victoria_cpu}")
    print()
    print("***  Juego de piedra, papel o tijeras  ***")
    print("1.- Piedra.")
    print("2.- Papel.")
    print("3.- Tijeras.")
    print("4.- Lagarto.")
    print("5.- Spock.")
    print("6.- Ver reglas.")
    print("0.- Salir.")
    opcion = int(input("Ingresa una opción: "))
    print()
    return opcion

def ver_reglas():
    print("Este juego es una variante del ya conocido juego 'Piedra, Papel y Tijeras', con algunas opciones de más.")
    print("A continucación se muestran las reglas")
    print("Tenemos cicno opciones para elegir: ")
    print("1.- Piedra.")
    print("2.- Papel.")
    print("3.- Tijeras.")
    print("4.- Lagarto.")
    print("5.- Spock.")
    print("Las reglas de combate:")
    print("- Piedra aplasta al Lagarto.")
    print("- Lagarto envenena a Spock.")
    print("- Spock destroza las Tijeras.")
    print("- Tijeras decapitan al Lagarto")
    print("- Lagarto se come el Papel")
    print("- Papel refuta a Spock")
    print("- Spock vaporiza la Piedra")
    print("- Piedra aplasta las Tijeras (como en el juego clásico)")
    print("Hay un total de 25 resultados posibles, lo que lo hace más emocionante y desafiante que la versión original.")
    print()
    return ()

def jugador(opcion):
    eleccion_jugador = ""
    if opcion == 1:
        eleccion_jugador = "PIEDRA"
    elif opcion == 2:
        eleccion_jugador = "PAPEL"
    elif opcion == 3:
        eleccion_jugador = "TIJERAS"
    elif opcion == 4:
        eleccion_jugador = "LAGARTO"
    elif opcion == 5:
        eleccion_jugador = "SPOCK"
    elif opcion == 6:
        ver_reglas()
        return "INSTRUCCIONES", ""
    elif opcion == 0:
        eleccion_jugador = "SALIR"
    else:
        print("Valor no válido.")
        return "INVALIDO", ""
    eleccion_cpu = choice(["PIEDRA", "PAPEL", "TIJERAS", "LAGARTO", "SPOCK"])
    print()
    return eleccion_jugador, eleccion_cpu

def juego(victoria, victoria_cpu, empate):
    while True:
        opcion = menu(victoria, victoria_cpu, empate)
        eleccion_jugador, eleccion_cpu = jugador(opcion)
        if eleccion_jugador == "SALIR":
            print("Resultados del juego.")
            print(f"Victorias del jugador: {victoria}, empates: {empate}, victorias del CPU: {victoria_cpu}")
            break
        if eleccion_jugador != "INSTRUCCIONES" and eleccion_jugador != "INVALIDO":
            resultado = piedra_papel_tijeras_lagarto_spock.get((eleccion_jugador, eleccion_cpu), "EMPATE")
            if resultado == "JUGADOR":
                print(f"Jugador: {eleccion_jugador}. CPU: {eleccion_cpu}. El resultado es: {resultado}")
                victoria += 1
            elif resultado == "CPU":
                print(f"Jugador: {eleccion_jugador}. CPU: {eleccion_cpu}. El resultado es: {resultado}")
                victoria_cpu += 1
            else:
                print(f"Jugador: {eleccion_jugador}. CPU: {eleccion_cpu}. El resultado es: EMPATE")
                empate += 1
            print()
    return victoria, victoria_cpu, empate

juego(victoria, victoria_cpu, empate)