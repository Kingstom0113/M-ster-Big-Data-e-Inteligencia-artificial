import pandas as pd

# Leer los datos desde el archivo Excel
ruta_archivo = "datos_alumnos.xlsx"
df_alumnos = pd.read_excel(ruta_archivo)

# Calcular el promedio de notas finales para cada alumno
df_alumnos["Nota Final Programación"] = df_alumnos[["Programación T1", "Programación T2", "Programación T3"]].mean(axis=1)
df_alumnos["Nota Final Base de Datos"] = df_alumnos[["Base de Datos T1", "Base de Datos T2", "Base de Datos T3"]].mean(axis=1)
df_alumnos["Nota Final Lenguajes"] = df_alumnos[["Lenguajes T1", "Lenguajes T2", "Lenguajes T3"]].mean(axis=1)
df_alumnos["Nota Final Sistemas"] = df_alumnos[["Sistemas T1", "Sistemas T2", "Sistemas T3"]].mean(axis=1)
df_alumnos["Nota Final Entornos"] = df_alumnos[["Entornos T1", "Entornos T2", "Entornos T3"]].mean(axis=1)

# Filtrar a los alumnos con 20 años o más
alumnos_mayores_20 = df_alumnos[df_alumnos["Edad"] >= 20]

# Mostrar las notas finales de los alumnos filtrados
resultados = alumnos_mayores_20[[
    "Nombre", "Apellidos", "Edad",
    "Nota Final Programación", "Nota Final Base de Datos",
    "Nota Final Lenguajes", "Nota Final Sistemas", "Nota Final Entornos"
]]

print(resultados)
