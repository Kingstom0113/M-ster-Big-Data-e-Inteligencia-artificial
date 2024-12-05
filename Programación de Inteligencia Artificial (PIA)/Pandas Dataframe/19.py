import pandas as pd

# Cargar los dos archivos Excel en DataFrames
ruta_archivo_excel_1 = '13.xlsx'  # Cambia esto por la ruta de tu primer archivo Excel
ruta_archivo_excel_2 = 'datos_alumnos.xlsx'

df_1 = pd.read_excel(ruta_archivo_excel_1)
df_2 = pd.read_excel(ruta_archivo_excel_2)

# Mostrar las primeras filas de ambos DataFrames para verificar su estructura
print("Primer archivo:")
print(df_1.head())

print("\nSegundo archivo:")
print(df_2.head())

# Fusionar los dos DataFrames basados en una columna común (por ejemplo, 'Correo' o 'ID')
# Asegúrate de que las columnas a fusionar existan en ambos DataFrames
df_combinado = pd.merge(df_1, df_2, on='Correo', how='outer')

# Guardar el DataFrame combinado en un nuevo archivo Excel
ruta_archivo_excel_combinado = 'ruta/del/archivo_combinado.xlsx'  # Cambia esto por la ruta donde quieres guardar el archivo Excel
df_combinado.to_excel(ruta_archivo_excel_combinado, index=False)

print(f"\nArchivo Excel combinado guardado en: {ruta_archivo_excel_combinado}")
