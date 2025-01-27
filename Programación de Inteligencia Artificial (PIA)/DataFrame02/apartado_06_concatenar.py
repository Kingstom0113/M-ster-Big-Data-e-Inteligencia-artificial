import pandas as pd
import numpy as np

# Nombres alumnos y generación de notas
nombres_alumnos = [
    "Juan Pérez", "María López", "Carlos García", "Ana Fernández",
    "Luis Martínez", "Sofía Gómez", "Miguel Rodríguez", "Laura Sánchez",
    "José Torres", "Lucía Morales", "Andrés Herrera", "Carmen Ruiz",
    "Raúl Castro", "Elena Jiménez", "Javier Gil", "Isabel Romero",
    "Hugo Ortiz", "Sara Delgado", "Pablo Ramírez", "Marta Vargas"
]
notas = {
    "Alumno": nombres_alumnos,
    "BD": np.random.uniform(1, 10, 20).round(1),
    "PR": np.random.uniform(1, 10, 20).round(1),
    "SI": np.random.uniform(1, 10, 20).round(1),
    "LM": np.random.uniform(1, 10, 20).round(1),
    "ED": np.random.uniform(1, 10, 20).round(1),
}
df_alumnos = pd.DataFrame(notas)

# Generar un nuevo DataFrame con datos faltantes
df_incompleto = df_alumnos.copy()
df_incompleto.loc[
    np.random.choice(df_incompleto.index, 5), 
    np.random.choice(["BD", "PR", "SI", "LM", "ED"], 3)
] = np.nan

print("\nNuevo DataFrame con datos faltantes:")
print(df_incompleto)

# Concatenar manteniendo los datos nulos (NaN)
df_concatenado = pd.concat([df_alumnos, df_incompleto], ignore_index=True)
print("\nConcatenación con datos nulos (NaN) mantenidos:")
print(df_concatenado)

# Eliminar los registros que no dispongan de datos (NaN)
df_sin_nulos = df_concatenado.dropna()
print("\nConcatenación eliminando registros con datos faltantes (NaN):")
print(df_sin_nulos)
