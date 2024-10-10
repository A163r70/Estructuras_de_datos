#Jesús Alberto Ramírez Salinas
#3 de Octubre de 2024
#Descripción: En este programa conocemos el uso de las variables en Python

# En Python todo es un objeto
# Variable - una variable es un nombre que almacena un valor guardado en la memoria temporal.
# Reglas para los nombres de las variables en Python:
# - Utilizar únicamente letras (mayúsculas o minúsculas), números y el guion bajo
# - La variable no puede iniciar con números
# - No se pueden utilizar palabras reservadas, ejemplos: if, else, True, class
# - Es sensible a mayúsculas y minúsculas. Por ejemplo, las palabras "Hola", "hola" y "HOLA" son consideradas diferentes.

# Buenas prácticas
# - Utilizar minúsculas para las palabras
# - Separar las palabras con el guion bajo
# - Utilizar nombres descriptivos de acuerdo a su uso. Por ejemplo: edad, en lugar de e.

# Ejemplos correctos y con buenas prácticas
fecha_nacimiento = "1 de enero del 2000"
clase = "Estructuras de Datos"
horas_estudio = 8
nombre = "Alberto"
es_estudiante = True

# Ejemplos incorrectos (líneas comentadas porque marcan error) o de malas prácticas
f = "1 de enero del 2000"
fechanacimiento = "1 de enero del 2000"
# class = "Estructuras de Datos"
# 8horas_estudio = 8
Nombre = "A l b e r t o"
NOMBRE = "ALBERTO"

# Notar que las variables 'nombre', 'Nombre' y 'NOMBRE', son distintas
print()
print("Las variables son sensibles a mayúsculas y minúsculas:")
print("Variable nombre:", nombre)
print("Variable Nombre:", Nombre)
print("Variable NOMBRE:", NOMBRE)

# Toda variable requiere un valor inicial
semestre = 3        # es una variable que apunta a un objeto de tipo int con valor de 3
print(semestre)     # imprime el valor de la variable
semestre = 4        # la variable ya no apunta al objeto anterior, sino a uno nuevo, por lo que se pierde la referencia
print(semestre)

# Se crean varias variables para ejemplificar su uso
nombre = "Alberto"  # variable de tipo String
altura = 1.65       # variable de tipo Float
edad = "diecinueve"           # variable de tipo Int
semestre = 3        #variables de tipo int

print()                     #el prints solo ya trae el salto de línea incluído
print("Nombre: ", nombre)
print("Altura: ", altura, " cm")
print("Edad: ", edad, " años")
print("Semestre: ", semestre)