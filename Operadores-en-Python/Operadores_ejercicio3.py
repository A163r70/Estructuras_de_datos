'''
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 15 de Octubre de 2024
Descripción: Este programa determinará si un usuario se autentifica correctamente con su usuario y contraseña.

'''

#Ejercicio Puesto por el docente en clase.
numero = int(input("Ingrese un número: "))
print(f"¿El número {numero} esta entre 10 y 15?: {numero>=10 and numero<=15}")

#Ejercicio pedido en el aula virtual.
Usuario = "Alberto"
Contraseña = "12345"
usuario = input("Ingresa tu usuario: ")
contraseña = input("Ingresa tu contraseña: ")

print(f"¿El acceso es correcto?: {Usuario == usuario and Contraseña == contraseña}")
