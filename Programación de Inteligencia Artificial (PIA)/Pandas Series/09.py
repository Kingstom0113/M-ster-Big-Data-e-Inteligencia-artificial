import pandas as pd
import matplotlib.pyplot as plt

# Ejercicio 9: Registro de Visitas a una Página Web

# Solicitar el número de visitas diarias durante 10 días
print("Por favor, ingresa el número de visitas diarias a una página web durante 10 días:")

# Nombres de los días
dias = ['Día 1', 'Día 2', 'Día 3', 'Día 4', 'Día 5', 'Día 6', 'Día 7', 'Día 8', 'Día 9', 'Día 10']
visitas = []

for dia in dias:
    while True:
        try:
            visitas_diarias = input(f"Visitas en {dia}: ")
            visitas_diarias = int(visitas_diarias)
            if visitas_diarias < 0:
                raise ValueError("El número de visitas no puede ser negativo.")
            visitas.append(visitas_diarias)
            break
        except ValueError as e:
            print(f"Entrada inválida. {e}. Inténtalo de nuevo.")

# Crear una Serie con los datos de visitas
serie_visitas = pd.Series(visitas, index=dias)

# Calcular el total y el promedio de visitas diarias
total_visitas = serie_visitas.sum()
promedio_visitas = serie_visitas.mean()

# Mostrar los días con más visitas que el promedio
dias_con_mas_visitas = serie_visitas[serie_visitas > promedio_visitas]

# Reemplazar las visitas menores a 50 con "Baja visita"
serie_actualizada = serie_visitas.replace({x: 'Baja visita' for x in serie_visitas[serie_visitas < 50]})

# Mostrar resultados
print("\n--- Resultados ---")
print(f"Total de visitas: {total_visitas}")
print(f"Promedio de visitas: {promedio_visitas:.2f}")
print("\nDías con más visitas que el promedio:")
print(dias_con_mas_visitas)

print("\nVisitas actualizadas (visitas < 50 reemplazadas con 'Baja visita'):")
print(serie_actualizada)

# Graficar el número de visitas diarias
plt.figure(figsize=(10, 6))
serie_visitas.plot(kind='bar', color='lightblue', edgecolor='black')
plt.title("Número de Visitas Diarias a la Página Web")
plt.xlabel("Días")
plt.ylabel("Visitas")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
