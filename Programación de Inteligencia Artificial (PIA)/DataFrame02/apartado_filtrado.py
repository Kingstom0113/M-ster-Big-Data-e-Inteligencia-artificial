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

# 1. Filtrar los suspensos en alguna de las materias
suspensos = df_alumnos[
    (df_alumnos["BD"] < 5) |
    (df_alumnos["PR"] < 5) |
    (df_alumnos["SI"] < 5) |
    (df_alumnos["LM"] < 5) |
    (df_alumnos["ED"] < 5)
]
print("Suspensos en alguna materia:")
print(suspensos)

# 2. Filtrar los suspensos en la asignatura de Programación
suspensos_programacion = df_alumnos[df_alumnos["PR"] < 5]
print("\nSuspensos en la asignatura de Programación:")
print(suspensos_programacion)

# 3. Filtrar las notas sobresalientes en cada materia (nota superior al 9)
sobresalientes = df_alumnos[
    (df_alumnos["BD"] > 9) |
    (df_alumnos["PR"] > 9) |
    (df_alumnos["SI"] > 9) |
    (df_alumnos["LM"] > 9) |
    (df_alumnos["ED"] > 9)
]
print("\nNotas sobresalientes en alguna materia:")
print(sobresalientes)

# 4. Filtrar los resultados para los alumnos “Marta Vargas” y “Carmen Ruiz”
alumnos_especificos = df_alumnos[
    df_alumnos["Alumno"].isin(["Marta Vargas", "Carmen Ruiz"])
]
print("\nResultados de Marta Vargas y Carmen Ruiz:")
print(alumnos_especificos)
