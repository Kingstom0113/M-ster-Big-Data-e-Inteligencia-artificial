# Crea una lista con los precios de productos y calcula el promedio.

import random

lista = [random.randint(1, 100) for _ in range(10)]
print(lista)
suma = sum(lista)
promedio = suma / len(lista)
print(promedio)
