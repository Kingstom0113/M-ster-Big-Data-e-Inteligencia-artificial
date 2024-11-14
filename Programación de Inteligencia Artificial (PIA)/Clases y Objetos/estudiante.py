class Estudiante:
    def __init__(self, nombre, curso, notas=None):
        # Atributos del estudiante
        self.nombre = nombre
        self.curso = curso
        self.notas = notas if notas is not None else []  # Si no se pasan notas, se inicializa una lista vacía
        self.promedio = self.calcular_promedio()  # Calcular el promedio al iniciar
    
    def añadir_nota(self, nota):
        # Método para añadir una nueva nota al estudiante
        if 0 <= nota <= 10:
            self.notas.append(nota)
            self.promedio = self.calcular_promedio()  # Actualizar el promedio después de añadir una nueva nota
            return f"Nota {nota} añadida. El nuevo promedio es {self.promedio:.2f}."
        else:
            return "La nota debe estar entre 0 y 10."
    
    def calcular_promedio(self):
        # Método para calcular el promedio de las notas
        if self.notas:
            return sum(self.notas) / len(self.notas)
        else:
            return 0  # Si no tiene notas, el promedio es 0
    
    def aprobado(self):
        # Método para verificar si el estudiante aprobó (promedio >= 5)
        if self.promedio >= 5:
            return f"{self.nombre} ha aprobado con un promedio de {self.promedio:.2f}."
        else:
            return f"{self.nombre} no ha aprobado. Su promedio es {self.promedio:.2f}."

# Ejemplo de uso
estudiante1 = Estudiante("Juan Pérez", "Matemáticas", [7, 8, 9])
estudiante2 = Estudiante("Ana Gómez", "Historia")

# Añadir una nueva nota y ver el resultado
print(estudiante1.añadir_nota(6))  # Añadir una nota y calcular el nuevo promedio
print(estudiante2.añadir_nota(4))  # Añadir una nota a estudiante2

# Mostrar si los estudiantes aprobaron o no
print(estudiante1.aprobado())  # Verificar si estudiante1 aprobó
print(estudiante2.aprobado())  # Verificar si estudiante2 aprobó

# Mostrar el promedio de notas de estudiante1
print(f"El promedio de {estudiante1.nombre} es: {estudiante1.promedio:.2f}")
