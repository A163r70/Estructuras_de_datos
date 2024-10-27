'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 26 de Octubre de 2024
Descripción: Este programa determinará si te permiten el acceso al bar "La Negra", por lo que se debe cumplir lo siguiente:

Tener al menos 18 años.
Tener al menos $ 250.00 para gastar.
Si ambas condiciones se cumplen, se imprime el mensaje en consola: "¡Bienvenido a tu mejor bar!".
En caso contrario, se imprime: "Lo sentimos, ya estamos por cerrar!
'''
edad = int(input("Ingresa tu edad: "))
dinero = int(input("Ingresa tu presupuesto: "))

if edad >= 18 and dinero >= 250:
    print("¡Bienvenido a tu mejor bar!.")
else:
    print("Lo sentimos, ya estamos por cerrar.")