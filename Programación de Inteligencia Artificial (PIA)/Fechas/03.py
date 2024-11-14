from datetime import datetime

def calcular_diferencia_dias(fecha1, fecha2):
    # Convertir las cadenas a objetos datetime
    fecha_obj1 = datetime.strptime(fecha1, "%d/%m/%Y")
    fecha_obj2 = datetime.strptime(fecha2, "%d/%m/%Y")
    
    # Calcular la diferencia entre las dos fechas
    diferencia = abs((fecha_obj2 - fecha_obj1).days)
    
    # Retornar el número de días de diferencia
    return diferencia

fecha1 = "14/11/2024"
fecha2 = "20/11/2024"

diferencia = calcular_diferencia_dias(fecha1, fecha2)
print(diferencia)  # Salida: 6, porque hay 6 días de diferencia
