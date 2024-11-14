class Reloj:
    def __init__(self, hora=0, minuto=0, segundo=0):
        # Atributos para la hora, minuto y segundo actuales
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
    
    def ajustar_hora(self, hora, minuto, segundo):
        # Método para ajustar la hora, minuto y segundo
        if 0 <= hora < 24 and 0 <= minuto < 60 and 0 <= segundo < 60:
            self.hora = hora
            self.minuto = minuto
            self.segundo = segundo
            return f"Hora ajustada a {self.mostrar_hora()}"
        else:
            return "Entrada no válida. Asegúrese de que la hora esté entre 0 y 23, el minuto entre 0 y 59, y el segundo entre 0 y 59."
    
    def avanzar_un_minuto(self):
        # Método para avanzar un minuto
        self.minuto += 1
        if self.minuto == 60:
            self.minuto = 0
            self.avanzar_una_hora()
        return f"Nuevo tiempo: {self.mostrar_hora()}"
    
    def avanzar_un_segundo(self):
        # Método para avanzar un segundo
        self.segundo += 1
        if self.segundo == 60:
            self.segundo = 0
            self.avanzar_un_minuto()
        return f"Nuevo tiempo: {self.mostrar_hora()}"
    
    def avanzar_una_hora(self):
        # Método privado para avanzar una hora
        self.hora += 1
        if self.hora == 24:
            self.hora = 0
    
    def mostrar_hora(self):
        # Método para mostrar la hora en formato hh:mm:ss
        return f"{self.hora:02}:{self.minuto:02}:{self.segundo:02}"

# Ejemplo de uso
reloj1 = Reloj(10, 30, 45)  # Inicializa el reloj con la hora 10:30:45

# Ajustar la hora
print(reloj1.ajustar_hora(12, 45, 0))  # Ajustar a 12:45:00

# Avanzar un minuto
print(reloj1.avanzar_un_minuto())  # Avanzar un minuto

# Avanzar un segundo
print(reloj1.avanzar_un_segundo())  # Avanzar un segundo

# Mostrar la hora actual
print(reloj1.mostrar_hora())  # Mostrar la hora actual
