numero = int(input("Introduce un número: "))
contador = 0

while numero != 0:
    numero //= 10  # Dividir el número por 10 (eliminar el último dígito)
    contador += 1

print(f"El número tiene {contador} dígitos.")
