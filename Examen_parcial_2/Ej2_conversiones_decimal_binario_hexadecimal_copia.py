'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 06 de diciembre de 2024
Descripción: Segundo ejercicio del examen del segundo parcial.
'''

#Mostramos un menú con las opciones que puede realizar el usuario, le pedimos que opción que desea y la retornamos
def menu():
    print("***  Ejercicio 2. Conversión entre las bases decimal, binaria y hexadecimal.  ***")
    print("1.- Convertir de decimal a binario y hexadecimal.")
    print("2.- Convertir de binario a decimal y hexadecimal.")
    print("3.- Convertir de hexadecimal a decimal y binario.")
    print("4.- Suma de binarios")
    print("0.- Salir.")
    opcion = int(input("Ingrese una opción: "))
    return opcion

#Para convertir de decimal a binario declaramos una lista vacía donde almacenaremos los 0 y 1
def decimal_binario_hexa(decimal):
    numero1 = decimal
    binario = [ ]
    contador = 0
    while numero1 > 0:
        residuo = numero1 % 2#Calculamos el residuo al dividir entre 2
        binario.insert(contador, residuo)#Insertamos el residuo en la lista.
        contador += 1
        numero1 //= 2#Dividimos nuestro número original.
    binario.reverse()#Volteamos la cadena para que los 0 y 1 esten colocados correctamente.
    binario_cadena = ''.join(map(str, binario))#Convertimos la lista en una cadena para mostrarlo mejor.
#Conversión de decimal a hexadecimal
    numero2 = decimal
    hexa = ""#Declaramos una cadena vacía donde guradaremos la conversión
    hexadecimal = "0123456789ABCDEF"#Ocupamos una cadena de caracteres hexadecimales
    while numero2 > 0:
        residuoh = numero2 % 16#Obtenemos el residuo al multiplicar entre 16, ya que es hexadecimal
        hexa = hexadecimal[residuoh] + hexa#Vamos agregando los digitos y acomodandolos también
        numero2 //= 16#Dividimos entre 16
    binario_hexadecimal = (binario_cadena, hexa)#Guardamos las conversiones en una tupla
    print(f"El número decimal {decimal} en binario es Ob{binario_hexadecimal[0]} y en hexadecimal es Ox{binario_hexadecimal[1]}")#Imprimimos las conversiones

def binario_decimal_hexa(binario):
    decimal = 0
    cantidad = len(binario)#Determinamos la cantidad de digitos que tiene el número ingresado por el usuario.
    for i in range(cantidad):#Iteramos sobre la cantidad obtenida.
        numero = int(binario[i])#Obtenemos digito por digito y lo almacenamos en una varable
        potencia = cantidad - 1 - i#Obtenemos la potencia que seria 1,2,3...
        decimal += numero * (2 ** potencia)#Obtenemos el decimal.

#Con el decimal obtenido, podemos aplicar la misma lógica que en la función anterior.
    numero_convertido = decimal
    hexa = ""
    hexadecimal = "0123456789ABCDEF"
    while numero_convertido > 0:
        residuo = numero_convertido % 16
        hexa = hexadecimal[residuo] + hexa
        numero_convertido //= 16
    decimal_hexadecimal = (decimal, hexa)
    print(f"El número binario Ob{binario} en decimal es {decimal_hexadecimal[0]} y en hexadecimal es Ox{decimal_hexadecimal[1]}")
    print()

def hexa_decimal_binario(hexadecimal):
    #En este caso creamos un diccionario con los números en hexadecimal.
    hexadecimales = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15,}
    longitud = len(hexadecimal)#Obtenemos el tamaño del número ingresado.
    decimal = 0
    for i in range(longitud):
        digito = hexadecimal[i]
        valor = hexadecimales[digito]
        potencia = longitud -1-i
        decimal += valor * (16 ** potencia)

#Con el decimal obtenido, aplicamos la misma lógica de la conversión de decimal a binario.
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
    print(f"El número hexadecimal Ox{hexadecimal} en decimal es {decimal_binario[0]} y en binario es Ob{decimal_binario[1]}")
    print()

def suma_binarios(binario1, binario2):
    decimal1 = 0
    decimal2 = 0
    longitud1 = len(binario1)
    longitud2 = len(binario2)
    for i in range(longitud1):
        numero = int(binario1[i])
        potencia = longitud1 - 1 - i
        decimal1 += numero * (2 ** potencia)
    print(decimal1)
    for j in range(longitud2):
        digito = int(binario2[j])
        potencias = longitud2 - 1 - j
        decimal2 += digito * (2 ** potencias)
    print(decimal2)
    suma = decimal1 + decimal2

    suma_binaria = [ ]
    contador = 0
    while suma > 0:
        residuo = suma % 2
        suma_binaria.insert(contador, residuo)
        contador += 1
        suma //= 2
        suma_binaria.reverse()
        cadena_suma_binaria = ''.join(map(str, suma_binaria))
    print(f"La suma del número binario {binario1} más el número {binario2} es igual a {suma_binaria}")
"""

numero1 = decimal
    binario = [ ]
    contador = 0
    while numero1 > 0:
        residuo = numero1 % 2#Calculamos el residuo al dividir entre 2
        binario.insert(contador, residuo)#Insertamos el residuo en la lista.
        contador += 1
        numero1 //= 2

decimal = 0
    cantidad = len(binario)#Determinamos la cantidad de digitos que tiene el número ingresado por el usuario.
    for i in range(cantidad):#Iteramos sobre la cantidad obtenida.
        numero = int(binario[i])#Obtenemos digito por digito y lo almacenamos en una varable
        potencia = cantidad - 1 - i#Obtenemos la potencia que seria 1,2,3...
        decimal += numero * (2 ** potencia)
"""

contador = 1
while contador != 0:
    opcion =  menu()
    if opcion == 1:#Conversión de decimal a binario y a hexadecimal
        decimal = int(input("Ingrese el número decimal que quiere convertir: "))
        decimal_binario_hexa(decimal)#Llamamos a la función y le mandamos el número en decimal
    elif opcion == 2:#Conversión de binario a decimal y a hexadecimal
        binario = input("Ingresa el número binario que quiere convertir: ")
        binario_decimal_hexa(binario)#Llamamos a la función y le mandamos el número en binario
    elif opcion == 3:#Converersión de hexadecimal a decimal y a binario
        hexadecimal = input("Ingrese el número hexadecimal que quiere convertir: ")
        hexa_decimal_binario(hexadecimal)#Llamamos a la función y le mandamos el número en hexadecimal
    elif opcion == 4:
        print("Ingrese los número binarios que quiere sumar.")
        binario1 = input("Ingrese el primer número binario: ")
        binario2 = input("Ingrese el segundo número binario: ")
        suma_binarios(binario1, binario2)
    elif opcion == 0:#Salir
        contador = 0
    else:#Por si ingresa un número fuera de rango
        print("Valor no válido.")