# -*- coding: utf-8 -*-

# Encuentra los n�meros pares en una lista de 10 n�meros enteros.

import random

lista = [random.randint(1, 100) for _ in range(10)]
print(lista)
pares = [numero for numero in lista if numero % 2 == 0]

print(pares)
