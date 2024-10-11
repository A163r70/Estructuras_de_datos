'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 11 de Octubre del 2024
Descripción:
Ejercicio sobre la conversión de los tipos de datos (Casting) visto en el programa anterior.
'''

'''
Instrucciones: 
Realiza un programa de nombre Casting_ejercicio.py que realice lo siguiente:
a) Convierta los siguientes números en cadenas: 3.14159265, 12, 0.
b) De los números anteriores, indica su valor booleano.
c) Convierta las siguientes cadenas a números: "10002", "100.02", "0".
d) De las cadenas anteriores, indica su valor booleano. Nota: especificar por qué el resultado de la cadena "0".
'''
print("Conversión de números a cadenas.")
num_1 = 3.14159265
num_2 = 12
num_3 = 0
print(f"los numeros {num_1}, {num_2} y {num_3} los convertimos a cadena con str(num_1): {str(num_1)}, str(num_2): {str(num_2)} y str(num_3): {str(num_3)}.")

print()
print("Conversión a booleanos.")
Num_1 = 3.14159265
es_verdadero = bool(Num_1)
print(f"¿El valor de {Num_1} es verdadero?: {es_verdadero}")
Num_2 = 12
es_verdadero = bool(Num_2)
print(f"¿El valor de {Num_2} es verdadero?: {es_verdadero}")
Num_3 = 0
es_verdadero = bool(Num_3)
print(f"¿El valor de {Num_3} es verdadero?: {es_verdadero}")
print()
print("Conversión de cadenas a numeros.")
cad_1 = "10002"
cad_int_1 = int(cad_1)
print(f"Número como cadena: {cad_1}.")
print(f"Número como entero más uno: {cad_int_1+1}")
cad_2 = "100.02"
cad_int_2 = float(cad_2)
print(f"Número como cadena: {cad_2}")
print(f"Número como float más uno: {cad_int_2+1}")
cad_3 = "0"
cad_int_3 = int(cad_3)
print(f"Número como cadena: {cad_3}")
print(f"Número como entero más uno: {cad_int_3+1}")
print()
print("Conversión a booleano.")
cadena_1 = "10002"
es_verdad = bool(cadena_1)
print(f"¿El valor de {cadena_1} es verdadero?: {es_verdad}")
cadena_2 = "100.022"
es_verdad = bool(cadena_2)
print(f"¿El valor de {cadena_2} es verdadero?: {es_verdad}")
cadena_3 = "0"
es_verdad = bool(cadena_3)
print(f"¿El valor de {cadena_3} es verdadero?: {es_verdad}")
#El valor del 0 es True, porque pasa lo mismo que en el casting, hay una cadena vacía lo cual Python creo que
#en vez de considerarlo como False, lo considera True. No tengo otra explicación del por qué.