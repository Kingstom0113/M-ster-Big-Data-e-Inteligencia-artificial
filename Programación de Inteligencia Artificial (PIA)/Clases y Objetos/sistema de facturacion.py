# Clase base Producto
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio unitario del producto
        self.cantidad = cantidad  # Cantidad de productos

    def calcular_costo(self):
        # Método común para calcular el costo total de un producto
        return self.precio * self.cantidad

# Clase derivada Electrodomestico
class Electrodomestico(Producto):
    def __init__(self, nombre, precio, cantidad, consumo_energetico):
        super().__init__(nombre, precio, cantidad)
        self.consumo_energetico = consumo_energetico  # Consumo energético en kWh

    def calcular_costo(self):
        # Si el consumo energético es mayor a un umbral, aplica un recargo
        costo_base = super().calcular_costo()
        if self.consumo_energetico > 1000:  # Umbral de consumo energético (kWh)
            recargo = costo_base * 0.05  # Recargo del 5% por alto consumo
            return costo_base + recargo
        return costo_base

# Clase derivada Ropa
class Ropa(Producto):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla  # Talla de la prenda (S, M, L, XL)

    def calcular_costo(self):
        # Si la talla es XL, se aplica un recargo del 10% adicional
        costo_base = super().calcular_costo()
        if self.talla == "XL":
            recargo = costo_base * 0.10  # Recargo del 10% por talla XL
            return costo_base + recargo
        return costo_base

# Clase derivada Alimento
class Alimento(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_de_vencimiento):
        super().__init__(nombre, precio, cantidad)
        self.fecha_de_vencimiento = fecha_de_vencimiento  # Fecha de vencimiento del alimento

    def calcular_costo(self):
        # Si el alimento está cerca de su fecha de vencimiento, aplica un descuento
        costo_base = super().calcular_costo()
        if self.fecha_de_vencimiento in ["hoy", "mañana"]:  # Alimentos cercanos a su vencimiento
            descuento = costo_base * 0.10  # Descuento del 10%
            return costo_base - descuento
        return costo_base

# Ejemplo de uso

# Crear productos de diferentes categorías
producto1 = Electrodomestico("Aire acondicionado", 300, 2, 1200)  # Alto consumo energético
producto2 = Ropa("Camisa", 20, 3, "M")  # Talla normal
producto3 = Ropa("Abrigo", 50, 1, "XL")  # Talla XL, con recargo
producto4 = Alimento("Leche", 1.5, 5, "mañana")  # Descuento por proximidad de vencimiento

# Mostrar el costo total de cada producto
print(f"Producto: {producto1.nombre}, Costo total: ${producto1.calcular_costo():.2f}")
print(f"Producto: {producto2.nombre}, Costo total: ${producto2.calcular_costo():.2f}")
print(f"Producto: {producto3.nombre}, Costo total: ${producto3.calcular_costo():.2f}")
print(f"Producto: {producto4.nombre}, Costo total: ${producto4.calcular_costo():.2f}")
