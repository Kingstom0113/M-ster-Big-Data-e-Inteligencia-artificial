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

# Pivotar la tabla
df_pivotado = df_alumnos.melt(
    id_vars=["Alumno"],
    var_name="Asignatura",
    value_name="Nota"
)
print("Tabla pivotada:")
print(df_pivotado)
