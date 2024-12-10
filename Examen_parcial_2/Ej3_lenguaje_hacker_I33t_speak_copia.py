'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 06 de diciembre de 2024
Descripción: Tercer ejercicio del examen del segundo parcial.
'''

def menu():
    print("***  Ejercicio 3. Lenguaje hacker (l33t sp34k).  ***")
    print("1.- Convertir un texto a lenguaje básico.")
    print("2.- Convertir un texto a lenguaje intermedio.")
    print("0.- Salir.")
    opcion = int(input("Ingrese una opción: "))
    print()
    return opcion

def lenguaje_basico(texto):
#Creamos un diccionario donde almacenamos las vocales y sus conversiones en el lenguaje hacker.
     lenguaje = {'a': "4", 'e': "3", 'i': "1", 'o': "0", 'u': "(_)",
                 'A': "4", 'B': "3", 'I': "1", 'O': "0", 'U': "(_)",
                 '1': "L", '2': "R", '3': "E", '4': "A", '5': "S",
                 '6': "b", '7': "T", '8': "B", '9': "g", '0': "o"}
     texto_traducido = ""#Creamos una cadena vacía donde guradaremos el texto traducido.
     for letra in texto:#Iteramos sobre el texto del usuario.
         if letra in lenguaje:#Si una letra del texto esta en el diccionario guradamos su valor en la cadena creada previamente.
             texto_traducido += lenguaje[letra]
         else:#Si la letra no se encuentra en el diccionario solo guardamos la letra tal y como aparece en el texto.
            texto_traducido += letra
     print(f"El texto traducido es el siguiente: ")
     print(texto_traducido)#Imprimimos el texto traducido.
     print()

#Ocupamos la misma lógica que en el caso anterior. Solo que en este caso almacenamos el abecedario completo, en
#mayúsculas y  minúsculas.
def lenguaje_medio(texto2):
    lenguaje = {'a':"4",'b':"13",'c':"[",'d':")",'e':"3",'f':"|=",'g':"&",'h':"#",'i':"1",'j':",_|",'k':"|<",'l':"|_",
                'm':"JVI",'n':"^/",'o':"0",'p':"|*",'q':"(_,)",'r':"|2",'s':"5",'t':"7",'u':"(_)",'v':"|/",'w':"VV",
                'x':"><",'y':"j",'z':"2",'A':"4",'B':"13",'C':"[",'D':")",'E':"3",'F':"|=",'G':"&",'H':"#",'I':"1",
                'J':",_|",'K':"|<",'L':"|_",'M':"JVI",'N':"^/",'O':"0",'P':"|*",'Q':"(_,)",'R':"|2",'S':"5",'T':"7",
                'U':"(_)",'V':"|/",'W':"VV",'X':"><",'Y':"j",'Z':"2", '1': "L", '2': "R", '3': "E", '4': "A", '5': "S",
                 '6': "b", '7': "T", '8': "B", '9': "g", '0': "o"}
    texto_traducido = ""
    for letras in texto2:
        if letras in lenguaje:
            texto_traducido += lenguaje[letras]
        else:
            texto_traducido += letras
    print(f"El texto traducido es el siguiente: ")
    print(texto_traducido)#Imprimimos el texto ya traducido.
    print()

contador = 1
while contador != 0:
    opcion = menu()
    if opcion == 1:#Traducción a lenguaje hacker básico
        texto = input("Ingresa el texto que desea traducir al lenguaje básico: ")
        lenguaje_basico(texto)
    elif opcion == 2:#Traducción a lenguaje hacker intermedio.
        texto2 = input("Ingresa el texto que desea traducir al lenguaje intermedio: ")
        lenguaje_medio(texto2)
    elif opcion == 0:
        contador = 0
    else:
        print("Valor no válido.")