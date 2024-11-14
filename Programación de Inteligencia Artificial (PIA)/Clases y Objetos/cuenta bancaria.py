class CuentaBancaria:
    def __init__(self, titular, saldo, tipo_cuenta):
        # Atributos de la cuenta bancaria
        self.titular = titular
        self.saldo = saldo
        self.tipo_cuenta = tipo_cuenta
    
    def depositar(self, cantidad):
        # Método para depositar dinero en la cuenta
        if cantidad > 0:
            self.saldo += cantidad
            return f"Has depositado {cantidad} unidades. El saldo actual es: {self.saldo}"
        else:
            return "La cantidad a depositar debe ser positiva."
    
    def retirar(self, cantidad):
        # Método para retirar dinero de la cuenta (asegurar que haya saldo suficiente)
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                return f"Has retirado {cantidad} unidades. El saldo actual es: {self.saldo}"
            else:
                return "Saldo insuficiente para realizar el retiro."
        else:
            return "La cantidad a retirar debe ser positiva."
    
    def mostrar_saldo(self):
        # Método para mostrar el saldo actual
        return f"El saldo actual de la cuenta es: {self.saldo}"

# Ejemplo de uso
cuenta1 = CuentaBancaria("Juan Pérez", 1000, "Ahorros")
cuenta2 = CuentaBancaria("Ana Gómez", 500, "Corriente")

# Realizando operaciones
print(cuenta1.depositar(200))  # Depositar dinero en cuenta1
print(cuenta1.retirar(300))    # Retirar dinero de cuenta1
print(cuenta1.mostrar_saldo())  # Mostrar saldo de cuenta1

print(cuenta2.depositar(-100))  # Intentar depositar un valor negativo
print(cuenta2.retirar(600))     # Intentar retirar más de lo disponible
print(cuenta2.mostrar_saldo())  # Mostrar saldo de cuenta2
