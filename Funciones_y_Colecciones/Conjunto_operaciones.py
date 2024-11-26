

conjuntoA = {11,7,10,9,5,1,15,7}
conjuntoB = {55,70,11,77,66,9,5}
print()
print(conjuntoA)
print(conjuntoB)
print("** Operaciones básicas **")
union = conjuntoA | conjuntoB
print(union)
interseccion = conjuntoA & conjuntoB
print(interseccion)
diferencia = conjuntoA - conjuntoB
print(diferencia)
print()
#Convertir de lista a conjuntos y viciversa
animales = ["León", "Tigre", "Leopardo", "Gato", "Aguila", "León"]
print(f"Lista de animales: {animales}")
#lista a conjunto set()
conjunto_animales = set(animales)
print(f"Lista convertrida a conjunto {conjunto_animales}")
#conjunto a lista
lista_modificada = list(conjunto_animales)
print(f"Conjunto convertido a lista {lista_modificada}")
#ganador = random.choice(lista) elije un número al azar de la lista