# -*- coding: utf-8 -*-

# Crea una lista de números e invierte el orden de los números sin usar reverse().

import random

lista = [random.randint(1, 100) for _ in range(10)]
print(lista)
print(lista[::-1])
