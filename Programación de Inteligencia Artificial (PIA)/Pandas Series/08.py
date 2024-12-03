import pandas as pd

# Ejercicio 8: Análisis de Datos Meteorológicos

# Solicitar las precipitaciones registradas durante los últimos 7 días
print("Por favor, ingresa las precipitaciones registradas durante los últimos 7 días (en mm):")

# Nombres de los días de la semana
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
precipitaciones = []

for dia in dias:
    while True:
        try:
            precipitacion = input(f"Precipitación en {dia}: ")
            if precipitacion.lower() == 'nan':  # Permitir ingresar 'NaN' si faltan datos
                precipitaciones.append(float('nan'))
                break
            precipitacion = float(precipitacion)
            if precipitacion < 0:
                raise ValueError("La precipitación no puede ser negativa.")
            precipitaciones.append(precipitacion)
            break
        except ValueError as e:
            print(f"Entrada inválida. {e}. Inténtalo de nuevo.")

# Crear una Serie con los datos de precipitaciones
serie_precipitaciones = pd.Series(precipitaciones, index=dias)

# Reemplazar los días sin lluvia (0 mm) con "Sin precipitación"
serie_actualizada = serie_precipitaciones.replace(0, "Sin precipitación")

# Calcular el total y el promedio de precipitaciones
total_precipitaciones = serie_precipitaciones.sum()
promedio_precipitaciones = serie_precipitaciones.mean()

# Mostrar los días con precipitaciones por encima del promedio
dias_por_encima_del_promedio = serie_precipitaciones[serie_precipitaciones > promedio_precipitaciones]

# Mostrar los resultados
print("\n--- Resultados ---")
print(f"Total de precipitaciones: {total_precipitaciones:.2f} mm")
print(f"Promedio de precipitaciones: {promedio_precipitaciones:.2f} mm")
print("\nDías con precipitación por encima del promedio:")
print(dias_por_encima_del_promedio)

print("\nDías actualizados (sin lluvia reemplazados por 'Sin precipitación'):")
print(serie_actualizada)
