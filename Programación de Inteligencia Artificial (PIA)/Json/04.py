import json
from datetime import datetime

# Función para cargar las ventas desde el archivo JSON
def cargar_ventas():
    try:
        with open("registro_ventas.json", "r") as file:
            data = json.load(file)
            return data['ventas']
    except FileNotFoundError:
        # Si el archivo no existe, devolver una lista vacía
        return []

# Función para guardar las ventas en el archivo JSON
def guardar_ventas(ventas):
    with open("registro_ventas.json", "w") as file:
        json.dump({"ventas": ventas}, file, indent=4)

# Función para agregar una nueva venta
def agregar_venta(ventas, producto, cantidad, precio, fecha):
    nueva_venta = {
        "producto": producto,
        "cantidad": cantidad,
        "precio": precio,
        "fecha": fecha
    }
    ventas.append(nueva_venta)
    guardar_ventas(ventas)

# Función para calcular el total de ventas
def calcular_total_ventas(ventas):
    total = sum(venta['cantidad'] * venta['precio'] for venta in ventas)
    return total

# Función para filtrar ventas por producto
def filtrar_por_producto(ventas, producto):
    return [venta for venta in ventas if venta['producto'].lower() == producto.lower()]

# Función para filtrar ventas por fecha
def filtrar_por_fecha(ventas, fecha):
    return [venta for venta in ventas if venta['fecha'] == fecha]

# Función para mostrar todas las ventas
def mostrar_ventas(ventas):
    if not ventas:
        print("No hay ventas registradas.")
    for venta in ventas:
        print(f"Producto: {venta['producto']}, Cantidad: {venta['cantidad']}, Precio: {venta['precio']}, Fecha: {venta['fecha']}")

# Inicialización de datos
ventas = cargar_ventas()

# Insertar al menos 10 ventas si no existen ventas
if not ventas:
    ventas = [
        {"producto": "Laptop", "cantidad": 2, "precio": 1000, "fecha": "2024-10-28"},
        {"producto": "Teclado", "cantidad": 5, "precio": 50, "fecha": "2024-10-27"},
        {"producto": "Mouse", "cantidad": 10, "precio": 20, "fecha": "2024-10-26"},
        {"producto": "Monitor", "cantidad": 3, "precio": 200, "fecha": "2024-10-25"},
        {"producto": "Impresora", "cantidad": 1, "precio": 150, "fecha": "2024-10-24"},
        {"producto": "Smartphone", "cantidad": 4, "precio": 500, "fecha": "2024-10-23"},
        {"producto": "Teclado", "cantidad": 7, "precio": 50, "fecha": "2024-10-22"},
        {"producto": "Laptop", "cantidad": 1, "precio": 1000, "fecha": "2024-10-21"},
        {"producto": "Smartwatch", "cantidad": 6, "precio": 150, "fecha": "2024-10-20"},
        {"producto": "Cargador", "cantidad": 8, "precio": 25, "fecha": "2024-10-19"}
    ]
    guardar_ventas(ventas)

# Ejemplo de uso

# Mostrar todas las ventas
print("Ventas registradas:")
mostrar_ventas(ventas)

# Agregar una nueva venta
print("\nAgregar una nueva venta:")
agregar_venta(ventas, "Auriculares", 3, 75, "2024-10-18")

# Calcular el total de ventas
total = calcular_total_ventas(ventas)
print(f"\nTotal de ventas: ${total}")

# Filtrar ventas por producto
print("\nVentas de 'Laptop':")
ventas_laptop = filtrar_por_producto(ventas, "Laptop")
for venta in ventas_laptop:
    print(f"Producto: {venta['producto']}, Cantidad: {venta['cantidad']}, Precio: {venta['precio']}, Fecha: {venta['fecha']}")

# Filtrar ventas por fecha
print("\nVentas del '2024-10-28':")
ventas_fecha = filtrar_por_fecha(ventas, "2024-10-28")
for venta in ventas_fecha:
    print(f"Producto: {venta['producto']}, Cantidad: {venta['cantidad']}, Precio: {venta['precio']}, Fecha: {venta['fecha']}")
