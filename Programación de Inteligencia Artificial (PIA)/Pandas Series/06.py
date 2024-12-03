import pandas as pd
import matplotlib.pyplot as plt

# Ejercicio 6: Evaluación de Encuesta de Satisfacción

# Solicitar las calificaciones de satisfacción de 12 clientes
print("Por favor, ingresa las calificaciones de satisfacción (de 1 a 5) de 12 clientes:")

calificaciones = []
for i in range(1, 13):
    while True:
        try:
            calificacion = int(input(f"Calificación del cliente {i} (1-5): "))
            if calificacion < 1 or calificacion > 5:
                raise ValueError("La calificación debe estar entre 1 y 5.")
            calificaciones.append(calificacion)
            break
        except ValueError as e:
            print(e)

# Crear una Serie con las calificaciones
serie_calificaciones = pd.Series(calificaciones)

# Calcular la frecuencia de cada calificación
frecuencia = serie_calificaciones.value_counts().sort_index()

# Calcular el porcentaje de clientes satisfechos (calificación ≥ 4)
satisfechos = serie_calificaciones[serie_calificaciones >= 4].count()
porcentaje_satisfechos = (satisfechos / len(serie_calificaciones)) * 100

# Reemplazar cualquier calificación de 1 con "Insatisfecho"
serie_actualizada = serie_calificaciones.replace(1, "Insatisfecho")

# Mostrar los resultados
print("\n--- Resultados ---")
print(f"Frecuencia de calificaciones:")
print(frecuencia)
print(f"\nPorcentaje de clientes satisfechos (calificación ≥ 4): {porcentaje_satisfechos:.2f}%")
print("\nCalificaciones actualizadas:")
print(serie_actualizada)

# Graficar las calificaciones en un gráfico de barras
plt.figure(figsize=(8, 5))
frecuencia.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Frecuencia de Calificaciones de Satisfacción")
plt.xlabel("Calificación")
plt.ylabel("Frecuencia")
plt.xticks(range(1, 6), labels=['1', '2', '3', '4', '5'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
