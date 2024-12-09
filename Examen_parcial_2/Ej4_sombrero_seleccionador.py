'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 06 de diciembre de 2024
Descripción: Segundo ejercicio del examen del segundo parcial.
'''
import random


def menu():
    print("***  Ejercicio 4. Test del sombrero seleccionador de Harry Potter.  ***")
    print("Este programa determina la casa (Gryffindor, Slytherin, Hufflepuff y Ravenclaw) a la que perteneces, de acuerdo a tus respuestas.")
    print("1.- Iniciar test.")
    print("0.- Salir")
    opcion = int(input("Ingresa una opción: "))
    return opcion

preguntas = [
    {'pregunta': "¿Cuál de las siguientes opciones odiarías más que la gente te llamara?",
     'respuesta': {'1': 'Gryffindor', '2': 'Ravenclaw', '3': 'Slytherin', '4': 'Hufflepuff'}},
    {'pregunta': "Después de tu muerte ¿qué es lo que más le gustaría que hiciera la gente cuando escuche su nombre?",
     'respuesta': {'1': 'Hufflepuff', '2': 'Gryffindor', '3': 'Ravenclaw', '4': 'Slytherin'}},
    {'pregunta': "Dada la opción, preferirías inventar una poción que garantizara:",
     'respuesta': {'1': 'Gryffindor', '2': 'Ravenclaw', '3': 'Hufflepuff', '4': 'Slytherin'}},
    {'pregunta': "¿Cómo te definirías en una sola palabra?",
     'respuesta': {'1': 'Gryffindor', '2': 'Ravenclaw', '3': 'Slytherin', '4': 'Hufflepuff'}},
    {"¿Qué cualidad te describe mejor?"}
]

opcion_respuesta = [
    ["1. Ordinario.", "2. Ignorante.", "3. Cobarde.", "4. Egoísta."],
    ["1. Te extraña, pero sonríe.", "2. Pide más historias sobre tus aventuras.",
     "3. Piensa con admiración tus logros.", "4. No me importa lo que piensen de mí."],
    ["1. Gloria.", "2. Sabiduría.", "3. Amor.", "4. Poder."]
]

def test(preguntas, opcion_respuesta):
    random.shuffle(preguntas)
    random.shuffle(opcion_respuesta)

    puntos = {'Gryffindor':0, 'Slytherin':0, 'Hufflepuff':0, 'Ravenclaw':0}

    for i in range(len(preguntas)):
        pregunta = preguntas[i]
        opciones = opcion_respuesta[i]

        print(f"{i+1}. {pregunta['pregunta']}")
        for opcion in opciones:
            print(opcion)

        while True:
            respuesta = input("Selecciona tu respuesta: ")
            if respuesta in pregunta['respuesta']:
                punto_casa = pregunta['respuesta'][respuesta]
                puntos[punto_casa] += 1
                break
            else:
                print("Opción no válida.")

    casa_ganador = ""
    mayor_puntaje = 0
    for casa, puntaje in puntos.items():
        if puntaje > mayor_puntaje:
            mayor_puntaje = puntaje
            casa_ganador = casa

    print(f"Tu casa es: {casa_ganador}")

while True:
    opcion = menu()
    if opcion == 1:
        test(preguntas, opcion_respuesta)
    elif opcion == 0:
        break
    else:
        print("Valor no válido.")