# Clase base Animal
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo nombre del animal
        self.edad = edad      # Atributo edad del animal
    
    def hacer_sonido(self):
        # Método común que será sobrescrito por las clases derivadas
        return "El animal hace un sonido."

# Clase derivada Perro
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza  # Atributo específico del perro
    
    def hacer_sonido(self):
        return f"{self.nombre} (Perro) dice: ¡Guau guau!"
    
    def correr(self):
        return f"{self.nombre} está corriendo."

# Clase derivada Gato
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color  # Atributo específico del gato
    
    def hacer_sonido(self):
        return f"{self.nombre} (Gato) dice: ¡Miau miau!"
    
    def saltar(self):
        return f"{self.nombre} está saltando."

# Clase derivada Pájaro
class Pajaro(Animal):
    def __init__(self, nombre, edad, especie):
        super().__init__(nombre, edad)
        self.especie = especie  # Atributo específico del pájaro
    
    def hacer_sonido(self):
        return f"{self.nombre} (Pájaro) dice: ¡Pío pío!"
    
    def volar(self):
        return f"{self.nombre} está volando."

# Ejemplo de uso
# Crear instancias de cada tipo de animal
perro = Perro("Rex", 5, "Labrador")
gato = Gato("Whiskers", 3, "Negro")
pajaro = Pajaro("Piolin", 2, "Canario")

# Mostrar sonidos y acciones de los animales
print(perro.hacer_sonido())  # Sonido del perro
print(perro.correr())         # Acción de correr del perro

print(gato.hacer_sonido())   # Sonido del gato
print(gato.saltar())         # Acción de saltar del gato

print(pajaro.hacer_sonido()) # Sonido del pájaro
print(pajaro.volar())        # Acción de volar del pájaro
