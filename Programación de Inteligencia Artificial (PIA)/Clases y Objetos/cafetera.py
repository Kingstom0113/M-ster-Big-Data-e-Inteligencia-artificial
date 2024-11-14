class Cafetera:
    def __init__(self, marca, capacidad_maxima, nivel_actual):
        # Atributos de la cafetera
        self.marca = marca
        self.capacidad_maxima = capacidad_maxima  # en litros
        self.nivel_actual = nivel_actual  # en litros
    
    def servir_cafe(self, cantidad):
        # Método para servir café (disminuye el nivel de café disponible)
        if cantidad <= self.nivel_actual:
            self.nivel_actual -= cantidad
            return f"Has servido {cantidad} litros de café. Nivel actual: {self.nivel_actual} litros."
        else:
            return "No hay suficiente café en la cafetera."
    
    def rellenar(self):
        # Método para rellenar la cafetera a su capacidad máxima
        self.nivel_actual = self.capacidad_maxima
        return f"La cafetera ha sido rellenada. Nivel actual: {self.nivel_actual} litros."
    
    def esta_vacia(self):
        # Método para indicar si la cafetera está vacía
        if self.nivel_actual == 0:
            return "La cafetera está vacía."
        else:
            return "La cafetera tiene café."
    
    def esta_llena(self):
        # Método para indicar si la cafetera está llena
        if self.nivel_actual == self.capacidad_maxima:
            return "La cafetera está llena."
        else:
            return f"La cafetera no está llena. Nivel actual: {self.nivel_actual} litros."

# Ejemplo de uso
cafetera1 = Cafetera("Delonghi", 2.0, 1.5)  # 2 litros de capacidad, 1.5 litros de café
cafetera2 = Cafetera("Nespresso", 1.5, 0.0)  # 1.5 litros de capacidad, sin café

# Operaciones con la cafetera
print(cafetera1.servir_cafe(0.5))  # Servir 0.5 litros de café
print(cafetera1.esta_vacia())  # Comprobar si está vacía
print(cafetera1.esta_llena())  # Comprobar si está llena
print(cafetera1.rellenar())  # Rellenar la cafetera

print(cafetera2.servir_cafe(0.1))  # Intentar servir café cuando la cafetera está vacía
print(cafetera2.esta_vacia())  # Comprobar si está vacía
print(cafetera2.esta_llena())  # Comprobar si está llena
