'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 13 de enero de 2025
Descripción: Conversiones.
'''

def imprimir_alumno(nombre: str, edad: int, matricula: int, grupo: int, semestre: int)-> None:
    print("*** Datos personales ***")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Matrícula: {matricula}")
    print(f"Grupo: {grupo}")
    print(f"Semestre: {semestre}")



def main()->None:
    pass

if __name__ == '__main__':
    nombre = "Alberto"
    edad = 19
    matricula = 12305839
    grupo = 303
    semetre = 3

    main()
    imprimir_alumno(nombre,edad,matricula,grupo,semetre)