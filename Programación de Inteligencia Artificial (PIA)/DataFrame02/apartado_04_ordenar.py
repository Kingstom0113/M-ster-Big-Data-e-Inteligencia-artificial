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

# Ordenar por nombre de alumno
orden_nombre = df_alumnos.sort_values(by="Alumno")
print("\nOrdenado por nombre de alumno:")
print(orden_nombre)

# Ordenar por Nota de Programación ascendente
orden_pr_asc = df_alumnos.sort_values(by="PR")
print("\nOrdenado por Nota de Programación (ascendente):")
print(orden_pr_asc)

# Ordenar por Nota de Base de Datos descendente
orden_bd_desc = df_alumnos.sort_values(by="BD", ascending=False)
print("\nOrdenado por Nota de Base de Datos (descendente):")
print(orden_bd_desc)
