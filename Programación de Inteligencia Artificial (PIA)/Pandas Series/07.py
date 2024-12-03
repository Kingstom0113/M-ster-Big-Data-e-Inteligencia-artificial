import pandas as pd
import matplotlib.pyplot as plt

# Ejercicio 7: Análisis de Precio de un Producto en Tiendas

# Solicitar al usuario que ingrese los precios del producto en 5 tiendas
print("Por favor, ingresa los precios del producto en 5 tiendas diferentes:")

tiendas = ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4', 'Tienda 5']
precios = []

for tienda in tiendas:
    while True:
        try:
            precio = input(f"Precio en {tienda}: ")
            if precio.lower() == 'nan':  # Permitir ingresar 'NaN' para valores faltantes
                precios.append(float('nan'))
                break
            precio = float(precio)
            if precio < 0:
                raise ValueError("El precio no puede ser negativo.")
            precios.append(precio)
            break
        except ValueError as e:
            print(f"Entrada inválida. {e}. Inténtalo de nuevo.")

# Crear una Serie con los precios
serie_precios = pd.Series(precios, index=tiendas)

# Mostrar el precio más bajo y más alto
precio_minimo = serie_precios.min()
precio_maximo = serie_precios.max()

# Calcular la mediana de los precios
mediana_precio = serie_precios.median()

# Identificar las tiendas con precios por encima de la mediana
tiendas_encima_de_mediana = serie_precios[serie_precios > mediana_precio]

# Rellenar los precios faltantes (NaN) con el precio promedio
precio_promedio = serie_precios.mean()
serie_precios_filled = serie_precios.fillna(precio_promedio)

# Mostrar resultados
print("\n--- Resultados ---")
print(f"Precio más bajo: {precio_minimo:.2f}")
print(f"Precio más alto: {precio_maximo:.2f}")
print(f"Mediana de los precios: {mediana_precio:.2f}")
print("\nTiendas con precios por encima de la mediana:")
print(tiendas_encima_de_mediana)

print("\nPrecios después de rellenar los valores faltantes con el precio promedio:")
print(serie_precios_filled)

# Graficar los precios
plt.figure(figsize=(8, 5))
serie_precios_filled.plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title("Precios del Producto en Diferentes Tiendas")
plt.xlabel("Tiendas")
plt.ylabel("Precio")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
