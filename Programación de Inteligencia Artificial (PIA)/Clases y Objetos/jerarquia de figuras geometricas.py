import math

# Clase base Figura
class Figura:
    def __init__(self, color, tipo):
        self.color = color  # Atributo color de la figura
        self.tipo = tipo    # Atributo tipo de la figura (ej. círculo, cuadrado, triángulo)
    
    def calcular_area(self):
        # Método común que será sobrescrito por las clases derivadas
        raise NotImplementedError("El método calcular_area debe ser implementado en las clases derivadas.")
    
    def calcular_perimetro(self):
        # Método común que será sobrescrito por las clases derivadas
        raise NotImplementedError("El método calcular_perimetro debe ser implementado en las clases derivadas.")

# Clase derivada Circulo
class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color, "Círculo")
        self.radio = radio  # Atributo específico del círculo
    
    def calcular_area(self):
        # Área de un círculo: π * radio^2
        return math.pi * self.radio ** 2
    
    def calcular_perimetro(self):
        # Perímetro de un círculo: 2 * π * radio
        return 2 * math.pi * self.radio

# Clase derivada Cuadrado
class Cuadrado(Figura):
    def __init__(self, color, lado):
        super().__init__(color, "Cuadrado")
        self.lado = lado  # Atributo específico del cuadrado
    
    def calcular_area(self):
        # Área de un cuadrado: lado^2
        return self.lado ** 2
    
    def calcular_perimetro(self):
        # Perímetro de un cuadrado: 4 * lado
        return 4 * self.lado

# Clase derivada Triangulo
class Triangulo(Figura):
    def __init__(self, color, base, altura, lado1, lado2, lado3):
        super().__init__(color, "Triángulo")
        self.base = base  # Atributos específicos del triángulo
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcular_area(self):
        # Área de un triángulo: (base * altura) / 2
        return (self.base * self.altura) / 2
    
    def calcular_perimetro(self):
        # Perímetro de un triángulo: suma de sus lados
        return self.lado1 + self.lado2 + self.lado3

# Ejemplo de uso
# Crear instancias de cada tipo de figura
circulo = Circulo("Rojo", 5)
cuadrado = Cuadrado("Azul", 4)
triangulo = Triangulo("Verde", 3, 6, 3, 4, 5)

# Mostrar el área y perímetro de cada figura
print(f"Círculo de color {circulo.color}:")
print(f"Área: {circulo.calcular_area():.2f}")
print(f"Perímetro: {circulo.calcular_perimetro():.2f}\n")

print(f"Cuadrado de color {cuadrado.color}:")
print(f"Área: {cuadrado.calcular_area():.2f}")
print(f"Perímetro: {cuadrado.calcular_perimetro():.2f}\n")

print(f"Triángulo de color {triangulo.color}:")
print(f"Área: {triangulo.calcular_area():.2f}")
print(f"Perímetro: {triangulo.calcular_perimetro():.2f}")
