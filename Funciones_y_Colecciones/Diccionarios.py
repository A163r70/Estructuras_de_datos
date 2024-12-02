'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 02 de diciembre de 2024
Descripción: Ejemplos sobre colecciones.
'''

"""
Un diccionario es ordenado, pero la forma de ingresar es diferente.
En vez de un ídnice, nosotros lo nombramos como queramos de la siguiente forma:
par_clave_valor

"""
print("** Ejemplo del uso de diccionarios **")
diccionario_profesor = {'nombre': "Alberto", 'primer apellido': "Martínez", 'edad': 31, 'correo': "alberto.mtba@unsij.edu.mx", 'cubo': 12}
#añadir elementos
print()
diccionario_alumno = { }
diccionario_alumno['nombre'] = "Alberto" #parecido a una lista, en vez de índices ponemos claves
diccionario_alumno['primer apellido'] = "Ramírez"
diccionario_alumno['grupo'] = 303
print(diccionario_profesor)
print(diccionario_alumno)
print()
#acceder
nombre_alumno = diccionario_alumno.get('nombre')#accedemos al diccionario y obtenemos el nombre
apellido_alumno = diccionario_alumno['primer apellido']#en vez del índice, accedemos a la clave
print(nombre_alumno)
print(apellido_alumno)
print()
#modificar elementos
#La clave no se puede modificar, pero el valor que tiene asignado sí
diccionario_alumno['nombre'] = "Jesús"
diccionario_alumno['grupo'] = 403
print(diccionario_alumno)
diccionario_alumno['segundo apellido'] = "Salinas"
diccionario_alumno['materia favorita'] =  "Estructura de datos"
print(diccionario_alumno)
print()
#Se eliminan los elementos
del diccionario_alumno['segundo apellido']#primer forma
diccionario_alumno.pop('grupo')
print(diccionario_alumno)
print()
#acceder a todo el par clave valor
for clave, valor in diccionario_alumno.items():
    print(f"clave: {clave} y valor: {valor}")
print()
#acceder solo al valor
for valor in diccionario_alumno.values():
    print(f"valor: {valor}")
print()
#acceder solo a las claves
for clave in diccionario_alumno.keys():
    print(f"clave: {clave}")
#Combinación con tuplas
#podemos utilizar una tupla como una clave
diccionario_egresados = {'nombre': "Santiago",('primer_apellido', 'segundo_apellido'): "Ramírez Salinas", 'edad': 25}
print(diccionario_egresados)
for valor in diccionario_egresados.values():
    print(f"valor: {valor}")
print()
for clave in diccionario_egresados.keys():
    print(f"clave: {clave}")
print()
diccionario_informatica = {'grupo_303': {'no. Alumnos': 12, 'no. Materias': 5, 'promedio_grupal': 7.99},
                           'grupo_503': {'no. Alumnos': 5, 'no. Materias': 5, 'promedio_grupal': 7.5},
                           'grupo_703': {'no. Alumnos': 8, 'no. Materias': 5, 'promedio_grupal': 7.6},
                           'grupo_903': {'no. Alumnos': 2, 'no. Materias': 5, 'promedio_grupal': 3.5},}
print(diccionario_informatica)
for grupo in enumerate(diccionario_informatica):
    print(f"Grupo: {grupo}")
#acceder a los elementos de un diccionario de diccionarios
promedio_303 = diccionario_informatica['grupo_303']['prmedio_grupal']
promedio_503 = diccionario_informatica['grupo_303']['prmedio_grupal']
promedio_703 = diccionario_informatica['grupo_303']['prmedio_grupal']
promedio_903 = diccionario_informatica['grupo_303']['prmedio_grupal']
print(promedio_303)
print(promedio_503)
print(promedio_703)
print(promedio_903)