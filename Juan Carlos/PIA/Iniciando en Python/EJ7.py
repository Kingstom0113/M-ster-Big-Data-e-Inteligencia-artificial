# 1. Crear la tupla 'puntos' con los valores dados
puntos = (5, 10, 15, 20, 25)

# 2. Imprimir el valor en la tercera posición de la tupla
print("Valor en la tercera posición:", puntos[2])  # Recuerda que el índice empieza en 0

# 3. Convertir la tupla en una lista
lista_puntos = list(puntos)

# 4. Agregar el valor 30 al final de la nueva lista
lista_puntos.append(30)

# 5. Convertir la lista nuevamente en tupla y imprimirla
nueva_tupla = tuple(lista_puntos)
print("Tupla final:", nueva_tupla)
