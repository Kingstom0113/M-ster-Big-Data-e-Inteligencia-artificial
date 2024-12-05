import pandas as pd
import random

# Cargar el archivo Excel en un DataFrame
ruta_archivo_excel = 'datos_alumnos.xlsx'  # Cambia esto por la ruta de tu archivo Excel
df_alumnos = pd.read_excel(ruta_archivo_excel)

# Mostrar las primeras filas para entender la estructura
print(df_alumnos.head())

# Modificar las notas de los alumnos en el DataFrame
# Ejemplo: Modificar las notas de 'Programación T1' a una nueva nota aleatoria entre 5 y 10
df_alumnos['Programación T1'] = [random.randint(5, 10) for _ in range(len(df_alumnos))]

# Guardar el DataFrame actualizado en un nuevo archivo CSV
ruta_archivo_nuevo_csv = '14.csv'  # Cambia esto por la ruta donde deseas guardar el archivo CSV
df_alumnos.to_csv(ruta_archivo_nuevo_csv, index=False)

print(f"Archivo CSV con las notas modificadas guardado en: {ruta_archivo_nuevo_csv}")
