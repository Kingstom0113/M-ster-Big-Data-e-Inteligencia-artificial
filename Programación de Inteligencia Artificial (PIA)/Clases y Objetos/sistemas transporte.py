# Clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, año):
        # Atributos comunes a todos los vehículos
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def mostrar_informacion(self):
        # Método para mostrar información común
        return f"{self.marca} {self.modelo} ({self.año})"
    
# Clase derivada Coche
class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, tipo_motor):
        super().__init__(marca, modelo, año)
        self.tipo_motor = tipo_motor  # Atributo específico del coche (ej. gasolina, eléctrico)
    
    def acelerar(self):
        return f"El {self.modelo} está acelerando."
    
    def frenar(self):
        return f"El {self.modelo} está frenando."
    
    def tocar_claxon(self):
        return f"El {self.modelo} está tocando el claxon: ¡BEEP BEEP!"
    
# Clase derivada Motocicleta
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, tipo_motor):
        super().__init__(marca, modelo, año)
        self.tipo_motor = tipo_motor  # Atributo específico de la motocicleta (ej. gasolina, eléctrico)
    
    def acelerar(self):
        return f"La motocicleta {self.modelo} está acelerando."
    
    def frenar(self):
        return f"La motocicleta {self.modelo} está frenando."
    
    def tocar_claxon(self):
        return f"La motocicleta {self.modelo} está tocando el claxon: ¡BEEP BEEP!"
    
# Clase derivada Bicicleta
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo, año)
        self.tipo = tipo  # Atributo específico de la bicicleta (ej. montaña, carretera)
    
    def pedalear(self):
        return f"La bicicleta {self.modelo} está siendo pedaleada."
    
    def frenar(self):
        return f"La bicicleta {self.modelo} está frenando."
    
# Ejemplo de uso
# Crear instancias de cada tipo de vehículo
coche1 = Coche("Toyota", "Corolla", 2020, "Gasolina")
moto1 = Motocicleta("Yamaha", "R1", 2023, "Gasolina")
bici1 = Bicicleta("Specialized", "Allez", 2021, "Carretera")

# Mostrar información de los vehículos
print(coche1.mostrar_informacion())  # Información del coche
print(moto1.mostrar_informacion())   # Información de la moto
print(bici1.mostrar_informacion())   # Información de la bicicleta

# Acciones específicas de cada vehículo
print(coche1.acelerar())       # Acción de acelerar para el coche
print(moto1.acelerar())        # Acción de acelerar para la moto
print(bici1.pedalear())        # Acción de pedalear para la bicicleta
print(coche1.tocar_claxon())   # Acción de tocar el claxon para el coche
print(moto1.tocar_claxon())    # Acción de tocar el claxon para la moto
print(bici1.frenar())          # Acción de frenar para la bicicleta
