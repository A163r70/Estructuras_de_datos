'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 13 de enero de 2025
Descripción: Conversiones.
'''

def imprimir_alumno(nombre: str, edad: int, matricula: int, grupo: int, *, semestre: int= 3)-> None:
    """
    Función que imprime datos de un alumno.
    :param nombre: Nombre del alumno.
    :param edad: Edad del alumno.
    :param matricula: Matrícula del alumno
    :param grupo: Grupo del alumno.
    :param semestre: Semetre del alumno.
    :return:
    """
    print("*** Datos personales ***")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Matrícula: {matricula}")
    print(f"Grupo: {grupo}")
    print(f"Semestre: {semestre}")


def main()->None:

    imprimir_alumno("Alberto", 31, 123, 303)

    # Argumentos por nombre
    imprimir_alumno(nombre="Jesús", edad=20, matricula=12392394, grupo=0, semestre=3)

    imprimir_alumno("Alberto", 31, 123, grupo= 3, semestre= 2)

if __name__ == '__main__':
    nombre = "Alberto"
    edad = 19
    matricula = 12305839
    grupo = 303
    #semetre = 3

    main()
    imprimir_alumno(nombre,edad,matricula, grupo)

