import pandas as pd
import matplotlib.pyplot as plt

# Ejercicio 3: Análisis de Temperaturas Semanales

# Solicitar al usuario las temperaturas registradas en una semana
print("Por favor, ingresa las temperaturas registradas en una semana (usa 'NaN' si falta algún dato):")

dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
temperaturas = []

for dia in dias:
    temp = input(f"Temperatura del {dia}: ")
    # Convertir a float o dejar como NaN si el usuario ingresa 'NaN'
    if temp.lower() == 'nan':
        temperaturas.append(float('nan'))
    else:
        temperaturas.append(float(temp))

# Crear una Serie con las temperaturas y los días como índice
serie_temperaturas = pd.Series(temperaturas, index=dias)

# Calcular temperatura máxima y mínima
temp_max = serie_temperaturas.max()
temp_min = serie_temperaturas.min()

# Identificar días con temperaturas por encima de 25°C
dias_calidos = serie_temperaturas[serie_temperaturas > 25]

# Rellenar valores faltantes (NaN) con la temperatura promedio
promedio_temp = serie_temperaturas.mean(skipna=True)
serie_temperaturas_filled = serie_temperaturas.fillna(promedio_temp)

# Mostrar los resultados
print("\n--- Análisis de Temperaturas ---")
print(f"Temperatura máxima: {temp_max:.2f}°C")
print(f"Temperatura mínima: {temp_min:.2f}°C")
print("\nDías con temperaturas por encima de 25°C:")
print(dias_calidos)
print("\nTemperaturas después de rellenar valores faltantes:")
print(serie_temperaturas_filled)

# Graficar las temperaturas
plt.figure(figsize=(8, 5))
serie_temperaturas_filled.plot(kind='line', marker='o', color='blue', label='Temperatura')
plt.title("Temperaturas Semanales")
plt.xlabel("Días de la semana")
plt.ylabel("Temperatura (°C)")
plt.xticks(rotation=45)
plt.axhline(y=promedio_temp, color='red', linestyle='--', label=f"Promedio ({promedio_temp:.2f}°C)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
