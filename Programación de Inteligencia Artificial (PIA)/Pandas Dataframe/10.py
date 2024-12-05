import pandas as pd
import random
import numpy as np

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

# Calcular el promedio general de cada alumno (promedio de todas las asignaturas)
columnas_notas = [
    "Programación T1", "Programación T2", "Programación T3",
    "Base de Datos T1", "Base de Datos T2", "Base de Datos T3",
    "Lenguajes T1", "Lenguajes T2", "Lenguajes T3",
    "Sistemas T1", "Sistemas T2", "Sistemas T3",
    "Entornos T1", "Entornos T2", "Entornos T3"
]

df_alumnos["Promedio General"] = df_alumnos[columnas_notas].mean(axis=1)

# Calcular la desviación estándar del promedio general de las notas
desviacion_estandar = np.std(df_alumnos["Promedio General"])

# Mostrar el resultado
print(f"La desviación estándar del promedio general de las notas es: {desviacion_estandar:.2f}")
