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
