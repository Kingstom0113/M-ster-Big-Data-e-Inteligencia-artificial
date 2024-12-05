import pandas as pd

# Cargar el archivo Excel en un DataFrame
ruta_archivo_excel = 'datos_alumnos.xlsx'
df_alumnos = pd.read_excel(ruta_archivo_excel)

# Filtrar a los alumnos cuya edad es mayor a 22
df_filtrado = df_alumnos[df_alumnos['Edad'] > 22]

# Guardar el DataFrame filtrado en un nuevo archivo Excel
ruta_archivo_nuevo_excel = '13.xlsx'  # Cambia esto por la ruta donde quieres guardar el archivo
df_filtrado.to_excel(ruta_archivo_nuevo_excel, index=False)

print(f"Archivo filtrado guardado en: {ruta_archivo_nuevo_excel}")
