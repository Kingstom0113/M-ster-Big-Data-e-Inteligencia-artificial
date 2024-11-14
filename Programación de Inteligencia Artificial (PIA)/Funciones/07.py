def mcd(a, b):
    while b != 0:
        a, b = b, a % b  # a se convierte en b, y b en el residuo de a dividido por b
    return a

print(mcd(56, 98))  # Salida: 14, porque el MCD de 56 y 98 es 14
print(mcd(101, 10)) # Salida: 1, porque el MCD de 101 y 10 es 1
