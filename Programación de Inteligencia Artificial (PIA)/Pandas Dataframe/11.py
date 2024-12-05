import pandas as pd

# Cargar el archivo Excel en un DataFrame
ruta_archivo = 'datos_alumnos.xlsx'
df_alumnos = pd.read_excel(ruta_archivo)

# Mostrar los primeros 5 registros
print(df_alumnos.head())
