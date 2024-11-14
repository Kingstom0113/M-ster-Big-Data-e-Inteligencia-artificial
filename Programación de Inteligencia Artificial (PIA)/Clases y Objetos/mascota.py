class Mascota:
    def __init__(self, nombre, tipo_animal, edad):
        # Atributos de la mascota
        self.nombre = nombre
        self.tipo_animal = tipo_animal
        self.edad = edad
        self.energia = 50  # Nivel inicial de energía (en una escala de 0 a 100)
    
    def alimentar(self, cantidad_comida):
        # Método para alimentar a la mascota, lo que aumenta su energía
        if self.energia + cantidad_comida <= 100:
            self.energia += cantidad_comida
            return f"{self.nombre} ha sido alimentado. Energía actual: {self.energia}%."
        else:
            self.energia = 100  # Si excede el 100%, la energía se ajusta a 100%
            return f"{self.nombre} está completamente lleno. Energía al 100%."
    
    def jugar(self, tiempo_juego):
        # Método para jugar con la mascota, lo que reduce su energía
        energia_dedicada = tiempo_juego * 2  # Supongamos que cada minuto de juego reduce la energía en 2%
        if self.energia - energia_dedicada >= 0:
            self.energia -= energia_dedicada
            return f"{self.nombre} ha jugado durante {tiempo_juego} minutos. Energía actual: {self.energia}%."
        else:
            self.energia = 0  # La energía no puede ser menor a 0
            return f"{self.nombre} está muy cansado. Energía agotada."
    
    def estado_energia(self):
        # Método para mostrar el estado de la energía de la mascota
        if self.energia >= 75:
            return f"{self.nombre} está lleno de energía."
        elif self.energia >= 30:
            return f"{self.nombre} tiene energía normal."
        else:
            return f"{self.nombre} está cansado."

# Ejemplo de uso
mascota1 = Mascota("Rex", "Perro", 3)
mascota2 = Mascota("Miau", "Gato", 2)

# Alimentar a las mascotas
print(mascota1.alimentar(30))  # Alimentar a Rex
print(mascota2.alimentar(40))  # Alimentar a Miau

# Jugar con las mascotas
print(mascota1.jugar(10))  # Jugar con Rex durante 10 minutos
print(mascota2.jugar(15))  # Jugar con Miau durante 15 minutos

# Mostrar el estado de la energía
print(mascota1.estado_energia())  # Verificar la energía de Rex
print(mascota2.estado_energia())  # Verificar la energía de Miau
