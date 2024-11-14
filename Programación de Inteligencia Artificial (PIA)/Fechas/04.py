from datetime import datetime, timedelta

def sumar_dias_a_fecha(fecha, dias):
    # Convertir la cadena de fecha en un objeto datetime
    fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
    
    # Crear un objeto timedelta con el número de días a sumar
    nueva_fecha = fecha_obj + timedelta(days=dias)
    
    # Retornar la nueva fecha formateada como cadena en el formato DD/MM/YYYY
    return nueva_fecha.strftime("%d/%m/%Y")

fecha_inicial = "14/11/2024"
dias_a_sumar = 10

nueva_fecha = sumar_dias_a_fecha(fecha_inicial, dias_a_sumar)
print(nueva_fecha)  # Salida: "24/11/2024"
