'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 26 de Octubre de 2024
Descripción: Este programa determinará un descuento en compras en "La cona", de acuerdo a lo siguiente:

Si tiene membresía, obtiene un 5 % de descuento en todas sus compras.
Si tiene la membresía y su compra fue mayor o igual a $ 1000.00, entonces el descuento es del 8 %.
Si no tiene la membresía, no obtiene ningún descuento y se invita a ser miembro.
'''

print("*** Descuentos por ser miembro de La Cona ***")
compra = float(input("¿De cuánto fué su compra?: "))
membresia = input("¿Cuenta con la membresía?: ")

if compra >= 1000.00 and membresia == "si":
    print("Su descuento será del 8%.")
    print(f"Su total es de: {(compra - (compra * 8)/100):.2f}")
elif membresia == "si":
    print("Su descuento será del 5%.")
    print(f"Su total es de: {(compra - (compra * 5)/100):.2f}")
else:
    print("Se le invita a ser miembro de la tienda para obtener un descuente de hasta el 8%.")
