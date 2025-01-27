import pandas as pd
import numpy as np

# Mostrar más filas y columnas
pd.set_option('display.max_rows', 300)
pd.set_option('display.max_columns', 500)

# Nombres alumnos
nombres_alumnos = [
    "Juan Pérez", "María López", "Carlos García", "Ana Fernández",
    "Luis Martínez", "Sofía Gómez", "Miguel Rodríguez", "Laura Sánchez",
    "José Torres", "Lucía Morales", "Andrés Herrera", "Carmen Ruiz",
    "Raúl Castro", "Elena Jiménez", "Javier Gil", "Isabel Romero",
    "Hugo Ortiz", "Sara Delgado", "Pablo Ramírez", "Marta Vargas"
]

# Generar notas aleatorias
notas = {
    "Alumno": nombres_alumnos,
    "Base de Datos": np.random.uniform(1, 10, 20).round(1),
    "Programación": np.random.uniform(1, 10, 20).round(1),
    "Sistemas Informáticos": np.random.uniform(1, 10, 20).round(1),
    "Lenguajes de Marcas": np.random.uniform(1, 10, 20).round(1),
    "Entornos de Desarrollo": np.random.uniform(1, 10, 20).round(1),
}

# Crear el DataFrame
df_alumnos = pd.DataFrame(notas)

# Renombrar las columnas de los módulos
df_alumnos.rename(
    columns={
        "Base de Datos": "BD",
        "Programación": "PR",
        "Sistemas Informáticos": "SI",
        "Lenguajes de Marcas": "LM",
        "Entornos de Desarrollo": "ED",
    },
    inplace=True
)

# -----------------------------------------------
# Apartado 03. Pivotar
# -----------------------------------------------
df_pivotado = df_alumnos.melt(
    id_vars=["Alumno"],
    var_name="Asignatura",
    value_name="Nota"
)
print("Tabla pivotada:")
print(df_pivotado)

# -----------------------------------------------
# Apartado 04. Ordenar
# -----------------------------------------------
# Ordenar por nombre de alumno
orden_nombre = df_alumnos.sort_values(by="Alumno")
print("\nOrdenado por nombre de alumno:")
print(orden_nombre)

# Ordenar por Nota de asignatura Programación ascendente
orden_pr_asc = df_alumnos.sort_values(by="PR")
print("\nOrdenado por Nota de Programación (ascendente):")
print(orden_pr_asc)

# Ordenar por Nota de asignatura Base de Datos descendente
orden_bd_desc = df_alumnos.sort_values(by="BD", ascending=False)
print("\nOrdenado por Nota de Base de Datos (descendente):")
print(orden_bd_desc)

# -----------------------------------------------
# Apartado 05. Agrupar
# -----------------------------------------------
# Promedio de notas de cada alumno
promedio_alumno = df_alumnos.set_index("Alumno").mean(axis=1)
print("\nPromedio de notas de cada alumno:")
print(promedio_alumno)

# Promedio de notas de cada materia
promedio_materia = df_alumnos.drop("Alumno", axis=1).mean()
print("\nPromedio de notas de cada materia:")
print(promedio_materia)

# Alumno con el mejor promedio
mejor_alumno = promedio_alumno.idxmax()
print("\nAlumno con el mejor promedio en todas las materias:")
print(mejor_alumno)

# -----------------------------------------------
# Apartado 06. Concatenar
# -----------------------------------------------
# Generar un nuevo DataFrame con datos faltantes
df_incompleto = df_alumnos.copy()
df_incompleto.loc[np.random.choice(df_incompleto.index, 5), np.random.choice(["BD", "PR", "SI", "LM", "ED"], 3)] = np.nan

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
