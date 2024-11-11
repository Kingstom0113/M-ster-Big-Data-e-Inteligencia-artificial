# -*- coding: utf-8 -*-

# Divide una lista de estudiantes en dos grupos de forma alterna (uno para cada grupo).

estudiantes = ['Juan', 'Maria', 'Luis', 'Ana', 'Pedro', 'Rosa']

grupo1 = estudiantes[::2]
grupo2 = estudiantes[1::2]

print(grupo1)
print(grupo2)
