class Smartphone:
    def __init__(self, marca, modelo, memoria, bateria, nivel_bateria_actual):
        # Atributos del smartphone
        self.marca = marca
        self.modelo = modelo
        self.memoria = memoria
        self.bateria = bateria  # Capacidad máxima de la batería en mAh
        self.nivel_bateria_actual = nivel_bateria_actual  # Nivel actual de la batería en porcentaje (0-100)
    
    def llamar(self, duracion_llamada):
        # Método para llamar a un contacto, lo que reduce el nivel de batería
        # Supongamos que por cada minuto de llamada, se reduce un 1% de batería
        consumo_bateria = duracion_llamada  # 1% de batería por minuto
        if self.nivel_bateria_actual >= consumo_bateria:
            self.nivel_bateria_actual -= consumo_bateria
            return f"Llamada de {duracion_llamada} minutos realizada. Nivel de batería actual: {self.nivel_bateria_actual}%"
        else:
            return "Batería insuficiente para realizar la llamada."
    
    def cargar(self, cantidad_carga):
        # Método para cargar el teléfono, aumentando el nivel de batería
        if self.nivel_bateria_actual + cantidad_carga <= 100:
            self.nivel_bateria_actual += cantidad_carga
            return f"Teléfono cargado en {cantidad_carga}%. Nivel de batería actual: {self.nivel_bateria_actual}%"
        else:
            self.nivel_bateria_actual = 100  # Si se excede, se ajusta al 100%
            return "Batería completamente cargada (100%)."
    
    def mostrar_nivel_bateria(self):
        # Método para mostrar el nivel de batería actual
        return f"Nivel de batería actual: {self.nivel_bateria_actual}%"

# Ejemplo de uso
smartphone1 = Smartphone("Samsung", "Galaxy S21", "128GB", "4000mAh", 80)
smartphone2 = Smartphone("Apple", "iPhone 13", "256GB", "4000mAh", 50)

# Realizar una llamada
print(smartphone1.llamar(30))  # Llamada de 30 minutos
print(smartphone2.llamar(60))  # Llamada de 60 minutos

# Cargar los teléfonos
print(smartphone1.cargar(20))  # Cargar 20%
print(smartphone2.cargar(60))  # Cargar 60% (esto debería llenar la batería completamente)

# Mostrar el nivel de batería
print(smartphone1.mostrar_nivel_bateria())
print(smartphone2.mostrar_nivel_bateria())
