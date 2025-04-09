import random
import time
from datetime import datetime

# Función para simular datos de sensores
def simular_sensor(nombre_sensor, min_valor, max_valor, unidad):
    valor = random.uniform(min_valor, max_valor)
    return {"nombre": nombre_sensor, "valor": round(valor, 2), "unidad": unidad, "timestamp": datetime.now()}

# Función para tomar decisiones basadas en reglas
def tomar_decision(datos_sensores):
    decisiones = []
    for dato in datos_sensores:
        if dato["nombre"] == "temperatura":
            if dato["valor"] > 25:
                decisiones.append({"sensor": "temperatura", "accion": "encender_aire_acondicionado"})
            elif dato["valor"] < 20:
                decisiones.append({"sensor": "temperatura", "accion": "encender_calefaccion"})
        elif dato["nombre"] == "luz":
            if dato["valor"] < 300:
                decisiones.append({"sensor": "luz", "accion": "encender_luces"})
            elif dato["valor"] > 700:
                decisiones.append({"sensor": "luz", "accion": "apagar_luces"})
        elif dato["nombre"] == "CO2":
            if dato["valor"] > 1000:
                decisiones.append({"sensor": "CO2", "accion": "encender_ventilacion"})
    return decisiones

# Simulación principal
def simular_entorno_oficina():
    registros_sensores = []
    for _ in range(15): # 15 registros por sensor
        temperatura = simular_sensor("temperatura", 18, 28, "°C") # Sensor de temperatura (LM35)
        luz = simular_sensor("luz", 200, 800, "lux") # Sensor de luz (BH1750)
        humedad = simular_sensor("humedad", 30, 70, "%") # Sensor de humedad (DHT11)
        co2 = simular_sensor("CO2", 400, 1200, "ppm") # Sensor de CO2 (MQ-135)

        registros_sensores.extend([temperatura, luz, humedad, co2])
        time.sleep(2) # Pausa de 2 segundos entre registros

    decisiones = tomar_decision(registros_sensores)
    return registros_sensores, decisiones

# Generar informe
def generar_informe(registros_sensores, decisiones):
    with open("informe_sensores.txt", "w") as archivo:
        archivo.write("Informe de Sensores IoT\n\n")
        for registro in registros_sensores:
            archivo.write(f"Sensor: {registro['nombre']}, Valor: {registro['valor']} {registro['unidad']}, Timestamp: {registro['timestamp']}\n")
        archivo.write("\nDecisiones Inteligentes:\n")
        for decision in decisiones:
            archivo.write(f"Sensor: {decision['sensor']}, Acción: {decision['accion']}\n")

# Ejecutar simulación y generar informe
registros, decisiones = simular_entorno_oficina()
generar_informe(registros, decisiones)

print("Simulación completada. Informe generado en informe_sensores.txt")