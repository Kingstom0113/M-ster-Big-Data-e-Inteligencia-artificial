# -*- coding: utf-8 -*-

# Encuentra los duplicados en una lista de números y elimina las repeticiones.

import random

lista = [random.randint(1, 10) for _ in range(10)]
print(lista)
duplicados = list(set([numero for numero in lista if lista.count(numero) > 1]))

print(duplicados)
