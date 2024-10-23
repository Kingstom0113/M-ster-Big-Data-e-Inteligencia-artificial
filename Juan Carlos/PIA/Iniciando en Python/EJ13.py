# 1. Crear el diccionario 'clase' con la estructura dada
clase = {
    "estudiante1": {
        "nombre": "Carlos",
        "edad": 19,
        "materias": ["Matemáticas", "Física"]
    },
    "estudiante2": {
        "nombre": "Marta",
        "edad": 20,
        "materias": ["Química", "Biología"]
    }
}

# 2. Agregar un tercer estudiante llamado "Pedro", de 21 años, con las materias "Historia" y "Geografía"
clase["estudiante3"] = {
    "nombre": "Pedro",
    "edad": 21,
    "materias": ["Historia", "Geografía"]
}

# 3. Imprimir el nombre y la edad de todos los estudiantes
for estudiante in clase.values():
    print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}")

# 4. Cambiar la edad de "Marta" a 21 años
clase["estudiante2"]["edad"] = 21

# 5. Eliminar las materias de "Carlos"
del clase["estudiante1"]["materias"]

# Imprimir el diccionario final para verificar los cambios
print("\nDiccionario final:", clase)
