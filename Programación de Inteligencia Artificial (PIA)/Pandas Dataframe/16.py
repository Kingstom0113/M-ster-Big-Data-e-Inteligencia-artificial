import pandas as pd

# Cargar el archivo CSV en un DataFrame
ruta_archivo_csv = '14.csv'  # Cambia esto por la ruta de tu archivo CSV
df_alumnos = pd.read_csv(ruta_archivo_csv)

# Mostrar las primeras filas para verificar la estructura del DataFrame
print(df_alumnos.head())

# Agrupar por 'Edad' y calcular el promedio de las notas de cada grupo
# Aquí se calcula el promedio de todas las columnas numéricas por edad
df_promedio_edad = df_alumnos.groupby('Edad').mean()

# Guardar el DataFrame resultante en un nuevo archivo Excel
ruta_archivo_nuevo_excel = '16.xlsx'  # Cambia esto por la ruta donde quieres guardar el archivo Excel
df_promedio_edad.to_excel(ruta_archivo_nuevo_excel)

print(f"Archivo Excel con el promedio por edad guardado en: {ruta_archivo_nuevo_excel}")
