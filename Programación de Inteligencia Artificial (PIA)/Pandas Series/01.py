import pandas as pd

# Ejercicio 1: Análisis de Ventas de una Semana

# Solicitar al usuario las ventas diarias de una semana
ventas_diarias = []
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

print("Por favor, ingresa las ventas de cada día de la semana:")

for dia in dias:
    venta = float(input(f"Ventas del {dia}: "))
    ventas_diarias.append(venta)

# Crear una Serie con los datos proporcionados
ventas = pd.Series(ventas_diarias, index=dias)

# Realizar el análisis
total_ventas = ventas.sum()
promedio_ventas = ventas.mean()
dia_mayores_ventas = ventas.idxmax()

# Visualizar los días con ventas por encima del promedio
ventas_sobre_promedio = ventas[ventas > promedio_ventas]

# Mostrar los resultados
print("\n--- Análisis de Ventas ---")
print(f"Total de ventas en la semana: {total_ventas}")
print(f"Promedio de ventas diarias: {promedio_ventas:.2f}")
print(f"Día con las mayores ventas: {dia_mayores_ventas}")
print("\nDías con ventas por encima del promedio:")
print(ventas_sobre_promedio)
