'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 21 de enero de 2025
Descripción: Conversiones.
'''

def colores_favoritos(persona: str, * vargs):
    print(f"{persona}: {vargs}")

def sumar(*vargs)->int:
    resultado = 0
    for i in vargs:
        resultado += i

    return resultado

if __name__ == '__main__':
    colores_favoritos("Jennifer", "Morado", "Negro", "Blanco", "Rosa")
    colores_favoritos("Addi", "Azul", "Blanco", "Negro")
    colores_favoritos("Alberto", "Azul")
    cadena = "Hola"
    tupla = "hola",
    print(cadena)
    print(tupla)
    resultado = sumar(4,3,4,1,6)
    print(resultado)

