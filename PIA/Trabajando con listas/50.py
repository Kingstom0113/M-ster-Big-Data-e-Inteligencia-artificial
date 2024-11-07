# Crea una lista de enteros y usa reduce() para obtener el producto de todos los elementos

from functools import reduce

lista = [1, 2, 3, 4, 5]

producto = reduce(lambda x, y: x * y, lista)

print(producto)
