class Pelota:
    def __init__(self, tipo_de_deporte, tamaño, presion_aire):
        # Atributos de la pelota
        self.tipo_de_deporte = tipo_de_deporte
        self.tamaño = tamaño
        self.presion_aire = presion_aire  # La presión de aire puede ser un valor numérico
        
    def inflar(self, cantidad):
        # Método para inflar la pelota, aumentando la presión de aire
        self.presion_aire += cantidad
        return f"La pelota ha sido inflada. La nueva presión es {self.presion_aire} psi."
    
    def desinflar(self, cantidad):
        # Método para desinflar la pelota, reduciendo la presión de aire
        if self.presion_aire - cantidad >= 0:
            self.presion_aire -= cantidad
            return f"La pelota ha sido desinflada. La nueva presión es {self.presion_aire} psi."
        else:
            return "No se puede desinflar más allá de una presión de 0 psi."
    
    def estado_presion(self):
        # Método para mostrar el estado de la presión de la pelota
        if self.presion_aire < 10:
            return "La presión de la pelota está baja."
        elif 10 <= self.presion_aire <= 20:
            return "La presión de la pelota es normal."
        else:
            return "La presión de la pelota es alta."

# Ejemplo de uso
pelota1 = Pelota("Fútbol", "Tamaño 5", 12)  # Pelota de fútbol con presión de aire inicial de 12 psi
pelota2 = Pelota("Baloncesto", "Tamaño 7", 22)  # Pelota de baloncesto con presión de aire de 22 psi

# Inflar y desinflar las pelotas
print(pelota1.inflar(5))  # Inflar la pelota1
print(pelota1.estado_presion())  # Verificar el estado de la presión de la pelota1

print(pelota2.desinflar(10))  # Desinflar la pelota2
print(pelota2.estado_presion())  # Verificar el estado de la presión de la pelota2

# Intentar desinflar demasiado
print(pelota1.desinflar(20))  # Intentar desinflar más allá de la presión mínima
