import hashlib
import random

class Bloque:
    def __init__(self, mensaje, hash_anterior=""):
        self.mensaje = mensaje
        self.hash_anterior = hash_anterior
        self.hash = self.calcular_hash()

    def calcular_hash(self):
        contenido = self.mensaje + self.hash_anterior
        return hashlib.sha256(contenido.encode()).hexdigest()

def distorsionar_mensaje(mensaje, probabilidad_error=0.1):
    mensaje_distorsionado = ""
    for caracter in mensaje:
        if random.random() < probabilidad_error:
            mensaje_distorsionado += random.choice("abcdefghijklmnopqrstuvwxyz ")
        else:
            mensaje_distorsionado += caracter
    return mensaje_distorsionado

def simular_cadena(mensaje_inicial, num_bloques, probabilidad_error=0.1):
    cadena = [Bloque(mensaje_inicial)]
    for i in range(1, num_bloques):
        mensaje_anterior = cadena[i - 1].mensaje
        mensaje_alterado = distorsionar_mensaje(mensaje_anterior, probabilidad_error)
        hash_anterior = cadena[i - 1].hash
        cadena.append(Bloque(mensaje_alterado, hash_anterior))
    return cadena

def verificar_integridad(cadena):
    for i in range(1, len(cadena)):
        if cadena[i].hash_anterior != cadena[i - 1].hash:
            return False
    return True

def modo_trampa(cadena, indice_bloque, mensaje_nuevo):
    cadena[indice_bloque].mensaje = mensaje_nuevo
    cadena[indice_bloque].hash = cadena[indice_bloque].calcular_hash()

def reparar_cadena(cadena, indice_alterado):
    for i in range(indice_alterado, len(cadena)):
        cadena[i].hash_anterior = cadena[i - 1].hash
        cadena[i].hash = cadena[i].calcular_hash()

def guardar_cadena(cadena, nombre_archivo="cadena.txt"):
    with open(nombre_archivo, "w") as archivo:
        for bloque in cadena:
            archivo.write(f"Mensaje: {bloque.mensaje}\n")
            archivo.write(f"Hash: {bloque.hash}\n")
            archivo.write(f"Hash anterior: {bloque.hash_anterior}\n")
            archivo.write("-" * 50 + "\n")

# Configuración y uso
mensaje_inicial = "Este es el mensaje inicial secreto."
num_bloques = 5
probabilidad_error = 0.3  # 30% de probabilidad de error
cadena = simular_cadena(mensaje_inicial, num_bloques, probabilidad_error)

print("Cadena inicial:")
for bloque in cadena:
    print(f"Mensaje: {bloque.mensaje}")

print(f"\n¿Cadena íntegra?: {verificar_integridad(cadena)}")

modo_trampa(cadena, 2, "Mensaje alterado a propósito.")
print(f"\n¿Cadena íntegra después de trampa?: {verificar_integridad(cadena)}")

reparar_cadena(cadena, 2)
print(f"\n¿Cadena íntegra después de reparación?: {verificar_integridad(cadena)}")

guardar_cadena(cadena)
print("\nCadena guardada en cadena.txt")