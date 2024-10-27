'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 15 de Octubre de 2024
Descripción: Este programa determinará True o False de acuerdo a la expresión (exp1 O exp2) Y (exp3 O exp4).
'''

print("*** Expresión booleana (Exp1 o Exp2) Y (Exp3 o Exp4) ***")
#Le pedimos al ususario 4 valores.
Expresion_1 = input("Ingresa V para Verdadero o F para Falso: ")
Expresion_1 = Expresion_1.lower() == "v"
Expresion_2 = input("Ingresa V para Verdadero o F para Falso: ")
Expresion_2 = Expresion_2.lower() == "v"
Expresion_3 = input("Ingresa V para Verdadero o F para Falso: ")
Expresion_3 = Expresion_3.lower() == "v"
Expresion_4 = input("Ingresa V para Verdadero o F para Falso: ")
Expresion_4 = Expresion_4.lower() == "v"
#Imprimimos el resultado de la operación.
print(f"El resultado de la expresión boolean es: {(Expresion_1 or Expresion_2) and (Expresion_3 or Expresion_4)}")