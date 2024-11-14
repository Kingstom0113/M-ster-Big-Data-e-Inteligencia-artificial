from datetime import datetime

def convertir_fecha(formato_original):
    # Convertir la cadena en un objeto datetime usando strptime
    fecha_obj = datetime.strptime(formato_original, "%Y-%m-%d")
    
    # Formatear la fecha en el formato DD/MM/YYYY usando strftime
    fecha_convertida = fecha_obj.strftime("%d/%m/%Y")
    
    return fecha_convertida

fecha_inicial = "2024-11-14"
fecha_nueva = convertir_fecha(fecha_inicial)
print(fecha_nueva)  # Salida: "14/11/2024"
