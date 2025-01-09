'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 06 de enero de 2025
Descripción: .
'''

"""numero = int(input("Ingresa un número cualquiera: "))
print()
cadena = input("Ingresa una cadena: ")
print(cadena.isnumeric())
print(cadena.isalpha())
print(cadena.isalnum())"""

#isnumeric sirve para positivos y el 0
numero2 = input("Ingresa un número cualquiera: ")
while not numero2.isnumeric():
    print("Opción no válida")
    numero2 = input("Intenta nuevamente: ")
print()
numero2 = input(numero2)
print(f"El número {numero2} es de tipo: {type(numero2)}")#type para saber el tipo

def cadena_a_entero(cadenaa):#y a flotante
    no_puntos = cadenaa.count(".")
    #.replace reemplazar
    no_guiones = cadenaa.count("-")#.replace(".") va corrido
    revisar_cadena = cadenaa.lstrip("-")
    if revisar_cadena.isnumeric() and no_guiones in (0,1): #no_puntos(0,1)
        return int(cadenaa)#return float(cadenaa)
    else:
        return None
num_cadena = input("Ingresa un número entero: ")
numeroo = cadena_a_entero(num_cadena)
while numeroo is None:
    print("Opción no válida")
    num_cadena = input("Ingresa un número entero: ")
    numeroo = cadena_a_entero(num_cadena)

print(f"El número {numeroo} es tipo {type(numeroo)}")