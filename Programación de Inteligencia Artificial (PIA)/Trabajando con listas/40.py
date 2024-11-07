# Divide una lista en partes iguales, p.e. , una lista de 12 elementos en 3 listas de 4.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
partes = [lista[i:i+4] for i in range(0, len(lista), 4)]

for i in partes:
    print(i)
