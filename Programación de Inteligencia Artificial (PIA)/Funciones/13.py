def pasos_a_kilometros(pasos):
    longitud_paso = 0.78  # Longitud media de un paso en metros
    distancia_metros = pasos * longitud_paso  # Distancia total en metros
    distancia_kilometros = distancia_metros / 1000  # Convertimos metros a kilómetros
    return distancia_kilometros

print(pasos_a_kilometros(1000))  # Salida: 0.78, porque 1000 pasos son aproximadamente 0.78 km
print(pasos_a_kilometros(5000))  # Salida: 3.9, porque 5000 pasos son aproximadamente 3.9 km
