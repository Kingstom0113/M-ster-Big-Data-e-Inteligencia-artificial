import json

# Función para cargar los coches desde un archivo JSON
def cargar_coches():
    try:
        with open("concesionario_coches.json", "r") as file:
            data = json.load(file)
            return data['coches']
    except FileNotFoundError:
        # Si el archivo no existe, devolver una lista vacía
        return []

# Función para guardar los coches en el archivo JSON
def guardar_coches(coches):
    with open("concesionario_coches.json", "w") as file:
        json.dump({"coches": coches}, file, indent=4)

# Función para agregar un coche al concesionario
def agregar_coche(coches, marca, modelo, precio, año):
    nuevo_coche = {
        "marca": marca,
        "modelo": modelo,
        "precio": precio,
        "año": año
    }
    coches.append(nuevo_coche)
    guardar_coches(coches)

# Función para filtrar los coches por marca
def filtrar_por_marca(coches, marca):
    return [coche for coche in coches if coche['marca'].lower() == marca.lower()]

# Función para calcular el precio promedio de los coches
def calcular_precio_promedio(coches):
    if not coches:
        return 0
    total_precio = sum(coche['precio'] for coche in coches)
    return total_precio / len(coches)

# Función para actualizar el precio de un coche
def actualizar_precio(coches, marca, modelo, nuevo_precio):
    for coche in coches:
        if coche['marca'].lower() == marca.lower() and coche['modelo'].lower() == modelo.lower():
            coche['precio'] = nuevo_precio
            guardar_coches(coches)
            return coche
    return None

# Función para mostrar todos los coches
def mostrar_coches(coches):
    if not coches:
        print("No hay coches disponibles en el concesionario.")
    for coche in coches:
        print(f"Marca: {coche['marca']}, Modelo: {coche['modelo']}, Precio: {coche['precio']}, Año: {coche['año']}")

# Inicialización de datos
coches = cargar_coches()

# Insertar al menos 10 coches si no existen
if not coches:
    coches = [
        {"marca": "Toyota", "modelo": "Corolla", "precio": 20000, "año": 2023},
        {"marca": "Ford", "modelo": "Focus", "precio": 18000, "año": 2022},
        {"marca": "Honda", "modelo": "Civic", "precio": 22000, "año": 2023},
        {"marca": "BMW", "modelo": "Serie 3", "precio": 35000, "año": 2021},
        {"marca": "Audi", "modelo": "A4", "precio": 40000, "año": 2020},
        {"marca": "Mercedes", "modelo": "Clase C", "precio": 45000, "año": 2022},
        {"marca": "Volkswagen", "modelo": "Golf", "precio": 25000, "año": 2021},
        {"marca": "Peugeot", "modelo": "308", "precio": 23000, "año": 2020},
        {"marca": "Nissan", "modelo": "Qashqai", "precio": 27000, "año": 2023},
        {"marca": "Seat", "modelo": "León", "precio": 19000, "año": 2021}
    ]
    guardar_coches(coches)

# Ejemplo de uso

# Mostrar todos los coches
print("Coches disponibles en el concesionario:")
mostrar_coches(coches)

# Calcular el precio promedio de los coches
precio_promedio = calcular_precio_promedio(coches)
print(f"\nPrecio promedio de los coches: {precio_promedio:.2f} €")

# Filtrar coches por marca (ejemplo: Toyota)
print("\nFiltrar coches por marca 'Toyota':")
coches_toyota = filtrar_por_marca(coches, "Toyota")
for coche in coches_toyota:
    print(f"Marca: {coche['marca']}, Modelo: {coche['modelo']}, Precio: {coche['precio']}, Año: {coche['año']}")

# Actualizar el precio de un coche (ejemplo: actualizar el precio del Toyota Corolla)
print("\nActualizar el precio del Toyota Corolla a 21000 €:")
actualizado = actualizar_precio(coches, "Toyota", "Corolla", 21000)
if actualizado:
    print(f"Precio actualizado: {actualizado['marca']} {actualizado['modelo']} a {actualizado['precio']} €")
else:
    print("Coche no encontrado.")

# Mostrar todos los coches después de la actualización
print("\nCoches disponibles después de la actualización:")
mostrar_coches(coches)
