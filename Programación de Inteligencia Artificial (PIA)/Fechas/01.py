from datetime import datetime

def obtener_fecha_formateada():
    # Obtener la fecha y hora actuales
    ahora = datetime.now()
    
    # Formatear la fecha y hora en el formato DD/MM/YYYY HH:MM:SS
    fecha_formateada = ahora.strftime("%d/%m/%Y %H:%M:%S")
    
    return fecha_formateada

print(obtener_fecha_formateada())
