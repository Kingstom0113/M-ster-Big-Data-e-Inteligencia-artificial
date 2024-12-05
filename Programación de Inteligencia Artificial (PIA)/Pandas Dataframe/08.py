import pandas as pd
import random

# Generar datos aleatorios para los alumnos
nombres = ["Alejandro", "María", "Carlos", "Lucía", "José", "Ana", "Javier", "Laura",
           "Pablo", "Marta", "Sergio", "Elena", "Fernando", "Cristina", "David", 
           "Isabel", "Rubén", "Patricia", "Manuel", "Raquel"]
apellidos = ["García", "Martínez", "López", "Sánchez", "Pérez", "Gómez", "Fernández",
             "Díaz", "Ruiz", "Moreno", "Jiménez", "Álvarez", "Romero", "Vargas", 
             "Silva", "Castro", "Ortega", "Núñez", "Ramos", "Molina"]

data = []
for i in range(20):
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    correo = f"{nombre.lower()}.{apellido.lower()}@ejemplo.com"
    edad = random.randint(18, 25)
    programacion = [random.randint(0, 10) for _ in range(3)]  # Notas de Programación
    base_datos = [random.randint(0, 10) for _ in range(3)]    # Notas de Base de Datos
    lenguajes = [random.randint(0, 10) for _ in range(3)]     # Notas de Lenguajes
    sistemas = [random.randint(0, 10) for _ in range(3)]      # Notas de Sistemas
    entornos = [random.randint(0, 10) for _ in range(3)]      # Notas de Entornos

    # Agregar todos los datos a una fila
    data.append([nombre, apellido, correo, edad] + programacion + base_datos + lenguajes + sistemas + entornos)

# Definir columnas del DataFrame
columnas = [
    "Nombre", "Apellidos", "Correo", "Edad",
    "Programación T1", "Programación T2", "Programación T3",
    "Base de Datos T1", "Base de Datos T2", "Base de Datos T3",
    "Lenguajes T1", "Lenguajes T2", "Lenguajes T3",
    "Sistemas T1", "Sistemas T2", "Sistemas T3",
    "Entornos T1", "Entornos T2", "Entornos T3"
]

# Crear el DataFrame
df_alumnos = pd.DataFrame(data, columns=columnas)

# Verificar si algún módulo está reprobado (nota < 5)
# Creamos una nueva columna que indicará si el alumno ha reprobado algún módulo
df_alumnos["Reprobado"] = (
    (df_alumnos[["Programación T1", "Programación T2", "Programación T3"]].lt(5)).any(axis=1) |
    (df_alumnos[["Base de Datos T1", "Base de Datos T2", "Base de Datos T3"]].lt(5)).any(axis=1) |
    (df_alumnos[["Lenguajes T1", "Lenguajes T2", "Lenguajes T3"]].lt(5)).any(axis=1) |
    (df_alumnos[["Sistemas T1", "Sistemas T2", "Sistemas T3"]].lt(5)).any(axis=1) |
    (df_alumnos[["Entornos T1", "Entornos T2", "Entornos T3"]].lt(5)).any(axis=1)
)

# Filtrar los alumnos que han reprobado al menos un módulo
alumnos_reprobados = df_alumnos[df_alumnos["Reprobado"] == True]

# Exportar los alumnos reprobados a un archivo CSV
ruta_archivo_csv = "alumnos_reprobados.csv"
alumnos_reprobados.to_csv(ruta_archivo_csv, index=False)

# Mostrar un mensaje de confirmación
print(f"Los alumnos que han reprobado al menos un módulo se han exportado a {ruta_archivo_csv}.")
