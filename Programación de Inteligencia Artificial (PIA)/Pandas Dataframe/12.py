import pandas as pd

# Cargar el archivo Excel en un DataFrame
ruta_archivo_excel = 'datos_alumnos.xlsx'
df_alumnos = pd.read_excel(ruta_archivo_excel)

# Guardar el DataFrame como un archivo CSV
ruta_archivo_csv = '12.csv'  
df_alumnos.to_csv(ruta_archivo_csv, index=False)

print(f"Archivo guardado en formato CSV en: {ruta_archivo_csv}")
