'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 06 de diciembre de 2024
Descripción: Segundo ejercicio del examen del segundo parcial.
'''


def menu():
    print("***  Ejercicio 2. Conversión entre las bases decimal, binaria y hexadecimal.  ***")
    print("1.- Convertir de decimal a binario y hexadecimal.")
    print("2.- Convertir de binario a decimal y hexadecimal.")
    print("3.- Convertir de hexadecimal a decimal y binario.")
    print("0.- Salir.")
    opcion = int(input("Ingrese una opción: "))
    return opcion

def decimal_binario_hexa(decimal):
    numero1 = decimal
    binario = [ ]
    contador = 0
    while numero1 > 0:
        residuo = numero1 % 2
        binario.insert(contador, residuo)
        contador += 1
        numero1 //= 2
    binario.reverse()
    binario_cadena = ''.join(map(str, binario))

    numero2 = decimal
    hexa = ""
    hexadecimal = "0123456789ABCDEF"
    while numero2 > 0:
        residuoh = numero2 % 16
        hexa = hexadecimal[residuoh] + hexa
        numero2 //= 16
    binario_hexadecimal = (binario_cadena, hexa)
    print(f"El número decimal {decimal} en binario es {binario_hexadecimal[0]} y en hexadecimal es {binario_hexadecimal[1]}")

def binario_decimal_hexa(binario):
    decimal = 0
    cantidad = len(binario)
    for i in range(cantidad):
        numero = int(binario[i])
        potencia = cantidad - 1 - i
        decimal += numero * (2 ** potencia)

    numero_convertido = decimal
    hexa = ""
    hexadecimal = "0123456789ABCDEF"
    while numero_convertido > 0:
        residuo = numero_convertido % 16
        hexa = hexadecimal[residuo] + hexa
        numero_convertido //= 16
    decimal_hexadecimal = (decimal, hexa)
    print(f"El número binario {binario} en decimal es {decimal_hexadecimal[0]} y en hexadecimal es {decimal_hexadecimal[1]}")
    print()

def hexa_decimal_binario(hexadecimal):
    hexadecimales = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15,}
    longitud = len(hexadecimal)
    decimal = 0
    for i in range(longitud):
        digito = hexadecimal[i]
        valor = hexadecimales[digito]
        potencia = longitud -1-i
        decimal += valor * (16 ** potencia)

    numero1 = decimal
    binario = []
    contador = 0
    while numero1 > 0:
        residuo = numero1 % 2
        binario.insert(contador, residuo)
        contador += 1
        numero1 //= 2
    binario.reverse()
    cadena_binaria = ''.join(map(str, binario))
    decimal_binario = (decimal, cadena_binaria)
    print(f"El número hexadecimal {hexadecimal} en decimal es {decimal_binario[0]} y en binario es {decimal_binario[1]}")
    print()

contador = 1
while contador != 0:
    opcion =  menu()
    if opcion == 1:
        decimal = int(input("Ingrese el número decimal que quiere convertir: "))
        decimal_binario_hexa(decimal)
    elif opcion == 2:
        binario = input("Ingresa el número binario que quiere convertir: ")
        binario_decimal_hexa(binario)
    elif opcion == 3:
        hexadecimal = input("Ingrese el número hexadecimal que quiere convertir: ")
        hexa_decimal_binario(hexadecimal)
    elif opcion == 0:
        contador = 0
    else:
        print("Valor no válido.")
