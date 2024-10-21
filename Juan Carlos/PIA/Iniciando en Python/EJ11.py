# 1. Crear la tupla 'dias_semana' con los días de la semana
dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

# 2. Verificar si el día "Sábado" está en la tupla
if "Sábado" in dias_semana:
    print("El día 'Sábado' está en la tupla.")
else:
    print("El día 'Sábado' no está en la tupla.")

# 3. Usar un loop para imprimir cada día de la semana
for dia in dias_semana:
    print(dia)

# 4. Intentar modificar el valor del primer día de la tupla
try:
    dias_semana[0] = "Nuevo_Día"  # Intentar cambiar "Lunes" a "Nuevo_Día"
except TypeError as e:
    print("Error:", e)
    print("No se puede modificar una tupla.")
