# -*- coding: utf-8 -*-

#  Crea una lista de palabras y usa map() para convertirlas a may�sculas

lista = ['hola', 'mundo', 'python', 'programacion']
resultado = list(map(lambda x: x.upper(), lista))

print(resultado)
