import pandas as pd
import random
import matplotlib.pyplot as plt

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

# Calcular la nota final de 'Programación' y 'Base de Datos' (promedio de las 3 notas)
df_alumnos["Programación Final"] = df_alumnos[["Programación T1", "Programación T2", "Programación T3"]].mean(axis=1)
df_alumnos["Base de Datos Final"] = df_alumnos[["Base de Datos T1", "Base de Datos T2", "Base de Datos T3"]].mean(axis=1)

# Crear gráfico de dispersión entre 'Programación Final' y 'Base de Datos Final'
plt.figure(figsize=(8, 6))
plt.scatter(df_alumnos["Programación Final"], df_alumnos["Base de Datos Final"], color='b', alpha=0.7)

# Añadir títulos y etiquetas
plt.title('Relación entre las notas finales de Programación y Base de Datos')
plt.xlabel('Nota final de Programación')
plt.ylabel('Nota final de Base de Datos')

# Mostrar gráfico
plt.grid(True)
plt.show()
