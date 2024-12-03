import pandas as pd

# Ejercicio 10: Análisis de Puntuaciones de Juegos

# Solicitar las puntuaciones del jugador en 8 rondas
print("Por favor, ingresa las puntuaciones del jugador en 8 rondas de un juego:")

# Números de rondas
rondas = ['Ronda 1', 'Ronda 2', 'Ronda 3', 'Ronda 4', 'Ronda 5', 'Ronda 6', 'Ronda 7', 'Ronda 8']
puntuaciones = []

for ronda in rondas:
    while True:
        try:
            puntuacion = input(f"Puntuación en {ronda}: ")
            puntuacion = int(puntuacion)
            if puntuacion < 0:
                raise ValueError("La puntuación no puede ser negativa.")
            puntuaciones.append(puntuacion)
            break
        except ValueError as e:
            print(f"Entrada inválida. {e}. Inténtalo de nuevo.")

# Crear una Serie con las puntuaciones
serie_puntuaciones = pd.Series(puntuaciones, index=rondas)

# Calcular la puntuación máxima, mínima y la diferencia entre la más alta y la más baja
puntuacion_maxima = serie_puntuaciones.max()
puntuacion_minima = serie_puntuaciones.min()
diferencia_max_min = puntuacion_maxima - puntuacion_minima

# Mostrar las rondas con puntuación superior a 80
rondas_superiores_a_80 = serie_puntuaciones[serie_puntuaciones > 80]

# Ordenar las puntuaciones de menor a mayor y mostrar el ranking
ranking = serie_puntuaciones.sort_values()

# Mostrar resultados
print("\n--- Resultados ---")
print(f"Puntuación máxima: {puntuacion_maxima}")
print(f"Puntuación mínima: {puntuacion_minima}")
print(f"Diferencia entre la puntuación máxima y mínima: {diferencia_max_min}")
print("\nRondas con puntuación superior a 80:")
print(rondas_superiores_a_80)

print("\nRanking de puntuaciones (de menor a mayor):")
print(ranking)
