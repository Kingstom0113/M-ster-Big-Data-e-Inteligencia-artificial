base = int(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

resultado = 1

for _ in range(exponente):
    resultado *= base

print(f"{base} elevado a la potencia de {exponente} es: {resultado}")
