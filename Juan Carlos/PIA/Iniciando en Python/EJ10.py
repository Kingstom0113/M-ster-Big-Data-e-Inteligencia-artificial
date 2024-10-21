# 1. Crear la lista 'números' con los valores dados
numeros = [12, 45, 78, 23, 56, 89, 23, 56]

# 2. Contar cuántas veces aparece el número 23 en la lista
conteo_23 = numeros.count(23)
print("El número 23 aparece:", conteo_23, "veces.")

# 3. Encontrar el índice de la primera aparición del número 56
indice_56 = numeros.index(56)
print("El índice de la primera aparición del número 56 es:", indice_56)

# 4. Eliminar el último número de la lista
numeros.pop()  # También se podría usar 'del numeros[-1]'

# 5. Usar el método extend() para agregar los valores [100, 200, 300] al final de la lista
numeros.extend([100, 200, 300])

# 6. Hacer una copia de la lista en una nueva variable llamada 'numeros_copia'
numeros_copia = numeros.copy()

# 7. Limpiar (vaciar) la lista original
numeros.clear()

# Imprimir resultados
print("Lista original después de limpiar:", numeros)
print("Copia de la lista:", numeros_copia)
