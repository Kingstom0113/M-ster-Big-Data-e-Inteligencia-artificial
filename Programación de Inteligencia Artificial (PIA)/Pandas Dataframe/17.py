import pandas as pd

# Cargar el archivo CSV en un DataFrame
ruta_archivo_csv = '14.csv'  # Cambia esto por la ruta de tu archivo CSV
df_alumnos = pd.read_csv(ruta_archivo_csv)

# Mostrar las primeras filas para verificar la estructura del DataFrame
print(df_alumnos.head())

# Calcular el promedio general de las notas por alumno (usando las columnas de notas)
# Suponiendo que las notas están en las columnas de 'Programación', 'Base de Datos', 'Lenguajes', 'Sistemas', 'Entornos'
columnas_notas = [
    'Programación T1', 'Programación T2', 'Programación T3',
    'Base de Datos T1', 'Base de Datos T2', 'Base de Datos T3',
    'Lenguajes T1', 'Lenguajes T2', 'Lenguajes T3',
    'Sistemas T1', 'Sistemas T2', 'Sistemas T3',
    'Entornos T1', 'Entornos T2', 'Entornos T3'
]

# Calcular el promedio de las notas por alumno
df_alumnos['Promedio General'] = df_alumnos[columnas_notas].mean(axis=1)

# Añadir la columna de grupo de honor
df_alumnos['Grupo de Honor'] = df_alumnos['Promedio General'].apply(lambda x: 'Sí' if x > 9 else 'No')

# Guardar el DataFrame actualizado en un nuevo archivo CSV
ruta_archivo_nuevo_csv = '17.csv'  # Cambia esto por la ruta donde deseas guardar el archivo CSV
df_alumnos.to_csv(ruta_archivo_nuevo_csv, index=False)

print(f"Archivo CSV con la nueva columna 'Grupo de Honor' guardado en: {ruta_archivo_nuevo_csv}")
