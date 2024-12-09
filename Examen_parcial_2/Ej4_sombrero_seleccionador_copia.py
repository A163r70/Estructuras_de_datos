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
#En una lista de diccionarios guradamos las preguntas con la casa a la que posiblemente perteneceria el usuario.
preguntas = [
    {'pregunta': "¿Cuál de las siguientes opciones odiarías más que la gente te llamara?",
     'respuesta': {'1': 'Gryffindor', '2': 'Ravenclaw', '3': 'Slytherin', '4': 'Hufflepuff'}},
    {'pregunta': "Después de tu muerte ¿qué es lo que más le gustaría que hiciera la gente cuando escuche su nombre?",
     'respuesta': {'1': 'Hufflepuff', '2': 'Gryffindor', '3': 'Ravenclaw', '4': 'Slytherin'}},
    {'pregunta': "Dada la opción, preferirías inventar una poción que garantizara:",
     'respuesta': {'1': 'Gryffindor', '2': 'Ravenclaw', '3': 'Hufflepuff', '4': 'Slytherin'}},
    {'pregunta': "¿Cómo te definirías en una sola palabra?",
     'respuesta': {'1': 'Gryffindor', '2': 'Ravenclaw', '3': 'Slytherin', '4': 'Hufflepuff'}},
    {'pregunta': "¿Qué cualidad te describe mejor?",
     'respuesta': {'1': 'Gryffindor', '2': 'Ravenclaw', '3': 'Hufflepuff', '4': 'Slytherin'}},
    {'pregunta': "¿Cuál es tu clase favorita?",
     'respuesta': {'1': 'Gryffindor', '2': 'Ravenclaw', '3': 'Hufflepuff', '4': 'Slytherin'}},
    {'pregunta': "¿Cuál es tu lenguaje de programación favorito?",
     'respuesta': {'1': 'Gryffindor', '2': 'Ravenclaw', '3': 'Hufflepuff', '4': 'Slytherin'}},
     {'pregunta': "¿Qué superpoder deseas tener?",
      'respuesta': {'1':'Slytherin', '2': 'Gryffindor', '3': 'Hufflepuff', '4': 'Ravenclaw'}}
]
#En una lista de listas guardamos las opciones que tiene el usuario.
opcion_respuesta = [
    ["1. Ordinario.", "2. Ignorante.", "3. Cobarde.", "4. Egoísta."],
    ["1. Te extraña, pero sonríe.", "2. Pide más historias sobre tus aventuras.",
     "3. Piensa con admiración tus logros.", "4. No me importa lo que piensen de mí."],
    ["1. Gloria.", "2. Sabiduría.", "3. Amor.", "4. Poder."],
    ["1. Valiente.", "2. Ambicioso.", "3. Leal.", "4. Curioso."],
    ["1. La fuerza.", "2. La astucia.", "3. La paciencia.", "4. La inteligencia."],
    ["1. Vuelo.", "2. Defensa contra las artes oscuras.", "3.  Animales fantásticos.", "4. Pociones."],
    ["1. C.", "2. Python.", "3.  C++.", "4. JavaScript."],
    ["1. Dormir", "2. Invisibilidad", "3. Superfuerza", "4. Teletransportarse"]
]

def test(preguntas, opcion_respuesta):
#Revolvemos la preguntas y las respuestas para que cada vez que se realize el test cambien el orden de las preguntas.
    random.shuffle(preguntas)
    random.shuffle(opcion_respuesta)

#Creamos un diccionario que almacenará los puntos de cada casa.
    puntos = {'Gryffindor':0, 'Slytherin':0, 'Hufflepuff':0, 'Ravenclaw':0}

    for i in range(len(preguntas)):#Acomodamos las preguntas revuletas con sus respectivos opciones.
        pregunta = preguntas[i]
        opciones = opcion_respuesta[i]

        print(f"{i+1}. {pregunta['pregunta']}")#Mostramos la preguntas.
        for opcion in opciones:
            print(opcion)#Mostramos las opciones que tiene para elegir.

        while True:
#Si la respuesta ingresada esta en las listas de respuestas verificamos a que casa se le asignara y le asignamos un punto
            respuesta = input("Selecciona tu respuesta: ")
            if respuesta in pregunta['respuesta']:
                punto_casa = pregunta['respuesta'][respuesta]
                puntos[punto_casa] += 1
                break
            else:
                print("Opción no válida.")
#Obtenemos a la casa ganadora comparando si su puntaje es mayor al puntaje preestablecido, si es mayor el puntaje se
#actualiza y lal final queda la casa con mayor puntaje.
    casa_ganador = ""
    mayor_puntaje = 0
    for casa, puntaje in puntos.items():
        if puntaje > mayor_puntaje:
            mayor_puntaje = puntaje
            casa_ganador = casa

    print(f"Tu casa es: {casa_ganador}")#Mostramos a que casa pertenece el usuario.

while True:
    opcion = menu()
    if opcion == 1:
        test(preguntas, opcion_respuesta)
    elif opcion == 0:
        break
    else:
        print("Valor no válido.")