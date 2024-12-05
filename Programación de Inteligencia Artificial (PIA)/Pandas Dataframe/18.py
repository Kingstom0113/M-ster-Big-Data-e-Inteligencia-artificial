import pandas as pd

# Cargar el archivo Excel en un DataFrame
ruta_archivo_excel = 'datos_alumnos.xlsx'
df_alumnos = pd.read_excel(ruta_archivo_excel)

# Mostrar las primeras filas para verificar la estructura del DataFrame
print(df_alumnos.head())

# Calcular la nota mínima de cada módulo
# Seleccionamos las columnas de notas
columnas_notas = [
    'Programación T1', 'Programación T2', 'Programación T3',
    'Base de Datos T1', 'Base de Datos T2', 'Base de Datos T3',
    'Lenguajes T1', 'Lenguajes T2', 'Lenguajes T3',
    'Sistemas T1', 'Sistemas T2', 'Sistemas T3',
    'Entornos T1', 'Entornos T2', 'Entornos T3'
]

# Calcular la nota mínima de cada módulo
nota_minima_por_modulo = df_alumnos[columnas_notas].min()

# Guardar el resultado en un archivo CSV
ruta_archivo_csv = '18.csv'  # Cambia esto por la ruta donde quieres guardar el archivo CSV
nota_minima_por_modulo.to_csv(ruta_archivo_csv)

print(f"Archivo CSV con la nota mínima por módulo guardado en: {ruta_archivo_csv}")
