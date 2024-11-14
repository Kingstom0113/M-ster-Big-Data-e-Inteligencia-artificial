class Persona:
    def __init__(self, nombre, edad, genero, altura):
        # Atributos de la persona
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.altura = altura
    
    def saludar(self, otra_persona):
        # Método para saludar a otra persona
        return f"Hola, {otra_persona.nombre}! Soy {self.nombre}."
    
    def es_mayor_de_edad(self):
        # Método para verificar si la persona es mayor de edad (18 años o más)
        if self.edad >= 18:
            return f"{self.nombre} es mayor de edad."
        else:
            return f"{self.nombre} es menor de edad."
    
    def edad_en_5_anos(self):
        # Método para mostrar la edad de la persona en 5 años
        edad_futura = self.edad + 5
        return f"En 5 años, {self.nombre} tendrá {edad_futura} años."

# Ejemplo de uso
persona1 = Persona("Juan", 25, "Masculino", 1.75)
persona2 = Persona("Ana", 17, "Femenino", 1.60)

# Saludar entre personas
print(persona1.saludar(persona2))  # Saludo de Juan a Ana
print(persona2.saludar(persona1))  # Saludo de Ana a Juan

# Verificar si las personas son mayores de edad
print(persona1.es_mayor_de_edad())  # Juan es mayor de edad
print(persona2.es_mayor_de_edad())  # Ana es menor de edad

# Mostrar la edad en 5 años
print(persona1.edad_en_5_anos())  # Edad de Juan en 5 años
print(persona2.edad_en_5_anos())  # Edad de Ana en 5 años
