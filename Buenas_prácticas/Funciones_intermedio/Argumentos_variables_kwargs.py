'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 21 de enero de 2025
Descripción: Conversiones.
'''

def preferencias(tema: str, ** kwargs):
    print(f"El tema es {tema}")
    for key, value in kwargs.items():
        print(f"Nombre: {key} prefiere {value}")


if __name__ == '__main__':
    preferencias("Comida", Rebeca= "Mole", Juan= "Tacos", Bryan= "Tlayudas", Jamileth="Tamales")