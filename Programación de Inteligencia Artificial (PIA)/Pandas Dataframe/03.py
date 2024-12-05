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

# Calcular el promedio general
df_alumnos["Promedio General"] = df_alumnos[
    ["Programación T1", "Programación T2", "Programación T3",
     "Base de Datos T1", "Base de Datos T2", "Base de Datos T3",
     "Lenguajes T1", "Lenguajes T2", "Lenguajes T3",
     "Sistemas T1", "Sistemas T2", "Sistemas T3",
     "Entornos T1", "Entornos T2", "Entornos T3"]
].mean(axis=1)

# Añadir la columna 'Aprobado'
df_alumnos["Aprobado"] = df_alumnos["Promedio General"] >= 5
df_alumnos["Aprobado"] = df_alumnos["Aprobado"].apply(lambda x: "Sí" if x else "No")

# Calcular la nota máxima por módulo
notas_maximas = {
    "Programación": df_alumnos[["Programación T1", "Programación T2", "Programación T3"]].max().max(),
    "Base de Datos": df_alumnos[["Base de Datos T1", "Base de Datos T2", "Base de Datos T3"]].max().max(),
    "Lenguajes": df_alumnos[["Lenguajes T1", "Lenguajes T2", "Lenguajes T3"]].max().max(),
    "Sistemas": df_alumnos[["Sistemas T1", "Sistemas T2", "Sistemas T3"]].max().max(),
    "Entornos": df_alumnos[["Entornos T1", "Entornos T2", "Entornos T3"]].max().max(),
}

# Mostrar las notas máximas
print("Nota máxima por módulo:")
for modulo, nota_max in notas_maximas.items():
    print(f"{modulo}: {nota_max}")

# Guardar el DataFrame actualizado en un archivo Excel
ruta_archivo = "datos_alumnos_con_aprobados.xlsx"
df_alumnos.to_excel(ruta_archivo, index=False)

# Mostrar un ejemplo del DataFrame generado
print("\nEjemplo del DataFrame:")
print(df_alumnos[["Nombre", "Apellidos", "Promedio General", "Aprobado"]].head())
