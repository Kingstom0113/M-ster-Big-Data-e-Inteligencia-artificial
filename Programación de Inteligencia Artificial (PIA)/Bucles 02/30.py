numero = int(input("Introduce un número: "))
suma_digitos = 0

while numero > 0:
    digito = numero % 10  # Obtiene el último dígito
    suma_digitos += digito  # Suma el dígito a la suma total
    numero //= 10  # Elimina el último dígito del número

print(f"La suma de los dígitos es: {suma_digitos}")
