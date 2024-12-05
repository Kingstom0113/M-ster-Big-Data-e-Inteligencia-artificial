import pandas as pd
import random

# Lista de nombres y apellidos
nombres = ["Alejandro", "María", "Carlos", "Lucía", "José", "Ana", "Javier", "Laura",
           "Pablo", "Marta", "Sergio", "Elena", "Fernando", "Cristina", "David", 
           "Isabel", "Rubén", "Patricia", "Manuel", "Raquel"]
apellidos = ["García", "Martínez", "López", "Sánchez", "Pérez", "Gómez", "Fernández",
             "Díaz", "Ruiz", "Moreno", "Jiménez", "Álvarez", "Romero", "Vargas", 
             "Silva", "Castro", "Ortega", "Núñez", "Ramos", "Molina"]

# Generar datos para los alumnos
data = []
for i in range(20):
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    correo = f"{nombre.lower()}.{apellido.lower()}@ejemplo.com"
    edad = random.randint(18, 25)
    programacion = [random.randint(0, 10) for _ in range(3)]  # Notas de 3 trimestres
    base_datos = [random.randint(0, 10) for _ in range(3)]
    lenguajes = [random.randint(0, 10) for _ in range(3)]
    sistemas = [random.randint(0, 10) for _ in range(3)]
    entornos = [random.randint(0, 10) for _ in range(3)]
    
    # Concatenar los datos en una fila
    data.append([nombre, apellido, correo, edad] + programacion + base_datos + lenguajes + sistemas + entornos)

# Crear el DataFrame
columnas = [
    "Nombre", "Apellidos", "Correo", "Edad",
    "Programación T1", "Programación T2", "Programación T3",
    "Base de Datos T1", "Base de Datos T2", "Base de Datos T3",
    "Lenguajes T1", "Lenguajes T2", "Lenguajes T3",
    "Sistemas T1", "Sistemas T2", "Sistemas T3",
    "Entornos T1", "Entornos T2", "Entornos T3"
]
df_alumnos = pd.DataFrame(data, columns=columnas)

# Calcular el promedio general de cada alumno
df_alumnos["Promedio General"] = df_alumnos[
    ["Programación T1", "Programación T2", "Programación T3",
     "Base de Datos T1", "Base de Datos T2", "Base de Datos T3",
     "Lenguajes T1", "Lenguajes T2", "Lenguajes T3",
     "Sistemas T1", "Sistemas T2", "Sistemas T3",
     "Entornos T1", "Entornos T2", "Entornos T3"]
].mean(axis=1)

# Añadir la columna 'Aprobado'
df_alumnos["Aprobado"] = df_alumnos["Promedio General"] >= 5

# Convertir la columna 'Aprobado' en texto ("Sí" o "No")
df_alumnos["Aprobado"] = df_alumnos["Aprobado"].apply(lambda x: "Sí" if x else "No")

# Guardar el DataFrame actualizado en un archivo Excel
ruta_archivo = "datos_alumnos_actualizado.xlsx"
df_alumnos.to_excel(ruta_archivo, index=False)

# Mostrar un ejemplo del DataFrame actualizado
print(df_alumnos[["Nombre", "Apellidos", "Promedio General", "Aprobado"]])
