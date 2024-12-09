'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 06 de diciembre de 2024
Descripción: Segundo ejercicio del examen del segundo parcial.
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
     lenguaje = {'a': "4", 'e': "3", 'i': "1", 'o': "0", 'u': "(_)",
                 'A': "4", 'B': "3", 'I': "1", 'O': "0", 'U': "(_)"}
     texto_traducido = ""
     for letra in texto:
         if letra in lenguaje:
             texto_traducido += lenguaje[letra]
         else:
            texto_traducido += letra
     print(f"El texto traducido es el siguiente: ")
     print(texto_traducido)
     print()

def lenguaje_medio(texto2):
    lenguaje = {'a':"4",'b':"13",'c':"[",'d':")",'e':"3",'f':"|=",'g':"&",'h':"#",'i':"1",'j':",_|",'k':"|<",'l':"|_",
                'm':"/V\ ",'n':"|\|",'o':"0",'p':"|*",'q':"(_,)",'r':"|2",'s':"5",'t':"7",'u':"(_)",'v':"\/",'w':"\/\/",
                'x':"><",'y':"j",'z':"2",'A':"4",'B':"13",'C':"[",'D':")",'E':"3",'F':"|=",'G':"&",'H':"#",'I':"1",
                'J':",_|",'K':"|<",'L':"|_",'M':"/\/\ ",'N':"^/",'O':"0",'P':"|*",'Q':"(_,)",'R':"|2",'S':"5",'T':"7",
                'U':"(_)",'V':"\/",'W':"\/\/",'X':"><",'Y':"j",'Z':"2"}
    texto_traducido = ""
    for letras in texto2:
        if letras in lenguaje:
            texto_traducido += lenguaje[letras]
        else:
            texto_traducido += letras
    print(f"El texto traducido es el siguiente: ")
    print(texto_traducido)
    print()

contador = 1
while contador != 0:
    opcion = menu()
    if opcion == 1:
        texto = input("Ingresa el texto que desea traducir al lenguaje básico: ")
        lenguaje_basico(texto)
    elif opcion == 2:
        texto2 = input("Ingresa el texto que desea traducir al lenguaje intermedio: ")
        lenguaje_medio(texto2)
    elif opcion == 0:
        contador = 0
    else:
        print("Valor no válido.")