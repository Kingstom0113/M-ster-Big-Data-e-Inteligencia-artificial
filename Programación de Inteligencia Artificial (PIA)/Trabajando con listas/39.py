# -*- coding: utf-8 -*-

# Crea una lista de n�meros e invierte el orden de los n�meros sin usar reverse().

import random

lista = [random.randint(1, 100) for _ in range(10)]
print(lista)
print(lista[::-1])
