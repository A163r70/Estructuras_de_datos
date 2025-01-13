'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 13 de enero de 2025
Descripción: Conversiones.
'''


def saludar(nombre: str)-> None:
    """
    Función que saluda a un nombre recibido.
    :param nombre: {Cadena con un nombre a saludar.}
    :return:
    """
    print(f"Hola, {nombre}")

if __name__ == '__main__':
    nombre = input("Ingrese un nombre: ")
    saludar(nombre)