import pandas as pd

# Ejercicio 4: Registro de Horas de Trabajo

# Solicitar las horas trabajadas por un empleado durante 5 días laborales
print("Por favor, ingresa las horas trabajadas por un empleado durante 5 días laborales:")

dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
horas_trabajadas = []

for dia in dias:
    horas = float(input(f"Horas trabajadas el {dia}: "))
    horas_trabajadas.append(horas)

# Crear una Serie con los datos
serie_horas = pd.Series(horas_trabajadas, index=dias)

# Calcular el total de horas trabajadas
total_horas = serie_horas.sum()

# Mostrar los días en los que se trabajó más de 8 horas
dias_extra = serie_horas[serie_horas > 8]

# Reemplazar las horas menores a 6 con "Medio tiempo"
serie_clasificacion = serie_horas.copy()
serie_clasificacion[serie_horas < 6] = "Medio tiempo"

# Clasificar los días
clasificaciones = []
for horas in serie_horas:
    if horas == "Medio tiempo":
        clasificaciones.append("Medio tiempo")
    elif horas > 8:
        clasificaciones.append("Extra")
    else:
        clasificaciones.append("Normal")

# Agregar la clasificación a una nueva Serie
serie_clasificada = pd.Series(clasificaciones, index=dias)

# Mostrar resultados
print("\n--- Resultados ---")
print(f"Total de horas trabajadas: {total_horas:.2f} horas")
print("\nDías con más de 8 horas trabajadas:")
print(dias_extra)
print("\nClasificación de días según horas trabajadas:")
print(serie_clasificada)
