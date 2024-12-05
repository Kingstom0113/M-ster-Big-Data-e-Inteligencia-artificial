import pandas as pd

# Cargar el archivo CSV en un DataFrame
ruta_archivo_csv = '14.csv'  # Cambia esto por la ruta de tu archivo CSV
df_alumnos = pd.read_csv(ruta_archivo_csv)

# Mostrar las primeras filas para verificar la estructura del DataFrame
print(df_alumnos.head())

# Calcular el promedio de las notas de un módulo específico
# Por ejemplo, calcular el promedio de las notas en 'Programación T1'
promedio_programacion_t1 = df_alumnos['Programación T1'].mean()

# Mostrar el resultado
print(f"El promedio de las notas en 'Programación T1' es: {promedio_programacion_t1}")
