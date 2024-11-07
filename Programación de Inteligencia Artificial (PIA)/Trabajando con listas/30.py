# -*- coding: utf-8 -*-
# Crea una lista de números al azar y usa sorted() para ordenar la lista sin modificar la original.

import random

lista = [random.randint(1, 100) for _ in range(10)]
print(lista)
