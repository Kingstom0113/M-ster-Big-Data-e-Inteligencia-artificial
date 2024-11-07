# 1. Crear el diccionario 'capitales' con las parejas clave-valor
capitales = {
    "España": "Madrid",
    "Francia": "París",
    "Italia": "Roma"
}

# 2. Agregar una nueva pareja clave-valor "Alemania": "Berlín"
capitales["Alemania"] = "Berlín"

# 3. Cambiar el valor asociado a la clave "Francia" para que sea "Lyon"
capitales["Francia"] = "Lyon"

# 4. Eliminar la entrada correspondiente a "Italia"
del capitales["Italia"]

# 5. Imprimir todas las claves del diccionario
print("Claves del diccionario:", capitales.keys())

# 6. Imprimir todos los valores del diccionario
print("Valores del diccionario:", capitales.values())

# 7. Imprimir el diccionario final
print("Diccionario final:", capitales)
