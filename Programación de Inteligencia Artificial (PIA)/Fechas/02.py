from datetime import datetime

def convertir_a_fecha(cadena):
    # Convertir la cadena al objeto datetime usando strptime
    fecha = datetime.strptime(cadena, "%d/%m/%Y")
    
    # Retornar el objeto datetime
    return fecha

fecha_convertida = convertir_a_fecha("14/11/2024")
print(fecha_convertida)
