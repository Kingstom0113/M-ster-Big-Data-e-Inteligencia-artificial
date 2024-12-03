import pandas as pd

# Ejercicio 5: Inventario de Productos

# Solicitar al usuario las cantidades de 8 productos
print("Por favor, ingresa las cantidades de 8 productos en stock (usa 'NaN' si falta algún dato):")

nombres_productos = []
cantidades = []

for i in range(1, 9):
    nombre = input(f"Nombre del producto {i}: ")
    cantidad = input(f"Cantidad en stock de {nombre}: ")
    nombres_productos.append(nombre)
    # Convertir a float o asignar NaN si el usuario escribe 'NaN'
    if cantidad.lower() == 'nan':
        cantidades.append(float('nan'))
    else:
        cantidades.append(int(cantidad))

# Crear una Serie con los datos proporcionados
serie_inventario = pd.Series(cantidades, index=nombres_productos)

# Mostrar los productos con menos de 10 unidades
productos_bajo_stock = serie_inventario[serie_inventario < 10]

# Rellenar valores faltantes (NaN) con 0
serie_inventario_filled = serie_inventario.fillna(0)

# Ordenar los productos por cantidad en stock
productos_ordenados = serie_inventario_filled.sort_values()

# Mostrar resultados
print("\n--- Resultados ---")
print("\nProductos con menos de 10 unidades:")
print(productos_bajo_stock)

print("\nInventario después de rellenar valores faltantes:")
print(serie_inventario_filled)

print("\nProductos ordenados por cantidad en stock:")
print(productos_ordenados)
