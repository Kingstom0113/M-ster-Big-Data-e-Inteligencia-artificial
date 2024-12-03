import pandas as pd

# Ejercicio 2: Calificaciones de Estudiantes

# Solicitar al usuario las calificaciones de 10 estudiantes
print("Por favor, ingresa las calificaciones de 10 estudiantes:")

nombres_estudiantes = []
calificaciones = []

for i in range(1, 11):
    nombre = input(f"Nombre del estudiante {i}: ")
    calificacion = float(input(f"Calificación de {nombre}: "))
    nombres_estudiantes.append(nombre)
    calificaciones.append(calificacion)

# Crear una Serie con las calificaciones y asignar nombres como índice
serie_calificaciones = pd.Series(calificaciones, index=nombres_estudiantes)

# Calcular promedio, mediana y desviación estándar
promedio = serie_calificaciones.mean()
mediana = serie_calificaciones.median()
desviacion_std = serie_calificaciones.std()

# Reemplazar las calificaciones por debajo de 50 con "Reprobado"
serie_calificaciones_actualizada = serie_calificaciones.copy()
serie_calificaciones_actualizada[serie_calificaciones_actualizada < 50] = "Reprobado"

# Mostrar los estudiantes con calificaciones aprobatorias
estudiantes_aprobados = serie_calificaciones_actualizada[serie_calificaciones_actualizada != "Reprobado"]

# Mostrar resultados
print("\n--- Resultados ---")
print(f"Promedio de las calificaciones: {promedio:.2f}")
print(f"Mediana de las calificaciones: {mediana:.2f}")
print(f"Desviación estándar: {desviacion_std:.2f}")
print("\nCalificaciones actualizadas:")
print(serie_calificaciones_actualizada)
print("\nEstudiantes con calificaciones aprobatorias:")
print(estudiantes_aprobados)
