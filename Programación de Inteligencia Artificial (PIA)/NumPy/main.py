# Manuel Soto Romero
# Tarea - Ejercicios NumPy

import numpy as np

# 1. Crear un vector con valores dentro del rango 10-49
vector = np.arange(10, 50)
print("\n1. Vector con valores de 10 a 49:\n", vector)

# 2. Invertir vector
vector_invertido = vector[::-1]
print("\n2. Vector invertido:\n", vector_invertido)

# 3. Crear un array de 10 ceros
array_ceros = np.zeros(10)
print("\n3. Array de 10 ceros:\n", array_ceros)

# 4. Crear un array de 10 unos
array_unos = np.ones(10)
print("\n4. Array de 10 unos:\n", array_unos)

# 5. Crear matriz 3x3 con valores del 0 a 8
matriz_3x3 = np.arange(9).reshape(3, 3)
print("\n5. Matriz 3x3 con valores del 0 al 8:\n", matriz_3x3)

# 6. Crear un array de 10 cincos
array_cincos = np.full(10, 5)
print("\n6. Array de 10 cincos:\n", array_cincos)

# 7. Transformar el array anterior a dimensiones [2,5] y [5,2]
array_2x5 = array_cincos.reshape(2, 5)
array_5x2 = array_cincos.reshape(5, 2)
print("\n7. Array transformado a 2x5:\n", array_2x5)
print("Array transformado a 5x2:\n", array_5x2)

# 8. Encontrar los índices (no el valor) que no son cero dentro del siguiente array
array_indices = [1, 2, 4, 2, 4, 0, 1, 0, 0, 0, 12, 4, 5, 6, 7, 0]
indices_no_cero = np.nonzero(array_indices)
print("\n8. Índices que no son cero:\n", indices_no_cero[0])

# 9. Crear una matriz identidad 6x6
matriz_identidad = np.eye(6)
print("\n9. Matriz identidad 6x6:\n", matriz_identidad)

# 10. Crear vector con 100 valores aleatorios de formato entero
vector_aleatorio = np.random.randint(0, 100, 100)
print("\n10. Vector de 100 valores aleatorios:\n", vector_aleatorio)

# 11. Crear un array con valores al azar de forma 3x3x3
array_3x3x3 = np.random.random((3, 3, 3))
print("\n11. Array 3x3x3 de valores aleatorios:\n", array_3x3x3)

# 12. Encontrar los valores mínimos y máximos del array anterior
valor_min = array_3x3x3.min()
valor_max = array_3x3x3.max()
print("\n12. Valor mínimo:", valor_min)
print("Valor máximo:", valor_max)

# 13. Indicar los índices (posición) de los valores mínimos y máximos del array
indice_min = np.unravel_index(np.argmin(array_3x3x3), array_3x3x3.shape)
indice_max = np.unravel_index(np.argmax(array_3x3x3), array_3x3x3.shape)
print("\n13. Índice del valor mínimo:", indice_min)
print("Índice del valor máximo:", indice_max)

# 14. Generar una matriz de tamaño 10x10 en la que los bordes sean 1 y el interior ceros
matriz_bordes = np.ones((10, 10))
matriz_bordes[1:-1, 1:-1] = 0
print("\n14. Matriz 10x10 con bordes 1 y el interior ceros:\n", matriz_bordes)

# 15. Crear array de tamaño 5x5 con los siguientes valores: [0,1,2,3,4]
array_5x5 = np.tile(np.arange(5), (5, 1))
print("\n15. Array 5x5 con valores [0,1,2,3,4]:\n", array_5x5)

# 16. Crear dos arrays aleatorios del mismo tamaño (3x3 o 5x5) y verificar si son iguales
array1 = np.random.randint(0, 10, (3, 3))
array2 = np.random.randint(0, 10, (3, 3))
son_iguales = np.array_equal(array1, array2)
coincidencias = array1 == array2
print("\n16. Array 1:\n", array1)
print("Array 2:\n", array2)
print("Los arrays son iguales:", son_iguales)
print("Coincidencias elemento a elemento:\n", coincidencias)

# 17. Generar array de dimensión 5x5 en el que los elementos sean de tipo numérico entero aleatorio comprendido entre el 1 y 100
matriz_5x5 = np.random.randint(1, 101, (5, 5))
print("\n17. Matriz 5x5 de enteros aleatorios entre 1 y 100:\n", matriz_5x5)

# 18. Obtener la suma total de la matriz 5x5
suma_total = matriz_5x5.sum()
print("\n18. Suma total de la matriz 5x5:", suma_total)

# 19. Obtener un nuevo array que contenga la suma de cada una de las columnas
suma_columnas = matriz_5x5.sum(axis=0)
print("\n19. Suma de cada columna de la matriz 5x5:\n", suma_columnas)

# 20. Extraer fila inicial, fila intermedia (fila 3) y la última fila de la matriz 5x5
fila_inicial = matriz_5x5[0, :]
fila_intermedia = matriz_5x5[2, :]
fila_final = matriz_5x5[-1, :]
print("\n20. Fila inicial:\n", fila_inicial)
print("Fila intermedia (fila 3):\n", fila_intermedia)
print("Fila final:\n", fila_final)
