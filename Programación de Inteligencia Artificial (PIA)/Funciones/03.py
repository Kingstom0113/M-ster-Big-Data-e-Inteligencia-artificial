def suma_digitos(n):
    suma = 0
    while n > 0:
        suma += n % 10  # Obtiene el último dígito de n
        n = n // 10     # Elimina el último dígito de n
    return suma

print(suma_digitos(123))  # 1 + 2 + 3 = 6
print(suma_digitos(456))  # 4 + 5 + 6 = 15